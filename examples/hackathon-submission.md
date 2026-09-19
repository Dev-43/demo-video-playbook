# Example: Hackathon Submission Demo

This example covers the specific pressures and decisions of a judged submission demo.
Use this alongside `references/modes.md` (Mode A) when preparing for any hackathon.

---

## What makes hackathon demos different

Judges see 30–100+ projects in a session. They are tired. They are looking for reasons to move on.
Your demo has one job: make them lean forward at least once.

The three questions a judge answers while watching:
1. Do I understand what problem this solves?
2. Do I believe the solution actually works?
3. Is there a moment that surprised me?

If the answer to any of these is no — the demo failed, regardless of how good the product is.

---

## The wow moment rule

Every hackathon demo needs one moment that changes how the judge sees the problem.
Not a feature. A moment.

Find it by asking: "What would make someone who doesn't care about this product suddenly care?"

It is usually not the most technically complex thing you built.
It is usually the most visually clear demonstration that something previously impossible is now possible.

Identify the wow moment before scripting. Build the demo toward it. Give it more screen time than anything else.

---

## Arc for hackathon (Mode A)

```
Problem in the world (real, felt — not stated abstractly)
→ Gap: why existing solutions don't solve it
→ Your solution introduced (briefly — one sentence)
→ Live proof — end to end — including the wow moment
→ Judge-relevant outcome — mapped to rubric if known
```

---

## Timing allocation for 90 seconds

| Section | Time | Notes |
|---|---|---|
| Problem | 0–15s | Make it felt. Use a scenario, not a statistic. |
| Gap | 15–22s | One sentence on why existing tools fail |
| Solution intro | 22–28s | Name and one-line description — then immediately show it |
| Live proof | 28–75s | Full end-to-end. Wow moment at ~60s. |
| Outcome / rubric | 75–85s | Map to judging criteria explicitly if known |
| CTA | 85–90s | Repo, demo link, or "we're open to [track]" |

---

## Demo environment for judged submissions

### Safe environment rules
- Use a demo account — no real user data
- Test the demo on the exact network the hackathon provides (conference wifi is unreliable)
- Have a recorded backup — if the live demo fails, play the recording without apology
- Know the fallback state: which moment to jump to if something breaks mid-demo

### Data preparation
- Prepare 2–3 pre-loaded examples with different inputs
- The first example should produce the wow moment reliably
- The second is backup if the first fails
- Test all examples the night before — not the morning of

### Reset path
Write the exact steps to return to clean starting state.
Practice the reset until it takes under 30 seconds.

---

## Mapping to judging criteria

If you know the judging rubric, map your proof spine to it explicitly.

Common hackathon criteria and how to address them in the demo:

| Criterion | How to show it |
|---|---|
| Innovation | Show the thing that didn't exist before — make the before/after contrast explicit |
| Technical complexity | Brief trace reveal — 5 seconds of agent execution, architecture overlay, or terminal output |
| Real-world impact | Start with a scenario a real person would face — make the judge feel the problem |
| Polish / completeness | Show the CTA leading to a working product — not a prototype with broken links |
| Use of sponsor API | Name the API on screen when you use it — don't assume judges notice |

---

## Common hackathon demo mistakes

| Mistake | Why it fails | Fix |
|---|---|---|
| Opening with the tech stack | Judges don't care about the stack until they care about the problem | Open with the problem — mention the stack in passing during the demo |
| Showing too many features | Judges can't remember 5 features — they remember 1 moment | Choose one proof spine, put secondary features in the cut list |
| Rushing through the result | The result is the proof — rushing it destroys the trust you built | Give the result more time than the action |
| "As you can see..." with nothing visible | You're narrating a screen the viewer can already see | Narrate meaning, not what's visible |
| Demo fails, no backup | Recovers awkwardly, loses judge confidence | Prepare recorded backup — play it calmly if needed |
| CTA to a broken link | Judge tries to click, gets a 404 | Test every link the night before |

---

## The question judges ask after

Watch for the questions judges ask after your presentation.
A specific question is a sign they engaged but missed something — answer it and note it for the next demo.

A judge asking "what happens when X?" means the demo didn't show X.
That's the next video in your series.
