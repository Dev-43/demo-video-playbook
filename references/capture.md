# capture.md — Recording, Editing, and Delivery

Read this before recording or directing an edit.
Everything here is scoped to what changes between a clear demo and a confusing one.

---

## Environment setup

### Screen and window

Frame the application so the important text is readable in a small player.
Recording the entire desktop leaves the actual feature in a tiny corner of the video.

- Resize the window to show only what matters
- Increase interface zoom until key text is readable at feed size
- Keep enough surrounding UI to show where the action is happening
- Keep controls and their effects visible together when possible

Test: open the recording on your phone before you post it. If you can't read the key output, the viewer can't either.

### Demo account and data

- Use a demo account — keep real customer data, credentials, and internal URLs out of frame
- Prepare believable data: names, requests, deadlines that look real
- Example: "Please send the revised homepage copy to Maya by Friday" reads as real. "Test task 1" does not.
- Close unrelated browser tabs, notifications, and autocomplete suggestions

### Dry run

Run the complete proof spine once without recording.
Verify:
- The output is correct (right fields, right data, right result)
- The step sequence is what you planned
- The reset path works

Completing the action is not enough if the result is wrong.

### Clean starting state

Prepare the exact starting state you'll record from.
Write it down so later takes begin from the same point.
Leftover tasks, previous results, or dirty state from an earlier take will show in the recording.

---

## Recorders

Choose based on your OS and how much editing you want to do afterward.

| Tool | OS | Strengths | Notes |
|---|---|---|---|
| **Screen Studio** | Mac only | Auto-zoom, smooth cursor, social-friendly exports | Use auto-zooms as first pass, then remove any that pull attention away from the proof |
| **Cap** | Mac / Win / Linux | Open source, Studio mode, backgrounds, auto-zoom, cursor effects | Good for X posts where background polish matters |
| **OpenScreen** | Windows (free) | Zooms, cursor animation, captions, trimming, MP4/GIF export | Community fork is actively maintained; original repo archived |

A zoom should point to the decision or result that matters.
It should not fire simply because the recorder detected a click.

---

## Recording technique

### Cursor

- Move deliberately — stop once you reach the target control
- Do not scan the screen looking for the element while recording
- If you spend a take searching through menus, reset that section and try again

### Timing

- Pause briefly before the action — gives the viewer time to read the starting state
- Pause after the result appears — give the viewer time to read and understand it
- Do not cut away the moment the result appears

### Takes

- Record in sections when a full run is hard to keep clean
- Keep window size, zoom level, data, and cursor position consistent between sections
- Do not splice together steps the product cannot actually perform in sequence
- Read the script aloud once before recording — if it sounds unnatural, simplify it

### Audio

- Record narration in a quiet room
- If recording narration separately from screen capture, keep timing notes for sync
- A plain voice explaining clearly beats a polished voice explaining confusingly

---

## Editing

### Sequence before polish

Make a rough cut with just the screen recording and narration before adding music, transitions, or
animated captions. Verify the sequence makes sense first.
Otherwise you can spend an evening polishing a shot that should have been removed.

### What to cut

- Repeated clicks and unnecessary waiting
- Any section where you searched for a control
- Introduction length — cut here before cutting the proof

### What never to cut

- The action that starts the feature
- The state that confirms completion
- Time the viewer needs to read the result

### Zoom in editing

Zoom toward useful details:
- A closer view of the result field helps the viewer compare input to output
- Cropping away the input may make that comparison impossible

Do not zoom on every click — only zoom when the viewer needs to see a specific detail.

### Speed changes

If you speed up a process: label it on screen.
"2x speed" or "3 minutes later" makes the cut honest.
An unlabeled speed change implies the product is faster than it is.

### Captions

- Place captions away from controls and important output
- Keep captions short enough to read before the next shot cuts
- Lower music until narration is effortless to hear

---

## Platform-specific delivery

### X / Twitter
- Export as MP4, under 512MB, under 2 minutes 20 seconds (though 30–45s is the target)
- Captions on — most viewers watch muted
- First frame must be visually strong — it appears as the thumbnail in the feed
- Aspect ratio: 16:9 for desktop, 9:16 or 1:1 for mobile-first

### LinkedIn
- MP4, up to 10 minutes (though 45–90s is the target)
- Captions strongly recommended — LinkedIn autoplay is muted
- Native upload performs better than a YouTube link in the feed

### Demo day (live)
- Test the recording on the presentation display before the session
- Have a backup: recorded video in case live demo fails
- Know your fallback state — which point in the demo to jump to if something breaks

### Hackathon submission
- Check submission requirements for format, length, and file size
- Some platforms require a YouTube or Loom link — upload there first
- Include the repo link in the video or description

---

## Pre-publish checklist

- [ ] Watched on phone — sound OFF — task, change, and result are all clear
- [ ] Watched on phone — sound ON — narration matches screen at every moment
- [ ] Key text is readable at feed size
- [ ] No private data, credentials, or internal URLs in frame
- [ ] Captions do not cover important UI elements
- [ ] Speed-ups are labeled
- [ ] Shown to someone unfamiliar with the product — they can answer:
  - "What did the product do?"
  - "What would you do next?"
- [ ] CTA points to the correct page or action

---

## After publishing

Watch for questions in replies. A question is a specific gap the demo left open.

| Question type | What it means | Next step |
|---|---|---|
| "How does X work?" | The mechanism wasn't clear | Focused follow-up video on that step |
| "Does it work for Y?" | Scope wasn't clear | Clarify in a reply or follow-up |
| "When does Z happen?" | Trigger condition wasn't shown | Add a follow-up showing the condition |
| "Is this free / available?" | CTA didn't answer availability | Update the post or pin a reply |

Use real questions to decide what to explain next — not what you want to show next.
