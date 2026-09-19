# demo-video-playbook

A coding agent skill for planning, scripting, staging, and reviewing software demo videos.

Built for developers who ship technical products but aren't demo veterans.
Teaches as it guides — every decision comes with a reason, not just an instruction.

> Core insight: building the product is often easier than explaining it clearly in 60 seconds.
> A demo is a claim made visible. Every shot must earn its place by proving something real.

---

## What this skill does

Drop it into any project folder. Your coding agent reads the codebase and helps you:

- **Plan** — choose what to show, who to show it to, and what story to tell
- **Script** — write a shot-by-shot plan with narration synced to what's on screen
- **Stage** — prepare a repeatable, honest recording environment
- **Review** — diagnose an existing rough cut and get the earliest applicable verdict
- **Series** — divide a multi-capability product into a focused demo series

---

## Supported contexts

| Context | What it optimizes for |
|---|---|
| Hackathon submission | Judging rubric, wow moment, end-to-end proof |
| X / Twitter launch post | Hook in 3s, silent-watchable, 30–45s, punchy CTA |
| Demo day presentation | Full story arc, complete walkthrough, investor-ready |
| LinkedIn / portfolio | Technical credibility, depth, one impressive detail |

---

## Supported product types

- Web apps and SaaS products
- AI agents and LangGraph workflows
- CLI and API tools
- Background processing and async systems
- Any product where the interesting work is invisible

---

## Install

### Option 1 — Drop into your project

Copy the repo into your project folder:

```bash
git clone https://github.com/Dev-43/demo-video-playbook
```

Then in your coding agent:

```
Use the demo-video-playbook skill to plan a demo for this project
```

or trigger directly:

```
/demo-video
```

### Option 2 — Global skills folder

Place the repo in your global skills directory so it's available in every project.

For Claude Code:
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Dev-43/demo-video-playbook ~/.claude/skills/demo-video-playbook
```

---

## How to trigger it

```
/demo-video
```
Starts the full pipeline from scratch — product grilling, arc selection, script, shot plan, checklist.

```
/demo-video [brief product description]
```
Skips the initial prompt — goes straight to the context and arc questions.

```
Review my demo: [description of existing script or rough cut]
```
Routes to the review path — returns a verdict (ready / recut / re-record / replan) with specific repairs.

```
Plan a demo series for [product]
```
Routes to the series path — maps use cases to viewers and divides into focused videos.

---

## What you get

Three files ready to use before you hit record:

| File | Contents |
|---|---|
| `DEMO_SCRIPT.md` | Demo thesis, truth map, proof spine, include/cut table, full narration script |
| `SHOT_PLAN.md` | Shot-by-shot table, pre-record setup, composition rules, reset instructions |
| `RECORDING_CHECKLIST.md` | Before record, during recording, editing, pre-publish test, post-publish |

---

## What you need to provide

The skill infers what it can from your codebase. It asks only for choices that would materially change the demo.

**Minimum input:** tell it what you built — even a rough description works.

**What makes output better:**
- Who the viewer is and what decision they're making after watching
- Where the demo is being posted
- The target duration
- What the "before" state looks like — life without your product

**What the skill handles on its own:**
- Which feature to show vs. leave out
- How to write a hook that works for the context
- How to sync narration with what's on screen
- Shot timing by platform
- Recording environment setup
- Editing order (rough cut before polish — always)
- Pre-publish test questions

---

## Repo structure

```
demo-video-playbook/
├── SKILL.md                        ← main router — start here
├── references/
│   ├── modes.md                    ← context-specific arcs (hackathon, X, demo day, LinkedIn)
│   ├── proof-patterns.md           ← evidence patterns for invisible AI/agent work
│   ├── workflow.md                 ← arc selection, hook writing, cut decisions
│   ├── capture.md                  ← recording, editing, delivery
│   ├── templates.md                ← output contracts (DEMO_SCRIPT, SHOT_PLAN, CHECKLIST)
│   └── review-rubric.md            ← blocking gates and diagnosis for existing cuts
├── examples/
│   ├── nexus-demo.md               ← adaptive skill platform (LangGraph + FastAPI)
│   ├── agent-tool-demo.md          ← AI verification agent (CrossCheck-style)
│   └── hackathon-submission.md     ← judged submission walkthrough
├── evals/
│   └── cases.md                    ← behavioral test cases
├── docs/
│   └── research-basis.md           ← sources and applied decisions
├── scripts/
│   └── check_skill.py              ← local audit script
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## Inspired by

**Demo Video Playbook by [@Maaztwts](https://github.com/somewherelostt/demo-video-playbook)**
The proof spine concept, truth map structure, and review verdict system are directly inspired by Maaz's architecture.

This repo extends his work with:
- Proof patterns for invisible AI/agent work
- Dynamic arc selection by context
- Teaching-oriented guidance for developers new to demo-making
- Examples grounded in real agentic projects

See `docs/research-basis.md` for the full attribution and decision log.

---

## License

MIT — use it, fork it, improve it.

If you find something missing or wrong, open an issue or contribute.
See `CONTRIBUTING.md`.
