# Example: Nexus — Adaptive Skill Development Platform

This example walks through the full skill pipeline applied to Nexus —
an adaptive learning platform built on LangGraph, FastAPI, and Next.js.
Use this as a reference when applying the skill to your own project.

---

## Context detected

- **Product:** Nexus — adaptive skill learning agent
- **Platform:** X/Twitter launch post + Hackathon submission
- **Duration:** 45s (X post) / 90s (hackathon)

---

## Demo thesis

```
For a developer trying to learn LangGraph who doesn't know where to start,
show a learning path being generated that skips what they already know,
prove it with the visible skill graph adapting in real time,
then ask them to try it at [URL].
```

---

## Truth map (example)

| Claim | Status | Condition / Source |
|---|---|---|
| Generates personalized learning path from stated goal | ✅ Verified | Works in current build |
| Skips topics user already knows | ✅ Verified | Based on onboarding assessment |
| Skill graph updates as user completes modules | ✅ Verified | LangGraph state visible in dev tools |
| Recommends next resource in real time | ✅ Verified | FastAPI endpoint returning recommendation |
| Integrates with GitHub to detect existing skills | ⚠️ Conditional | Only for users who connect GitHub |
| Supports team learning paths | ❌ Excluded | Not in current build — roadmap |

---

## Proof spine (X/Twitter version)

```
Starting state:  User types: "I want to learn LangGraph to build AI agents"
Action:          Nexus runs the assessment and generates the path
Response:        Skill graph populates — skipping Python basics (user knows this)
Outcome:         A personalized 5-step path appears — starts at LangGraph node basics
Verification:    User expands one node — sees it links to their actual skill level, not a generic tutorial
```

---

## Arc selected

**X/Twitter:** Result-first → rewind → CTA

Reason: The skill graph populating visually is the most striking moment. Lead with the finished graph,
then show the 10-second generation process that produced it. The contrast between "generic course" and
"personalized path" is the story.

---

## Hook options

```
Hook A (recommended): "This learning path knows what you already know. Watch it skip the basics."
Hook B: "Stop reading tutorials written for everyone. Here's a path built for you."
Hook C (result-first): "That's your personalized LangGraph path — here's how it got there in 10 seconds."
```

**Locked hook:** Hook A — specific, begins the proof, sets up the contrast immediately.

---

## Shot plan (45-second X version)

| # | Time | Screen State | Narration | Technical Detail | Edit Note |
|---|---|---|---|---|---|
| 1 | 0–3s | Skill graph fully populated, personalized path visible | "This learning path knows what you already know." | | Hold — let viewer read the graph |
| 2 | 3–6s | Cut back to: blank Nexus input field | "Here's how it got there." | | Rewind signal — viewer understands arc |
| 3 | 6–10s | User types: "I want to learn LangGraph to build AI agents" | "Type your goal." | | Keep typing animation — feels real |
| 4 | 10–18s | Assessment runs — LangGraph nodes executing | "Nexus checks what you already know." | Show node execution briefly | 2x speed on assessment — label it |
| 5 | 18–30s | Skill graph populates — Python basics node grayed out | "Skips Python basics — you know this. Starts at node architecture." | Highlight skipped nodes | Slow — this is the proof |
| 6 | 30–38s | User expands one node — sees linked resource matching their level | "Every step links to something at your actual level." | | Hold on the resource detail |
| 7 | 38–45s | Nexus homepage / sign up screen | "Try it — [URL]" | | Clean ending — one action |

---

## Full script (45s X version)

**[HOOK — 0–3s]**
"This learning path knows what you already know. Watch it skip the basics."

**[REWIND — 3–6s]**
"Here's how it got there."

**[ACTION — 6–18s]**
"Type your goal. Nexus checks what you already know — 2x speed — then builds the path."

**[RESULT — 18–38s]**
"Skips Python basics — you already know this. Starts at LangGraph node architecture.
Every step links to something at your actual level — not a generic tutorial."

**[CTA — 38–45s]**
"Try it — [URL]"

---

## Recording notes

- Zoom to 125% — skill graph node labels must be readable at phone feed size
- Demo account: pre-load with Python and FastAPI as known skills, LangGraph as goal
- Dry run: verify the graph correctly grays out Python basics before recording
- Reset path: clear assessment → re-run onboarding → verify starting state
- Recorder: Cap (cross-platform) or Screen Studio (Mac) — auto-zoom on skill graph population

---

## Hackathon version differences (90s)

For hackathon: use Mode A arc — problem first.

**Additional hook:**
"Every developer learning AI agents hits the same wall — 47 tutorials, none of them know what you already know or what you're actually trying to build. Nexus fixes that."

**Add before the demo:**
- 15s: Show the problem — generic course list, user scrolling, overwhelmed
- Then: "Here's what personalized actually looks like."

**Add after the demo:**
- Show LangGraph execution trace briefly (5s) — proves the architecture is real
- "Built on LangGraph, FastAPI, Next.js — [repo link]"

---

## Follow-up video ideas

| Feature | Viewer | Arc |
|---|---|---|
| GitHub integration — detects existing skills from repos | Developer with existing GitHub projects | LinkedIn / portfolio |
| Team learning paths | Engineering manager | Demo day |
| How the LangGraph graph works under the hood | Technical hiring manager | LinkedIn |
| Full onboarding walkthrough | New user | Tutorial / help center |
