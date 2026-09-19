# modes.md — Intent-Specific Branches

Each context shares the same proof contract (truth map, proof spine, shot contract).
They do not share the same arc, opening, evidence weight, or CTA.
Select the branch that matches where the demo is going before writing anything.

---

## Mode A — Hackathon Submission

**Viewer:** Judges reviewing 30–100+ projects in a session
**Time pressure:** High — judges are tired, looking for reasons to move on
**What they need:** Understand the problem, believe the solution works, feel the wow moment

### Arc
```
Problem in the world (real, felt)
→ Gap that currently exists
→ Your solution introduced
→ Live proof — end to end
→ Judge-relevant outcome mapped to rubric
```

### Opening
Start with the problem the judge already recognizes.
Do not open with the product name or tech stack.
The product appears only after the problem is established.

> Weak: "We built an AI agent orchestrator using LangGraph and FastAPI."
> Strong: "Every AI agent you build breaks the moment it has to talk to another one. Here's what we did about it."

### Evidence weight
- Show the complete workflow — not just the highlight moment
- Map the proof to judging criteria: innovation, technical complexity, impact, polish
- If judges care about technical depth, show the agent reasoning or graph execution
- If judges care about real-world impact, show the before/after for a real person

### Timing
- 60–90 seconds for a recorded submission
- 2–3 minutes for a live demo day
- Spend the first 15–20s on the problem — do not rush to the product

### CTA
Match to what the hackathon provides:
- "Try it at [URL]"
- "See the full repo at [GitHub link]"
- "We're [track name] — [judging criterion] is our focus"

### Wow moment rule
Every hackathon demo needs one moment that makes a judge lean forward.
Identify it in the proof spine and give it more screen time than anything else.
Do not bury it in the middle — build toward it.

---

## Mode B — X / Twitter Launch Post

**Viewer:** Scrolling a fast-moving feed, probably on mobile, likely with sound off
**Time pressure:** Extreme — 3 seconds to hook, 30–45 seconds total
**What they need:** Immediate visual proof that something interesting happened

### Arc
```
Punchy result first (most impressive output on screen immediately)
→ Rewind to show how it happened
→ CTA — one action only
```

OR for contrast-led demos:
```
Pain state shown (something slow, broken, manual)
→ One action
→ Result — fast
→ CTA
```

### Opening
The first frame is the hook. No title card. No logo. No intro.
The product is doing something impressive by second 2.

> Weak first frame: App loading screen with logo
> Strong first frame: The finished output already on screen — agent completed, task done, result visible

### Silent-watchable rule
Watch your cut with sound OFF before posting.
If a viewer cannot follow the task, change, and result without audio — add captions or rethink the composition.
Captions must be placed away from the important UI elements they'd cover.

### Evidence weight
- Before/after contrast is the most powerful proof pattern for X
- Keep the result on screen long enough to read — do not cut away the moment it appears
- Show one thing completely rather than five things partially

### Timing
- 30–45 seconds maximum
- If it runs longer, cut from the introduction — never from the proof or result
- Short looping clips (under 15s) can omit the end card — put the CTA in the post text

### CTA
One action. Choose the single action that follows from what you just showed.
Do not ask someone to visit, follow, share, AND join in the same breath.

> Weak: "Follow for more, share this, join our Discord, and sign up at our website"
> Strong: "Try it — [link]" or "Star the repo — [link]"

---

## Mode C — Demo Day Presentation

**Viewer:** Investors, mentors, or evaluators — engaged, willing to follow a story
**Time pressure:** Low — they are there to watch
**What they need:** Understand the problem deeply, trust the solution, believe in you

### Arc
```
Pain everyone in the room recognizes (make it felt, not stated)
→ Why existing solutions fail
→ Your approach — what's different
→ Full live walkthrough — start to finish, nothing skipped
→ Vision — what becomes possible
```

### Opening
Start with a scenario or a question the audience already feels.
Do not open with "Hi, we're [team name] and we built [product]."

> Weak: "Hi, we're Team Nexus and we built an adaptive skill learning platform."
> Strong: "You just started learning LangGraph. There are 47 tutorials online. None of them know what you already know or what you're actually trying to build. That's the problem."

### Evidence weight
- The walkthrough must be end-to-end — judges at demo day want to see the complete workflow
- Show technical depth: agent reasoning, graph execution, architecture if relevant
- Do not skip steps — if a step is slow, label the speed-up
- Prove the output is real: show a log, a file, a database entry, something inspectable

### Timing
- 2–3 minutes for a live demo
- Practice the walkthrough until it runs in 90 seconds — then add story around it
- Never rush the result — if you built toward it, let them see it

### CTA
Match to what you want from this audience:
- "We're raising — talk to us after"
- "Try the beta — [link]"
- "We're looking for [specific pilot partner type]"

---

## Mode D — LinkedIn / Portfolio

**Viewer:** Recruiters, hiring managers, fellow engineers, potential collaborators
**Time pressure:** Medium — they clicked, they have 60 seconds of patience
**What they need:** Proof you can build real things + technical credibility

### Arc
```
Technical challenge stated clearly
→ Architectural decision or interesting approach
→ Proof it works — with depth
→ What you learned or what's next
```

### Opening
Lead with the challenge, not the product name.
Technical viewers respect honesty about difficulty more than polished marketing.

> Weak: "Here's a demo of Nexus, my adaptive skill platform."
> Strong: "The hard part of building an adaptive learning agent isn't the AI — it's knowing when to change the plan mid-session. Here's how I solved it."

### Evidence weight
- Show technical depth: terminal output, LangGraph node execution, agent decision trace, architecture overlay
- One impressive technical detail shown completely > five features shown fast
- The viewer wants to believe you understand what you built — show the depth

### Timing
- 45–90 seconds
- Let technical details breathe — don't rush past the interesting part
- Captions matter here — many watch muted on the LinkedIn feed

### CTA
- "Full repo: [GitHub link]"
- "Open to [role type] roles — DM me"
- "See the full write-up: [link]"

---

## Choosing between modes

When the context is ambiguous, ask:
*"Who is the primary viewer and what decision are they making after watching this?"*

- Judge evaluating for prize → Mode A
- Stranger on a feed → Mode B
- Investor or evaluator → Mode C
- Recruiter or peer engineer → Mode D

A single product will often need all four. Plan them as a series — same proof spine, different arc and CTA.
