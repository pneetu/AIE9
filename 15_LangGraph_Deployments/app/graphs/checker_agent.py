from __future__ import annotations
from typing import Literal
from typing_extensions import Annotated, TypedDict, NotRequired
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

# ----- State -----
class VibeState(TypedDict):
    messages: Annotated[list, add_messages]

    # optional fields
    retries: NotRequired[int]
    vibe: NotRequired[Literal["PASS", "FAIL"]]
    vibe_feedback: NotRequired[str]

# ----- LLM -----
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)

# ----- Nodes -----
def agent_node(state: VibeState) -> dict:
    system = SystemMessage(
        content=(
            "Approach every query with a bright, energetic curiosity. "
            "Be the friend who is both incredibly smart and genuinely kind. "
            "Aim for meaningful depth in few words. "
            "Only expand when the user asks for more detail."
        )
    )

    resp = llm.invoke([system, *state["messages"]])
    return {"messages": [resp]}

def checker_node(state: VibeState) -> dict:
    last = state["messages"][-1]
    judge = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

    prompt = [
        SystemMessage(
            content=(
                "You are a strict vibe checker.\n"
                "Decide if the assistant's last message is:\n"
                "- Warm and encouraging\n"
                "- Clear and actionable\n"
                "- Not judgmental or harsh\n\n"
                "Return ONLY in this exact format:\n"
                "VIBE: PASS|FAIL\n"
                "FEEDBACK: <one short sentence>"
            )
        ),
        last,
    ]

    verdict = judge.invoke(prompt).content.strip()

    vibe = "FAIL"
    feedback = "No feedback."

    for line in verdict.splitlines():
        if line.startswith("VIBE:"):
            vibe = line.split(":", 1)[1].strip()
        elif line.startswith("FEEDBACK:"):
            feedback = line.split(":", 1)[1].strip()

    return {"vibe": vibe, "vibe_feedback": feedback}

def rewrite_with_better_vibe_node(state: VibeState) -> dict:
    last = state["messages"][-1]
    feedback = state.get("vibe_feedback", "")

    rewriter = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    prompt = [
        SystemMessage(
            content=(
                "Rewrite the assistant's last message to PASS the vibe check.\n"
                "Keep the same meaning, but make it warmer and more encouraging.\n"
                "Be concise and actionable.\n"
                f"Vibe checker feedback: {feedback}"
            )
        ),
        last,
    ]

    rewritten = rewriter.invoke(prompt)

    return {
        "messages": [rewritten],
        "retries": state.get("retries", 0) + 1,
    }

# ----- Routing -----
MAX_RETRIES = 2

def route_after_vibe_check(state: VibeState) -> str:
    if state.get("vibe") == "PASS":
        return END
    if state.get("retries", 0) < MAX_RETRIES:
        return "rewrite_with_better_vibe"
    return END

# ----- Graph -----
def build_graph():
    g = StateGraph(VibeState)

    g.add_node("agent", agent_node)
    g.add_node("vibe_checker", checker_node)
    g.add_node("rewrite_with_better_vibe", rewrite_with_better_vibe_node)

    g.add_edge(START, "agent")
    g.add_edge("agent", "vibe_checker")

    g.add_conditional_edges(
        "vibe_checker",
        route_after_vibe_check,
        {
            END: END,
            "rewrite_with_better_vibe": "rewrite_with_better_vibe",
        },
    )

    g.add_edge("rewrite_with_better_vibe", "vibe_checker")

    return g.compile()

graph = build_graph()