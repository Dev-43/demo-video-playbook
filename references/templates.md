# templates.md — Output Contracts

These are the exact shapes for the three output files.
Every field must be filled with product-specific content — no placeholders left in the final output.

---

## File 1: DEMO_SCRIPT.md

```markdown
# DEMO_SCRIPT.md — [Product Name]

> Context: [hackathon / X post / demo day / LinkedIn]
> Arc: [chosen arc — one line explaining why this arc fits this context]
> Duration: [Xs] | Platform: [platform] | Hook: [chosen hook text]

---

## One Thing This Video Proves

"After watching this, someone should understand how to _____."

---

## Viewer

[Who they are — specific, not generic]
[What frustration this video resolves for them]
[What decision they are making after watching]

---

## Proof Spine

| Element | Description |
|---|---|
| Starting state | [Exact screen state before anything happens] |
| Action | [The single thing the user or system does] |
| Response | [What the product does — what visibly changes] |
| Outcome | [The result — what is now true that wasn't before] |
| Verification | [How the viewer confirms this is real] |

---

## Truth Map

| Claim | Status | Source / Condition |
|---|---|---|
| [feature or behavior] | ✅ Verified | [working in current build] |
| [feature or behavior] | ⚠️ Conditional | [only true when X] |
| [feature or behavior] | ❌ Excluded | [reason] |

---

## What's In / What's Cut

| Element | Decision | Reason |
|---|---|---|
| [feature / screen] | ✅ In | [why it serves the proof spine] |
| [feature / screen] | ❌ Cut | [why it distracts from the one thing] |

---

## Full Script

**[HOOK — 0 to Xs]**
"[Exact opening words — specific, begins the proof immediately]"

**[PROBLEM SETUP — Xs to Xs]** *(skip for X/Twitter arc)*
"[What life looks like without this — make it felt]"

**[ACTION — Xs to Xs]**
"[Narration during the action — name the controls as they appear on screen]"

**[RESULT — Xs to Xs]**
"[Point out specific fields or outputs — name what changed, what carried across]"

**[TECHNICAL PROOF — Xs to Xs]** *(when relevant)*
"[Show terminal / agent log / architecture — narrate what it means, not what it says]"

**[CONTROL — Xs to Xs]** *(for AI outputs — builds trust)*
"[Show that the output can be reviewed and edited]"

**[CTA — Xs to Xs]**
"[Exact one action — matches the screen that is visible at this moment]"

---

## Alternative Hooks

- Hook B: "[unused hook — save for next video or variant]"
- Hook C: "[unused hook]"

---

## Follow-up Video Ideas

Based on what this video deliberately left out:
- [Feature / use case] — viewer for this would be [who]
- [Feature / use case] — viewer for this would be [who]
```

---

## File 2: SHOT_PLAN.md

```markdown
# SHOT_PLAN.md — [Product Name]

> Use this beside your recorder. Every shot is mapped to the script line it delivers.

---

## Pre-Record Setup

- [ ] [Specific tab or window setup]
- [ ] Demo account prepared with: [specific data — names, requests, deadlines]
- [ ] Zoom level set to: [X%] — key text "[specific text]" is readable at feed size
- [ ] Notifications off
- [ ] Unrelated tabs closed
- [ ] Dry run complete — [specific output field] verified correct
- [ ] Starting state: [exact description of screen state before first take]

---

## Shot-by-Shot

| # | Time | Screen State | Narration | Technical Detail | Edit Note |
|---|---|---|---|---|---|
| 1 | 0–Xs | [exact UI state] | "[words]" | [agent step / log / code visible?] | [zoom? pause? caption?] |
| 2 | Xs–Xs | [state after action] | "[words]" | | |
| 3 | Xs–Xs | [result on screen] | "[words]" | [specific field to highlight] | [hold Xs — let viewer read] |
| 4 | Xs–Xs | [CTA screen] | "[words]" | | |

---

## Composition Rules for This Demo

- Keep [specific element] and [specific element] visible together — viewer needs to compare them
- Frame at [X% zoom] so [specific text] is readable at feed size
- Do not crop [specific UI area] — it provides context for [specific action]
- Zoom in on [specific element] after [specific action] — not before

---

## Reset Instructions

If a take goes wrong, return to clean starting state:
1. [Step 1]
2. [Step 2]
3. [Step 3 — verify: [specific thing to check before next take]]
```

---

## File 3: RECORDING_CHECKLIST.md

```markdown
# RECORDING_CHECKLIST.md — [Product Name]

---

## Before Record

- [ ] Demo account set up with: [specific data]
- [ ] Dry run complete — [specific output] verified correct
- [ ] Starting state clean: [exact reset state]
- [ ] Window resized / zoomed to: [specific setting]
- [ ] Notifications off
- [ ] Unrelated tabs closed
- [ ] Script read aloud — sounds natural, not robotic
- [ ] No private data, credentials, or internal URLs visible in frame

---

## During Recording

- [ ] Hook line delivered before any action begins
- [ ] Paused [Xs] before [specific action] — viewer reads the starting state
- [ ] Paused [Xs] after [specific result] — viewer reads [specific field]
- [ ] Cursor stopped at [specific element] — not scanning
- [ ] [Specific step] shown in full — not rushed

---

## Editing (rough cut first — always before polish)

- [ ] Rough cut done with screen + narration only — no music or effects yet
- [ ] Sequence makes sense without any polish
- [ ] Dead time removed: repeated clicks, unnecessary waiting
- [ ] Result stays on screen long enough to read [specific field]
- [ ] Zoom points to [specific element] — not every click
- [ ] [Specific speed-up section] labeled on screen: "[label text]"
- [ ] Captions placed away from [specific UI area]
- [ ] Music lower than narration — narration is effortless to hear

---

## Pre-Publish Test

- [ ] Watched on phone — sound OFF — task, change, and result are clear
- [ ] Watched on phone — sound ON — narration matches screen throughout
- [ ] [Specific key text] readable at feed size
- [ ] No private data, credentials, or internal URLs in frame
- [ ] Shown to someone unfamiliar — they answered:
  - "What did the product do?" → [expected answer]
  - "What would you do next?" → [expected answer]
- [ ] CTA links to the correct page or action

---

## After Publishing

Watch replies for gaps. First follow-up topic based on what this video left out:
- [Most likely question viewers will have]
- [Feature this video deliberately didn't show]
```
