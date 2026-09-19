# Example: Agent Verification Tool (CrossCheck-style)

This example covers agentic products where the interesting work is invisible —
background reasoning, web search, multi-step verification, citation generation.
Use this when the product is an AI agent and the value is in what it does, not just what it shows.

---

## The core challenge for agent demos

An agent does work that is mostly invisible.
The user submits something → a spinner → a result appears.
A viewer watching that has no reason to trust the result or believe the work happened.

The fix: use proof patterns from `references/proof-patterns.md` to make the invisible work visible.
For a verification agent: trace reveal + artifact reveal are the two most powerful patterns.

---

## Context detected

- **Product:** AI verification agent — checks factual claims against live sources
- **Platform:** X/Twitter launch + LinkedIn portfolio
- **Duration:** 45s (X) / 60s (LinkedIn)

---

## Demo thesis

```
For a developer or researcher who needs to verify factual claims quickly,
show a disputed claim being checked against live sources in under 30 seconds,
prove it with the visible citation trail and source list,
then ask them to try it at [URL] or star the repo.
```

---

## Truth map

| Claim | Status | Condition |
|---|---|---|
| Verifies claims against live web sources | ✅ Verified | Web search tool active in current build |
| Returns cited verdict with source list | ✅ Verified | Artifact visible in output |
| Handles "insufficient evidence" honestly | ✅ Verified | Tested with ambiguous claims |
| Shows agent reasoning trace | ✅ Verified | Dev mode exposes tool call log |
| Works on any claim type | ⚠️ Conditional | Best on factual, dateable claims — not opinions |
| Real-time streaming output | ⚠️ Conditional | Streaming enabled in hosted version only |
| Bulk verification (multiple claims) | ❌ Excluded | Not in current build |

---

## Proof spine

```
Starting state:  A disputed factual claim typed into the input field
Action:          User submits the claim
Response:        Agent runs — tool call log shows web search queries firing
Outcome:         Verdict returned: "Disputed — sources conflict on this date"
                 Citation list shows 3 sources, two supporting, one contradicting
Verification:    User clicks one citation — opens the actual source article
```

---

## Proof pattern used

**Trace reveal + Artifact reveal**

The trace (tool call log) proves the agent actually searched — not hallucinated.
The artifact (citation list with clickable links) proves the output is grounded.

Without both: the viewer sees a claim go in and a verdict come out and has no reason to trust it.
With both: the viewer can follow the reasoning and verify the sources themselves.

---

## Hook options

```
Hook A (recommended): "This claim took 4 hours to fact-check manually. Here's 28 seconds."
Hook B (contrast): "ChatGPT gave a confident wrong answer. Here's what a verified one looks like."
Hook C (technical — LinkedIn): "The hard part isn't the verdict. It's showing the work. Here's how I built that."
```

---

## Shot plan (45s X version)

| # | Time | Screen State | Narration | Technical Detail | Edit Note |
|---|---|---|---|---|---|
| 1 | 0–4s | Claim typed in input: "[specific disputed factual claim]" | "This claim took 4 hours to verify manually." | | Hold — viewer reads the claim |
| 2 | 4–7s | Submit button clicked | "Here's 28 seconds." | | |
| 3 | 7–18s | Tool call log scrolling — web search queries visible | "The agent searches live sources — not its training data." | Show 2–3 query lines clearly | Slow enough to read one query |
| 4 | 18–32s | Verdict appears: "Disputed" — citation list below | "Verdict: Disputed. Two sources confirm, one contradicts — here's which." | Highlight the conflicting source | Hold — viewer reads citations |
| 5 | 32–40s | User clicks one citation — source article opens | "Every claim is traceable. Click any citation." | | Let the article load visibly |
| 6 | 40–45s | Repo or product URL on screen | "Star the repo — [GitHub link]" | | |

---

## Full script (45s X version)

**[HOOK — 0–4s]**
"This claim took 4 hours to fact-check manually."

**[ACTION — 4–7s]**
"Here's 28 seconds."

**[TRACE — 7–18s]**
"The agent searches live sources — not its training data. You can see every query it runs."

**[RESULT — 18–40s]**
"Verdict: Disputed. Two sources confirm the claim, one directly contradicts it — and here's which.
Every citation is clickable. You don't have to take the agent's word for it."

**[CTA — 40–45s]**
"Star the repo — [GitHub link]"

---

## LinkedIn version differences (60s)

Use Mode D arc — lead with the technical challenge.

**Hook:** "The hard part of building a verification agent isn't the verdict — it's showing the work so someone can actually trust it. Here's how I solved that."

**Add after the demo:**
- 10s: Show the LangGraph or agent architecture briefly — which nodes handle search, citation, verdict
- "The full architecture is in the README — [link]"

**CTA:** "Open to [role] roles — repo link in comments"

---

## The recovery check (build trust proactively)

For a verification agent: show what happens when a claim can't be verified.

Submit an ambiguous claim → agent returns "Insufficient evidence — sources conflict on this detail."

This single moment builds more trust than three successful verifications.
It proves the agent doesn't hallucinate confident wrong answers.
Include it as a 10-second addendum or a follow-up post.

---

## Follow-up video ideas

| Video | Viewer | Proof pattern |
|---|---|---|
| How the agent handles contradicting sources | Technical audience | Trace reveal |
| Bulk verification mode (when built) | Power user | Artifact reveal |
| Architecture walkthrough — LangGraph nodes | Engineering hiring manager | Trace reveal + comparison |
| "What it gets wrong" — honest limitations | Trust-skeptical viewer | Recovery check |
