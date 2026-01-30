<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE9/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Vibe Check!](../00_Docs/Session_Sheets/01_Vibe_Check.md) |[Recording!](https://drive.google.com/file/d/1Rsmm0Hld3WFHRxhZpEDLN_JREQ43yhwu/view?usp=drive_link) | [Session 1 Slides](https://www.canva.com/design/DAG-EBzN2PQ/gE9-Uma217yych4M7GCjSw/edit?utm_content=DAG-EBzN2PQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 1 Assignment: Vibe Check](https://forms.gle/NeN59bCLdtXvwzVJ9) | [Feedback 1/13](https://forms.gle/1im4nmYK9cW9MFEk6) |

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE9 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)!


#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner.
    - Aspect Tested: Think of programming like organizing your thoughts about the world. Object-oriented programming (OOP) is a way to organize code around “objects” — little bundles that combine both data and behavior.
Here’s the idea in simple terms:
- Objects are like everyday things.
  - Example: A Dog is an object.
  - It has properties (data): name, age, color.
  - It has actions (behavior): bark(), eat(), sleep().
- A Class is a blueprint for making objects.
  - The class Dog describes what every dog knows (properties) and can do (actions).
  - An object is a specific dog you create from that blueprint, like fido or luna. These are called instances.
- Why this is useful:
  - It mirrors how we think about real things.
  - Keeps related data and actions together, making code easier to understand and change.
  - Helps you reuse code instead of rewriting it.
The four big ideas (pillars) of OOP:
1) Encapsulation (keep things neatly packed)   - You bundle data and the functions that work on that data in one place (the object).
   - You expose a simple interface (like start() and stop()) and hide messy details inside.
   - Benefit: fewer bugs and easier changes.
2) Inheritance (reuse and specialize)
   - You create a new class that builds on an existing one.
   - Example: Vehicle → Car and Bike. Car “inherits” common things from Vehicle, and adds its own details.
   - Benefit: reuse code instead of copying it.
3) Polymorphism (same request, different behavior)
   - You can call the same method name on different objects, and each object does the right thing in its own way.
   - Example: call move() on a Car or a Bike. Both move, but differently.
   - Benefit: write flexible code that works with many kinds of objects.
4) Composition (build from parts)
   - An object can be made of other objects.
   - Example: a Car has an Engine and Wheels.
   - Benefit: small, focused pieces that snap together like LEGO.
A tiny example (Python-like, just to see the idea):
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return f"{self.name} says woof"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"
animals = [Dog("Fido"), Cat("Misty")]
for a in animals:
    print(a.speak())
What this shows:
- Classes (Animal, Dog, Cat)
- Objects/instances (Dog("Fido"), Cat("Misty"))
- Inheritance (Dog and Cat extend Animal)
- Polymorphism (same speak() call, different results)
How to practice (quick, friendly steps):
- Pick something simple you know well (a To-Do task, a Book, a BankAccount).
- List 3–5 properties (for a Book: title, author, pages).
- List 2–3 actions (open(), read(), bookmark()).
- Write a class for it, then create two objects with different data.
- Call the methods and see the different outputs.
- Optional: make a second class that inherits and changes one method.
Encouragement: You don’t need to memorize jargon. Start by modeling a familiar thing with properties and actions. Keep it tiny, try it, and iterate. You’ve got this—one small class at a time!

2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested:  (https://arxiv.org/abs/2406.06608)(Generative Artificial Intelligence (GenAI) systems are increasingly being deployed across diverse industries and research domains. Developers and end-users interact with these systems through the use of prompting and prompt engineering. Although prompt engineering is a widely adopted and extensively researched area, it suffers from conflicting terminology and a fragmented ontological understanding of what constitutes an effective prompt due to its relatively recent emergence. We establish a structured understanding of prompt engineering by assembling a taxonomy of prompting techniques and analyzing their applications. We present a detailed vocabulary of 33 vocabulary terms, a taxonomy of 58 LLM prompting techniques, and 40 techniques for other modalities. Additionally, we provide best practices and guidelines for prompt engineering, including advice for prompting state-of-the-art (SOTA) LLMs such as ChatGPT. We further present a meta-analysis of the entire literature on natural language prefix-prompting. As a culmination of these efforts, this paper presents the most comprehensive survey on prompt engineering to date.) - Prompt engineering is central to how people use GenAI, but the field suffers from inconsistent terminology and fragmented understanding.
- The paper organizes the field by building a structured taxonomy and analyzing applications.
- It introduces: a 33-term vocabulary, 58 LLM prompting techniques, and 40 techniques for other modalities.
- It offers best practices and guidelines for effective prompting, including advice for SOTA models like ChatGPT.
- It includes a meta-analysis of natural language prefix-prompting literature.
- The authors position this as the most comprehensive survey of prompt engineering to date.

3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: Rook-7 picked up a heartbeat in the salvage yard: not a battery, but a seed. In its chest cavity, soil collected, the seed sprouted. Rook-7 shielded it from rain, angled its solar panel to light the sprout. In return, the sprout made the robot pause, count time in leaves. The yard's other machines teased: “You can’t talk to a plant.” But nights, wind translated. The sprout flickered in green syllables—thirst, joy, stretch. Rook-7 learned to listen beyond code. When scrap-haulers came, Rook-7 planted its feet and refused to budge. The haulers shrugged, went around. Seasons turned. Flowers unfurled like tiny sunrises. Birds visited, soft-clawing Rook-7’s shoulders. “Unexpected,” it logged, feeling a warmth no circuit owned. The yard wasn’t lonely anymore; it was a garden with a friend.

4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: - Apples: 12 apples ÷ 4 per pack = 3 packs
- Oranges: 9 oranges ÷ 3 per pack = 3 packs
You need 3 packs of apples and 3 packs of oranges.

5. Rewrite the following paragraph in a professional, formal tone…
(TapeAgents provide a comprehensive record of application functions, facilitating a deep understanding of each component. This detailed logging enables targeted improvements and optimizations, enhancing the application’s overall quality and user experience.)
    - Aspect Tested:  TapeAgents maintain a comprehensive audit trail of application functionality, enabling a thorough understanding of each component. This granular logging supports targeted enhancements and optimizations, thereby improving overall software quality and the end-user experience.


#### ❓Question #1:

Do the answers appear to be correct and useful?
##### ✅ Answer: The response to the OOP question was very detailed and covered topics with a broad scope. I appreciated this depth because it addressed not only the immediate question but also potential follow-up questions I might have in the future. The detailed explanations helped clarify doubts I might otherwise have had about specific concepts. Having more information is especially valuable when learning complex topics. I also liked the bullet-point structure, which made the content easier to follow and prevented it from feeling overwhelming. However, because of the level of detail, it was easy to lose track while reading. Additionally, the response took noticeably longer to generate compared to shorter prompts that required less computation or explanation, which were almost instantaneous.


---

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:
1. Prompt: Help me think through the pros and cons of Software Engineering job vs LLM Engineering job

   - Result: Great question. Here’s a clear way to think about it, plus some prompts to help you choose.
What each role usually means
- Software Engineer (SE): Design/build/maintain systems, features, and platforms; mature tooling; reliability and scalability are core.
- LLM Engineer (umbrella term): Could be applied LLM product work (prompting, RAG, evals), LLM infra/serving (throughput/latency/cost), data/finetuning pipelines, safety/evals, or research-adjacent applied ML. Most industry roles focus on integrating and evaluating models rather than training from scratch.
Pros and cons at a glance
Software Engineering
- Pros
  - Broad demand across industries; clearer career ladders and expectations.
  - Mature tooling and processes; success metrics are concrete (latency, uptime, tests).
  - Highly transferable skills (systems, APIs, cloud, reliability).
  - Lower volatility and less “science experiment” ambiguity.
- Cons
  - More maintenance/legacy work; slower tech novelty.
  - Impact can feel incremental; more constraints from existing systems.
  - Competitive, sometimes commoditized skill signals (e.g., DSA-heavy interviews).
LLM Engineering
- Pros
  - Cutting-edge, high-leverage; small teams can ship big user-visible features.
  - Premium opportunities at AI-first companies; high learning velocity.
  - Blend of product, data, and ML—great for building modern product sense.
  - Chance to influence evaluation standards, safety, and new UX patterns.
- Cons
  - Ambiguity: quality is harder to measure; evals are tricky and often bespoke.
  - Tooling and best practices are immature and change fast.
  - Dependency on third-party models, cost constraints, policy/compliance complexity.
  - Market volatility; titles vary widely; risk of skills getting stale if you only “prompt.”
  - Truly training models is rare outside well-funded labs.
Day-to-day differences
- SE: Shipping features; code reviews; tests; reliability; on-call; system design; stakeholder coordination.
- LLM: Prototyping prompts; building RAG pipelines; curating/evaluating data; setting up eval harnesses; cost/latency/quality trade-offs; model/SDK upgrades; monitoring hallucinations/safety; sometimes finetuning and serving (vLLM/TensorRT-LLM).
Skills emphasis
- SE core: System design, APIs, databases, distributed systems, testing/observability, cloud.
- LLM core: Python, embeddings/tokenization, retrieval/vector DBs, prompt engineering, eval design (automatic and human), data pipelines, MLOps, model serving, basic ML math, familiarity with RLHF/finetuning concepts.
Career capital and transferability
- SE gives durable foundations usable anywhere.
- LLM eng gives frontier product intuition, data/eval chops, and AI infra skills; still benefits greatly from strong SE fundamentals. Pure “prompt-only” skill is less durable; pair it with data/eval/infra depth.
Market reality (general)
- SE demand is broad and steady; hiring cycles fluctuate but roles exist in every sector.
- LLM roles are concentrated in AI-native companies and AI-platform teams; high upside but more localized and variable. Many roles are “AI product engineer” in practice.
How to choose (quick self-assessment)
- Pick SE if you prefer stability, clear specs/metrics, mature tooling, and large-scale systems.
- Pick LLM Eng if you enjoy ambiguity, fast prototyping, reading papers/blogs, crafting evals, and reasoning about probabilistic behavior, costs, and UX trade-offs.
- Hybrid: Join a product team building LLM features; you’ll do solid SE plus applied LLM work, keeping options open.
Low-risk experiments (2–4 weeks)
- LLM project: Build an end-to-end feature (RAG over docs or an agent for a specific workflow). Implement:
  - Retrieval quality evals (precision/recall, manual spot checks).
  - Cost/latency instrumentation; mitigate with caching and truncation.
  - Guardrails/safety filters; A/B prompts; simple finetune if data exists.
  - Shipping it to a few real users and iterating on feedback.
- SE project: Design and deploy a small service with strong reliability:
  - Clear API, load tests, observability (tracing/metrics), blue/green deploys, and an incident runbook.
Interview prep differences
- SE: DSA, system design, code quality, testing, reliability.
- LLM: Build/eval a RAG system, cost vs quality trade-offs, prompt/debug live, design eval pipelines, safe-guarding, model/infra choices, sometimes lightweight ML math and PyTorch.
Hedging strategies
- Choose an SE role at a company shipping AI features; volunteer for LLM-related tickets.
- In an LLM role, invest in core SE (infra, testing, scalability) so your skills remain durable.
- Aim for roles that include evals, data quality, and serving—not just prompt tinkering.
If you lean LLM, a 90-day ramp
- 0–30 days: Ship a RAG MVP; set up eval harness; baseline cost/latency; read a practical LLM book/course; learn vLLM and a vector DB.
- 31–60 days: Add guardrails, caching, chunking strategies; introduce automatic + human evals; reduce cost/latency by 30–50%.
- 61–90 days: Finetune or adapter-tune on your domain data; harden CI/CD for models/prompts; document runbooks and failure modes.
Questions to tailor advice
- What parts of engineering energize you: reliability and systems, or fast prototyping with messy data?
- How comfortable are you with ambiguity and imperfect metrics?
- Do you want broader role optionality in 2–5 years, or are you excited to specialize now?
- What’s your background in ML/math, and do you want to deepen it?
- How much risk (market, role definition) are you comfortable taking for higher upside?
If you share your background and what you enjoy day-to-day, I can map a path and suggest specific roles and projects.

2. Prompt:  Help me plan a birthday surprise for my husband, he is not  materialistic, but loves meeting close friends.

   - Result: Love this. Since he values time with close friends, let’s make the gift a meaningful, low‑stress gathering. Here are a few surprise concepts plus a simple timeline and scripts. Pick what fits, and I’ll tailor it to your details.
Surprise concepts (experience-focused)
- Intimate supper club at home
  - Potluck or favorite-cuisine menu; seat 8–12 max for cozy vibes.
  - After dessert, do a “toast circle” and present a jar of short notes from friends.
  - Play a 3–5 minute video montage of 20–30 second clips from friends.
- Sunset picnic pop‑up
  - At a park/backyard with blankets, string lights, a portable speaker.
  - Friends arrive early with simple picnic spreads; you walk him in at sunset.
  - Backup plan: living room picnic if weather turns.
- Progressive hangout
  - Stop 1 coffee, stop 2 activity (mini-golf, gallery, bowling, walk), stop 3 dinner at home where more friends are waiting.
  - Each stop adds one or two surprise guests so it builds gently.
- Backyard micro‑festival
  - Projector movie or acoustic set by a musician friend; yard games; taco bar/BBQ.
  - “Memory lane” photo line with clothespins, ending at a group photo spot.
- Hike + picnic + letters
  - Small group morning hike, picnic at the top, each friend reads a short note.
  - Great for someone who loves nature and low-key connection.
- Volunteer + brunch reveal
  - Do a service hour for a cause he cares about, then surprise brunch in a reserved room nearby.
Make-it-special touches (non-material)
- Video montage: ask friends for 20–30 sec clips; compile in iMovie/CapCut.
- Message jar: “Reasons we love you” or “Open when…” notes.
- Custom trivia about him (Kahoot or cards).
- Signature mocktail/cocktail named after him; a simple playlist of his favorites.
Cover story ideas to get him there
- “Date night—wear comfy/smart casual, I’ve got reservations.”
- “Help me test a picnic spot for a future event.”
- “Our friend needs us to swing by to check something—five minutes tops.”
- If he dislikes big surprises, do a “soft reveal” a couple hours before: tell him there will be a small get-together with close friends.
Simple timeline
- 4–6 weeks: choose concept/date; make short guest list; secure venue/park permit if needed.
- 3 weeks: send invites; ask for video clips and notes; assign a co‑conspirator to handle arrivals/parking.
- 1 week: finalize headcount/menu; gather decor (printed photos, string lights); create playlist/trivia.
- 2–3 days: shop/cook/confirm weather backup; send guests reminder with arrival time 30 minutes before him.
- Day-of: hide cars, set up food/drink zones, test projector/speaker, designate a photographer, keep first toast to kick things off.
- After: share photos/video; send a quick thank-you message.
Menu ideas (easy and crowd-pleasing)
- Grazing board + big-batch mains (pasta bake, tacos, curry bar) + bakery cake or favorite dessert.
- Drinks: water, one signature drink, beer/wine; include non-alcoholic options.
- Ask about dietary needs; label a couple items vegan/gluten-free if relevant.
Sample invite text to friends
- “Shh! We’re surprising [Name] for his birthday on [Date]. He isn’t into big parties—just quality time with close friends. Plan: arrive at [Time] (he arrives at [Time+30]). Venue: [Address/park pin]. Please keep cars out of sight. Optional: send a 20–30 sec video or 1–2 sentence note we’ll compile. Thanks!”
Sample message to him (if soft reveal)
- “I planned a small get-together with a few close friends for your birthday tonight. Nothing fancy—good food, chill vibes. We’ll head out at [Time]; dress comfy.”
Budget savers
- Potluck sides/desserts; you handle mains.
- Borrow projector/lights; print black-and-white photos at a drugstore.
- DIY playlist and signature drink instead of full bar.
To tailor this perfectly, a few quick questions:
- Rough headcount and city/season (indoor vs outdoor)?
- Budget range?
- His favorite foods, music, and any no-go’s?
- How surprised does he like to be (big reveal vs gentle)?
- Weekend or weeknight, and any kids joining?
- Any dietary restrictions or alcohol preferences?
Share your answers and I’ll draft a concrete plan with a checklist, menu, shopping list, and exact timeline for the day.

3. Prompt: What can I cook with tofu, broccoli and bread in fridge

   - Result: Nice trio—you can make a satisfying meal fast. Pick one that matches what’s in your pantry:
- Crispy tofu + broccoli stir-fry on toast
  - Sauce: 2 tbsp soy sauce, 1 tbsp vinegar or lemon, 1 tsp sugar/honey, chili to taste, splash water; optional 1 tsp cornstarch and 1 tsp sesame oil.
  - Pan-sear tofu cubes till golden, add broccoli (small florets), a little water to steam 1–2 min, pour in sauce to glaze. Spoon over buttered toast.
- Tofu–broccoli open-faced melts
  - Sauté broccoli until bright and tender. Mix with crumbled tofu, a spoon of mayo/vegan mayo or a little olive oil, mustard, salt, pepper, paprika. Pile on toasted bread, top with cheese or nutritional yeast, broil/pan-cover to melt.
- Peanut-sesame tofu and broccoli on toast
  - Sauce: 1 heaping tbsp peanut butter, 1 tbsp soy, 1 tsp vinegar/lime, 1 tsp sugar, warm water to loosen, chili if you like.
  - Stir-fry tofu and broccoli, toss with sauce. Serve over toast or with toasted bread chunks.
- Curried tofu-broccoli salad sandwiches
  - Steam or sauté chopped broccoli till tender-crisp. Mix with crumbled tofu, curry powder, mayo/vegan mayo or yogurt, lemon, salt, pepper; add raisins or chopped pickles if you have them. Pile on bread with greens.

- Tofu scramble with broccoli on toast
  - Crumble tofu with turmeric, salt, pepper, garlic/onion powder. Sauté broccoli, add tofu, cook till a little golden. Finish with a splash of soy or lemon. Serve on toast.
- Broccoli “pesto” toast with seared tofu
  - Blitz steamed broccoli with olive oil, garlic, lemon, salt, pepper; add nuts/seeds or a spoon of breadcrumbs for body if available. Spread on toast, top with crispy tofu.
- Sheet-pan or skillet toasties
  - Toss tofu and broccoli with olive oil, garlic, chili, salt, pepper. Roast at high heat or pan-sear till browned. Top bread with mustard or tomato, pile mixture on, add cheese if you want, and broil or cover in pan to melt.
- Tofu katsu-style sando with quick broccoli slaw
  - Make breadcrumbs from toasted bread. Coat tofu in a little mayo/mustard then crumbs; pan-fry till crisp. Shred broccoli finely, toss with vinegar, a pinch of sugar, salt. Sandwich with a quick sauce (ketchup + soy + Worcestershire/tonkatsu-ish).
Want me to tailor one to what you actually have (soy sauce, garlic, peanut butter, mayo, cheese, lemon, spices)?


#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer: The responses were very detailed for each prompt. While I appreciate in-depth explanations for educational topics, this level of detail felt overwhelming for tasks related to chores or fun activities. In those cases, I prefer concise, action-oriented guidance that allows me to act quickly rather than spending time processing extensive information or planning steps. I found myself wanting to reduce the depth of the responses to better match the goal of minimizing mental effort. Overall, the intent of the experience should be to reduce cognitive load, not add complexity by overloading the user with information. The experience should minimize cognitive load and support fast task completion, focusing on clear task-action steps instead of detailed what, how, why, or background narratives.


---

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:
1. Prompt: What does my schedule look like tomorrow?

   - Result: I’d love to help map it out, but I don’t have access to your calendar. If you paste your appointments or list your commitments and priorities, I’ll turn them into a clear, realistic plan.
Quick way to build tomorrow now:
- Tell me:
  1) Fixed events (times + duration)
  2) Top 3 priorities (deep work/tasks)
  3) Energy peaks (morning/afternoon/evening)
  4) Constraints (commute, childcare) and one self-care non‑negotiable
- I’ll timebox everything with buffers and give you a one-glance schedule.
If you want a ready-made template to tweak, use this:
- Morning
  - Start-up (10 min): review priorities, define 1 must-win
  - Deep work block (60–90 min)
  - Short break (10 min)
  - Admin/quick tasks (30–45 min)
- Midday
  - Meetings or continued focus (60–90 min)
  - Lunch + walk or recharge (30–45 min)
- Afternoon
  - Deep work or project block (60–90 min)
  - Buffer for messages/email (20–30 min)
  - Small tasks/cleanup (20–30 min)
- End of day
  - Wrap-up (10 min): note wins, set top 3 for next day
  - Personal wind-down/self-care (30–60 min)
Want me to draft a concrete schedule? Share your fixed events and top 3 priorities, or tell me “Plan a 9–5 day with a gym session and dinner,” and I’ll build it.

2. Prompt: What time should I leave for the airport?

   - Result: I can help you back-calculate a low-stress leave time. A quick rule of thumb:
- Domestic flights: be at the airport 2 hours before departure (2.5–3 hours at big hubs, holidays, or peak times).
- International flights: 3 hours before (3.5 at busy times).
- Add your door-to-terminal time: drive/rideshare time + 15–30 minutes for parking, shuttle, or rental car return.
- Add a 10–20 minute “calm buffer” if you like arriving unrushed.
Example: 2:00 pm domestic flight at a big airport, 40-minute drive, checking a bag, no PreCheck → aim to be at the airport by 12:00. Add 40 min drive + 20 min parking/shuttle + 10 min buffer → leave around 10:50–11:00 am.
If you want a precise leave time, tell me:
- Departure airport, date, and flight time
- Domestic or international, and airline
- Checked bags? TSA PreCheck/CLEAR?
- How you’re getting there and typical drive time
- Parking or rental car return
- Any special factors (kids, pets, mobility needs, prefer extra buffer)
We’ll set a time that feels calm and comfortable for you.


#### ❓Question #3:

What are some limitations of your application?
##### ✅ Answer: Since the system does not have access to my calendar, the responses were necessarily based on general information, which is understandable. If calendar context were available, the system could provide more personalized, one-line, action-oriented responses, for instancee, quickly surfacing relevant details during a busy schedule such as checking email timing around airport activities. Context awareness like this would significantly improve efficiency and reduce the need for additional planning or interpretation by the user.


---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- _describe adjustment(s) here_ : Since I noticed that my application was running slow meaning the prompt given to the application window was delayed to generate the response. Also my application was generating long responses that delayed the whole process, which means the user would get frustrated, so  I tried a few changes to test it.
1. No changes at all, response time was way long(32 sec), and lengthy response. 
2. Added async to the function ‘chat’ to fasten the multiple requests concurrently.
3. Set the max tokens to some value, to limit the output.
4. Set the temperature to 0.6 
5. I did not set the temperature 

Explain the concept of object-oriented programming in simple terms to a complete beginner.
##### Results:
1. _Comment here how the change(s) impacted the vibe check of your system_
2. (Response when async to the function, model : gpt-4.1-mini, max_tokens = 250, temperature set to 0.6)
 Of course! Think of object-oriented programming (OOP) like organizing things in the real world.Imagine you have a bunch of toys. Each toy can be thought of as an "object." Each object has two main things:
  **Attributes (or properties):** These are details about the object. For example, a toy car might have a color, size, and brand.
  **Methods (or actions):** These are things the object can do. For example, the toy car can "move" or "honk."
In OOP, you create "blueprints" called **classes** that define what attributes and methods objects of that type will have. Then, you make actual objects (called **instances**) from those blueprints.
So, instead of writing all your code as one big list of instructions, you organize it around objects that represent things in your program. This makes your code easier to understand, reuse, and manage.
Does that help? Would you like me to give a simple example?

3. (Response when async to the function, model : gpt-4.1-mini, max_tokens = 250)
Of course! Imagine you’re playing with a set of toy cars. Each toy car has its own color, size, and wheels, and each car can do things like move forward or stop. 
Object-oriented programming (OOP) works kind of like that. Instead of just writing instructions step-by-step, you create “objects” that represent things—like a toy car. Each object has:
1. **Properties** (also called attributes) — these are details about the object, like the car’s color or size.
2. **Methods** — these are actions the object can do, like move or stop.
In OOP, you design your program by creating these objects and telling them what to do, making it easier to organize and manage your code. It’s like building with blocks, where each block is an object with its own features and behaviors.
Does that help? I’m happy to explain any part in more detail!

4. (Response when non-async to the function, model : gpt-5)
Think of object-oriented programming (OOP) as a way to organize code the same way you think about real-life things.
- Objects: Things you can talk about, like a Dog or a BankAccount. Each object has:
  - Attributes (data): what it is (a dog’s name, a bank balance)
  - Methods (actions): what it can do (bark, deposit money)
- Classes: A blueprint or recipe for making objects. The class describes what attributes and methods the objects will have. From one class, you can make many objects.
Four core ideas (in friendly terms):
- Encapsulation: Keep data and the code that works on it together, and control access. Like using a TV remote instead of poking the circuit board.
- Inheritance: Make a new class that reuses and extends an existing one. A Dog is an Animal with extra doggy stuff.
- Polymorphism: Different objects respond to the same action in their own way. Dog.speak() barks, Cat.speak() meows.
- Abstraction: Show the simple controls, hide the complex guts. You drive a car without knowing the engine details.
Tiny example (Python):
class Dog:
    def __init__(self, name):
        self.name = name      # attribute (data)
        self.energy = 100


    def bark(self):           # method (action)
        print(self.name + " says woof!")
    def run(self):
        self.energy -= 10     # encapsulated change to internal state
class GuideDog(Dog):          # inheritance
    def bark(self):           # polymorphism (same method, different behavior)
        print(self.name + " gives a quiet woof.")
rex = Dog("Rex")
rex.bark()    # Rex says woof!
rex.run()
buddy = GuideDog("Buddy")
buddy.bark()  # Buddy gives a quiet woof.
How to start practicing:
- Pick something you know (Car, Student, GameCharacter).
- List 3–5 attributes (for Car: color, speed) and 3–5 methods (accelerate, brake).
- Write a simple class, create a couple of objects, call their methods.
- Then try a subclass (e.g., ElectricCar) that changes or adds behaviors.
You’ve got this—keep it small, model something you enjoy, and iterate.

## Submitting Your Homework
### Main Assignment
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - For your initial repo setup see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file (the one in your `AIE9/01_Prototyping_Best_Practices_and_Vibe_Check` folder)
4. Complete all three Activities:
    - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
    - **Activity #2:** Test your assistant with personal prompts it should be able to answer
    - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to your AIE9 repo.
+ The public Vercel URL to your updated Challenge project on your AIE9 repo.
