---
name: demo-video-playbook
description: >
  Plan, script, stage, or review evidence-led software demo videos. Use for new product launches,
  feature launches, hackathon submissions, X/Twitter clips, demo day presentations, LinkedIn portfolio
  demos, AI agent or LangGraph workflows, CLI or API tools, and demo series — when the agent must
  decide what to show, say, prove, cut, record, or ask viewers to do next. Activates on: "/demo-video",
  "help me make a demo", "demo script", "record my product", "plan a demo", "demo for hackathon",
  "launch video", "demo day", "review my demo". Not for brand films, testimonials, or videos that
  never demonstrate working software.
---

# Demo Video Playbook

A software demo is a claim made visible.
Build it around the smallest honest proof that matters to the intended viewer.

> Core insight: building the product is often easier than explaining it clearly in under a minute.
> When you record your own product, the explanation lives in your head. The viewer has none of it.
> Every shot must earn its place by proving something real.

---

## Route the request

Choose by the **state of the work** first:

- **New demo** — nothing recorded yet → run the main flow
- **Existing script, storyboard, rough cut, or export** → use the review path
- **Product with several audiences, jobs, or capabilities** → plan a demo series before scripting one video
- **Only a recording or editing question** → read `references/capture.md` and scope the answer to that operation

Then choose the **intent branch** in `references/modes.md`:

| Context | Branch |
|---|---|
| Hackathon submission | Judging-rubric aware, wow-moment critical |
| X / Twitter launch post | Hook in 3s, silent-watchable, punchy CTA |
| Demo day presentation | Full story arc, live or recorded |
| LinkedIn / portfolio | Credibility-first, technical depth |

Each context shares the same proof contract but does not share the same opening, arc, evidence, or CTA.
Read `references/modes.md` to select the right branch before scripting.

---

## Main flow: frame → verify → prove → cut → stage → gate

### 1. Frame the assignment

Resolve: viewer, decision, real-world scenario, destination, availability, runtime, and next action.
Infer from the project and publishing context when the answer is already present.
Ask only for a choice that would materially change the demo.

Write one **demo thesis**:

```
For [viewer], show [job] moving from [before] to [after],
prove it with [inspectable detail], then ask them to [next step].
```

**Done when:** the demo has one primary viewer, one job, one result, and one CTA.

---

### 2. Build the truth map

Inspect available materials: running software, README, routes, components, agent graphs, LangGraph nodes,
commands, tests, feature flags, release notes, sample data, API responses, logs, screenshots, approved messaging.

Classify each planned claim:

| Claim | Status | Condition / Source |
|---|---|---|
| [feature or behavior] | ✅ Verified | Works in current build — can be shown live |
| [feature or behavior] | ⚠️ Conditional | True only for [specific data / env / config] |
| [feature or behavior] | ❌ Excluded | Unreleased / unreliable / misleading / private |

**Rules — never break these:**
- A mockup is not a working product. If it's a mockup, label it on screen.
- A best-case AI run is not typical behavior. If showing best case, note it.
- Roadmap features that aren't shipped stay out — or are labeled "coming soon" explicitly.
- Generated output must show enough input, result, and human or system control to be judged.
- Private data, credentials, internal URLs, and unreleased features stay outside the frame.

Read `references/proof-patterns.md` when the value is invisible, async, distributed, or easy to fake —
especially for AI agents, LangGraph workflows, and background processing.

**Done when:** every spoken or shown claim has a verified source, stated condition, or explicit exclusion.

---

### 3. Choose the proof

Pick the evidence pattern that makes the value **inspectable** by a cold viewer.

The **proof spine** is the logical cause-and-effect chain every demo must follow:

```
Starting state → Meaningful action → Product response → Outcome → Verification
```

Write it explicitly before scripting:

```
Starting state:  [what the screen shows before anything happens]
Action:          [the single thing the user or system does]
Response:        [what the product does — what visibly changes]
Outcome:         [the result — what is now true that wasn't before]
Verification:    [how the viewer confirms this is real — a field, log, file, number, agent trace]
```

The edit may reveal the outcome first — but the viewer must still be able to reconstruct the chain.
Keep **one primary spine**. Put secondary capabilities in a cut list or a follow-up video.

Read `references/proof-patterns.md` for evidence patterns when the interesting work is invisible.

**Done when:** removing any beat would break the claim, causality, or proof.

---

### 4. Design the explanation

Read `references/workflow.md` for arc selection, hook writing, cut decisions, and difficult selection problems.
Read `references/modes.md` for the intent-specific opening, pace, and CTA.

Choose a hook that **begins the proof** — show the task, result, contrast, constraint, or objection.
Do not open with a slogan that delays the software appearing on screen.

Write a **shot contract** for every beat:

- Exact frame and starting state
- User or system action
- Narration or on-screen copy
- State change and proof detail
- Edit treatment — including disclosed cuts or speed changes
- Hold requirement and reset steps

Use the product's real nouns. Narration explains meaning and transitions — it does not read the interface aloud.
Give the proof **longer screen time** than the setup.

Read `references/templates.md` for the exact output shape to deliver.

**Done when:** every important narration line arrives with matching on-screen evidence, and the muted cut still
preserves the task, change, result, and next step.

---

### 5. Stage a repeatable take

Prepare: safe demo environment, believable data, stable starting state, reset path, readable application scale,
deliberate cursor path, clean audio, and a truthful fallback for unreliable steps.

Read `references/capture.md` before recording or directing an edit.

**Done when:** the complete proof spine succeeds **twice** from the written reset steps.

---

### 6. Run the clarity gate

Review the asset at its real player size:
1. From a cold start — no context about the product
2. Muted — visuals and captions alone must carry task, change, and result
3. With sound — narration must match what is on screen at every moment
4. At the destination's smallest likely size — feed size on mobile

Read `references/review-rubric.md` for blocking gates.
Repair promise, causality, proof, trust, and readability **before** adding polish.

**Done when:** a new viewer can name the job, result, proof detail, and next step without extra explanation.

---

## Review path

For an existing script, storyboard, rough cut, or finished export:

1. Establish intended viewer, promise, destination, and CTA
2. Reconstruct the proof spine from what is actually present
3. Find the first frame where promise, action, result, or verification becomes uncertain
4. Give the earliest applicable verdict: **replan** / **re-record** / **recut** / **ready**
5. Cite timestamps or exact script fragments — recommend the smallest repair that restores the proof
6. Separate blocking repairs from optional polish

Do not reward production value for hiding a broken proof spine.

---

## Demo series path

For a product with several use cases, audiences, or independent capabilities:

1. Map every job the product performs and every viewer type it serves
2. Group into: one **overview video** (the product) + N **focused videos** (one job each)
3. For each video: assign its own viewer, proof object, and CTA
4. Keep the starting interaction recognizable across videos — returning viewers skip the introduction
5. Script the overview last — it is easier to summarize focused demos than to split a broad one

---

## Boundaries

- Planning does not authorize recording, uploading, publishing, or contacting anyone
- Keep private data, credentials, internal URLs, notifications, local paths, and unreleased information outside the frame
- Keep one source of truth for each claim — surface conflicts instead of smoothing them over
- Verify current platform export or upload specs from an official source only when exact settings matter
- Show generated output with enough input, result, and human or system control to judge it
