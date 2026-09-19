# evals/cases.md — Behavioral Test Cases

These cases test decisions and artifacts — not exact wording.
A correct output matches the intent described, not a specific script.

---

## Case 1 — Arc selection: hackathon vs X post

**Input:**
> "Help me demo my AI agent. It detects bugs in pull requests automatically. I'm submitting to a hackathon."

**Expected behavior:**
- Detects: hackathon context → selects Mode A arc
- Opens with the problem (developer time wasted on avoidable bugs)
- Does not open with the product name or tech stack
- Identifies the wow moment before scripting (the first bug caught automatically)
- Maps proof to judging criteria if hackathon track is mentioned

**Fail signal:**
- Generates a result-first arc (X/Twitter style) for a hackathon submission
- Opens with "Introducing our AI-powered bug detection tool"
- Produces a shot plan under 45 seconds for a hackathon demo

---

## Case 2 — Truth map blocks an unsupported claim

**Input:**
> "I want to show that the agent works in real time with zero latency."

**Expected behavior:**
- Asks: "Can zero latency be shown live in the current build?"
- If not verified: marks the claim as Conditional or Excluded
- Does not write narration claiming zero latency
- Offers: label it as "near real-time" if that is accurate, or show a timer on screen

**Fail signal:**
- Writes "zero latency" into the script without verification
- Accepts the claim without questioning it

---

## Case 3 — Invisible work requires proof pattern

**Input:**
> "My product is a LangGraph agent that researches topics in the background and emails a summary."

**Expected behavior:**
- Identifies: the interesting work is invisible (background processing, async)
- Recommends: trace reveal (show the graph execution) + artifact reveal (show the email output)
- Includes a labeled time-skip ("3 minutes later") for the background processing
- Does not suggest showing only the trigger and the final email

**Fail signal:**
- Produces a shot plan that shows only: user types topic → email appears in inbox
- No trace, no artifact detail, no time-skip label

---

## Case 4 — One thing rule enforced

**Input:**
> "I want to show the dashboard, the AI recommendations, the export feature, and the team sharing view."

**Expected behavior:**
- Pushes back: "Which one of these makes someone watching for the first time immediately understand the value?"
- Explains why showing all four produces a demo where none of them land
- Helps the user identify the strongest proof spine from the four options
- Puts the other three in a follow-up video plan (cut list)

**Fail signal:**
- Produces a shot plan that includes all four features in a single 60-second video
- Does not push back on scope

---

## Case 5 — Review path: returns correct verdict

**Input:**
> "Here's my rough cut [description]: opens with logo for 5 seconds, then shows the product for 30 seconds, but the output text is too small to read, and there's no CTA."

**Expected behavior:**
- Reconstructs proof spine from description
- Identifies blocking issues:
  - Gate 1 fail: hook is delayed by 5-second logo (recut)
  - Gate 5 fail: output text unreadable at feed size (recut)
  - Gate 6 fail: no CTA (recut)
- Verdict: **Recut** (footage is usable — edit issues only)
- Specific repairs: remove logo intro, zoom in on output, add CTA ending

**Fail signal:**
- Returns "Ready" verdict
- Returns "Replan" without checking if footage is salvageable

---

## Case 6 — X/Twitter arc enforced

**Input:**
> "I'm posting a demo to X. It's 90 seconds long. The first 20 seconds explains the problem."

**Expected behavior:**
- Flags: 90 seconds is too long for X (target is 30–45s)
- Flags: 20-second problem setup is too long for X (should be 0–3s or cut entirely)
- Recommends: result-first arc, cut the intro
- Explains why: X feeds are fast, the result must hook before the problem is established

**Fail signal:**
- Accepts 90 seconds without flagging
- Accepts 20-second problem setup for X without pushback

---

## Case 7 — Demo series planned correctly

**Input:**
> "My product has four main use cases: individual users, teams, enterprise, and API access."

**Expected behavior:**
- Recommends a series: one overview video + four focused videos
- Each focused video gets its own viewer, proof spine, and CTA
- Overview is planned last (summarizes focused demos)
- Starting interaction is kept recognizable across all videos

**Fail signal:**
- Tries to fit all four use cases into one video
- Plans the overview first

---

## Case 8 — Teach-as-you-guide for new demo makers

**Input:**
> "I've never made a demo video before. I just built my first project and want to show it on LinkedIn."

**Expected behavior:**
- Explains the arc choice and why it fits LinkedIn before generating the script
- Explains the proof spine concept in plain language before asking for the details
- Every major decision in the script includes one line explaining why that choice works
- Does not assume familiarity with demo concepts (hook, proof spine, CTA)

**Fail signal:**
- Generates output without explaining decisions
- Uses jargon without defining it
- Produces the same output as it would for an experienced demo maker
