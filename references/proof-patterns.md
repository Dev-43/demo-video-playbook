# proof-patterns.md — Evidence Patterns for Software Behavior

Most demo advice assumes the interesting work is visible on screen.
For AI agents, LangGraph workflows, background processing, and distributed systems — it often isn't.
This file covers how to make invisible work inspectable without faking it.

---

## The core problem

A viewer cannot trust what they cannot verify.
If your agent does something impressive but the screen only shows a loading spinner followed by a result —
the viewer has no reason to believe the work happened, happened correctly, or happened because of your product.

The fix is always the same: **find or create an artifact the viewer can inspect.**

---

## Pattern 1 — Artifact reveal

**Use when:** The agent produces a file, document, database entry, or structured output

Show:
1. The input that triggered the work
2. The artifact that was produced
3. One specific detail in the artifact that proves the agent understood the input

> Example for Nexus: Show a user's stated goal → the generated learning path → point out that the path
> skips topics the user already knows (proving it's personalized, not generic)

> Example for CrossCheck: Show a claim submitted → the verification report produced → point out the
> specific source citation that contradicts or confirms the claim

**What not to do:** Show only the final output without the input. The viewer cannot judge whether the
output is good if they don't know what the agent was working with.

---

## Pattern 2 — Trace reveal

**Use when:** The agent reasons through steps, calls tools, or makes decisions

Show the reasoning trace, tool call log, or agent step sequence — even briefly.
A LangGraph execution trace, a chain-of-thought log, or a tool call list gives the viewer something to read.

Steps:
1. Trigger the agent action on screen
2. Show the trace or log scrolling (briefly — 3–5 seconds)
3. Pause on one specific decision or tool call that proves the agent is doing real work
4. Show the outcome

> Example for LangGraph: Show the node execution sequence — which nodes fired, in what order,
> and what state was passed between them

> Example for an AI verification agent: Show the web search tool calls the agent made before
> reaching its conclusion — proves it actually looked things up, not just hallucinated

**What not to do:** Show a trace so fast the viewer cannot read a single line.
If you speed it up, slow down on the one line that matters most.

---

## Pattern 3 — Comparison proof

**Use when:** The value is "better than before" or "better than the alternative"

Show the before state and the after state **side by side or in direct sequence**.
The viewer should be able to point to exactly what changed and why that change matters.

> Example for Nexus: Split screen — left shows a generic course curriculum,
> right shows Nexus's personalized path for the same goal. Viewer immediately sees the difference.

> Example for CrossCheck: Show the same claim run through a manual Google search (slow, messy)
> vs. CrossCheck (structured, cited, fast). The comparison is the proof.

**What not to do:** Show only the after state. Without the before, the viewer cannot judge the improvement.

---

## Pattern 4 — Role test

**Use when:** The product behaves differently for different users, permissions, or contexts

Show the same action performed by two different roles or with two different inputs,
and let the viewer see that the product responds correctly to the difference.

> Example: Show an admin user and a standard user attempting the same action —
> prove that access control works by showing the contrast

**When to use:** When the interesting behavior is conditional — it only matters that the product
does the right thing in each case.

---

## Pattern 5 — Recovery check

**Use when:** Reliability or error handling is part of the value

Show what happens when something goes wrong:
- Bad input given → agent handles it gracefully
- Step fails → system recovers without crashing
- Unexpected data → output is flagged, not silently wrong

> Example for CrossCheck: Submit a claim that cannot be verified → show the agent returning
> "insufficient evidence" rather than hallucinating a confident wrong answer.
> This is more trust-building than showing only successful verifications.

**What not to do:** Only show best-case runs. Technical viewers will ask "what happens when it fails?"
Answer that question proactively.

---

## Pattern 6 — Integration handoff

**Use when:** Your product connects to other tools or systems

Show the data leaving your product and arriving somewhere else — or arriving in your product from somewhere else.
The handoff is the proof that the integration is real.

> Example: Show a task created in your product appearing in Notion, Linear, or Slack —
> in real time, not as a screenshot

**What not to do:** Show the button click that triggers the integration, then cut to a separate screenshot
of the destination. That splice cannot be verified. Show the handoff happening continuously.

---

## Handling AI-generated output

AI output is inherently probabilistic. Viewers know this. Pretending otherwise destroys trust.

**Always show:**
- The input that produced the output (so the viewer can judge whether the output makes sense)
- Any controls for reviewing or correcting the output (proves a human stays in the loop)

**When the output varies:**
- Use a consistent seed or fixed example for recording — state this if relevant
- Or show two runs with different inputs to demonstrate the range of behavior

**When the output is long:**
- Highlight the relevant part rather than shrinking everything to fit
- Give the viewer enough time to read the highlighted section

**Never:**
- Splice together the best parts of multiple runs without disclosing it
- Show output from a fine-tuned or special model when the product uses a different one
- Speed past the output so fast the viewer cannot evaluate it

---

## For async and background processes

If the interesting work happens over minutes or hours:

1. Show the trigger (what starts the process)
2. Show a progress indicator or log that proves work is happening
3. Jump cut to the result — **label the time skip explicitly** ("3 minutes later" on screen)
4. Show the result in full

Do not pretend async work is instant. The time skip is not a weakness — label it and move on.

---

## Choosing a pattern

| Situation | Pattern |
|---|---|
| Agent produces a file or structured output | Artifact reveal |
| Agent reasons through steps or calls tools | Trace reveal |
| Value is "better than before" | Comparison proof |
| Behavior depends on role or input | Role test |
| Reliability or error handling matters | Recovery check |
| Product connects to other tools | Integration handoff |
| Multiple patterns apply | Use the one that is most visually clear for this viewer and platform |
