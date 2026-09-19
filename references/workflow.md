# workflow.md — Demo Selection, Hook, Arc, and Cut Decisions

This file covers the decisions that happen between framing and scripting:
choosing what to show, how to open, what story to tell, and what to cut.

---

## Choosing what to show

### The one-thing rule

Before opening any recorder, finish this sentence:

> "After watching this, someone should understand how to _____."

Be specific enough that you can show the answer on screen.

| Too vague | Specific enough |
|---|---|
| "Manage work better" | "Turn a Slack message into a tracked task without leaving the message" |
| "Learn faster" | "Get a personalized study path that skips what you already know" |
| "Verify information" | "Check a factual claim against live sources and get a cited verdict in 30 seconds" |

### When you want to show more than one thing

Push back. Choose the feature that:
1. Is most impressive to this specific viewer (not most impressive to you)
2. Has the clearest before/after visible on screen
3. Can be proven completely in the available time

The other features get their own videos. A demo series is better than one overcrowded demo.

### The cut list

Everything not on the proof spine goes on the cut list for future videos.
Write it down — it becomes the plan for the next video in the series.

---

## Arc selection

The arc is the story structure. It changes based on context.
Read `references/modes.md` for the full branch for each context.

### Dynamic arc rule

The arc is not fixed. It changes based on:
- Who the viewer is and what decision they're making
- Where the demo is going (X, demo day, LinkedIn, hackathon)
- Whether the result or the process is more impressive
- How much time is available

**Hackathon:** Problem → gap → solution → proof → judge outcome
**X/Twitter:** Result first → how it happened → CTA
**Demo day:** Pain → failed alternatives → your approach → full walkthrough → vision
**LinkedIn:** Technical challenge → decision → proof with depth → what's next

When in doubt: lead with the problem if the solution needs context,
lead with the result if the result is immediately impressive.

---

## Hook writing

The hook must tell the viewer exactly what they are about to see.
The next on-screen action must immediately begin delivering on the hook's promise.

### What makes a hook strong

- Specific enough to create a concrete expectation
- Short enough to land before the viewer loses patience (under 10 words is ideal)
- Begins the proof — does not delay it

### Hook patterns by arc

**Problem-led (hackathon, demo day):**
> "[Pain state] — here's what we did about it."
> "Every [thing they struggle with]. We fixed that."

**Result-led (X/Twitter):**
> "[Result] in [time or clicks]. No [old frustrating step]."
> "Watch this [impressive output] happen from a single [input]."

**Challenge-led (LinkedIn):**
> "The hard part of [building X] isn't [obvious thing] — it's [real challenge]. Here's how I solved it."
> "[Technical problem stated plainly]. Here's the approach."

**Contrast-led (any):**
> "This is [manual painful process]. This is [product]. Same result."

### Writing three options

Always write three hooks before locking one.
Reason: the first hook is usually what you wish the product did, not what it actually does.
The third hook is usually more honest and more specific.

Lock the hook before writing the script. A script written before the hook is locked will need to be rewritten.

---

## Shot planning principles

### The sync rule

Write narration beside what is visible on screen at that exact moment.
If a sentence describes a result that is not yet on screen — move the sentence or change the shot.

This is the most common demo mistake: the narration runs ahead while the viewer is still looking at the
previous screen.

### Timing allocation

Give the **result more time than the action.**
Viewers need to read it, understand it, and trust it.

| Section | Guideline |
|---|---|
| Hook | 3–5 seconds |
| Problem setup | 10–15s (hackathon/demo day) or 0s (X/Twitter) |
| Action | As fast as the product allows |
| Result | As long as the viewer needs to read and understand it |
| Technical proof | 5–10s when shown |
| CTA | 3–5 seconds |

If the shot plan runs over the target duration: cut from the introduction, never from the result.

### Composition rules

Keep controls and their effects visible together when possible:
- Settings beside the page they change
- Input beside the output it produces
- Email beside the task it creates
- Filter beside the result it returns

This saves the viewer from remembering a "before" screenshot while trying to understand the "after."

### Cursor rules

- Move deliberately — stop once you reach the target
- If you spend a take searching through menus, reset that section
- Leave a brief pause before the action and after the result — gives editing room

---

## Cut decisions

### What to cut

- Repeated clicks and waiting time (label speed-ups)
- Feature introductions that don't help prove the one thing
- Anything the viewer doesn't need to understand the proof spine

### What never to cut

- The action that starts the feature
- The state that confirms completion
- Any frame the viewer needs to trust the result

### Disclosed cuts

If you speed up a process or jump time: say so on screen.
"3 minutes later" / "2x speed" / "Background processing complete"
A labeled cut is honest. An unlabeled cut looks like the product is faster than it is.

### The muted test

Watch the final cut with sound off.
If a viewer cannot follow the task, change, and result without audio — the visuals or captions are failing.
Fix the composition or add captions before adding music.

---

## Difficult selection problems

### When the product does too many things

Map every job the product performs. Score each on:
1. How visually clear is the proof?
2. How much does this viewer care about it?
3. Can it be shown completely in the available time?

Pick the highest scorer. The others are future videos.

### When the most impressive thing is invisible

Read `references/proof-patterns.md` — specifically trace reveal, artifact reveal, and comparison proof.
Every impressive thing that happens invisibly has an artifact, log, or comparison that makes it visible.

### When the product isn't finished

Only show what is verified in the current build.
If a key step requires manual workaround to look seamless — label it as conditional in the truth map.
A demo of an honest incomplete product builds more trust than a polished demo of something that doesn't work.

### When the result varies (AI output)

Use a fixed example with a consistent seed for recording.
State this in the accompanying post if relevant: "Results vary — this is one example."
Or show two runs with different inputs to demonstrate the range honestly.
