# docs/research-basis.md — Sources and Applied Decisions

This file documents why the key decisions in this skill exist and where they came from.

---

## Primary influence

**Demo Video Playbook by @Maaztwts**
https://github.com/somewherelostt/demo-video-playbook

The core insight that shaped this skill:

> "Building the product is sometimes easier than explaining it in a 60-second demo.
> When you record your own product, it's easy to forget how much of the explanation is happening
> in your head. You know which button matters, what changed after the click, and why the output
> is useful. Someone seeing the product for the first time has none of that context."

The proof spine concept, truth map structure, and review verdict system in this skill
are directly inspired by Maaz's architecture. His skill demonstrated that demo planning
deserves the same rigor as software architecture — and that most demo advice starts too late
(at recording) when the real decisions happen earlier (at framing and truth-checking).

This repo builds on his architecture with additions specific to:
- Agentic and LangGraph products (proof patterns for invisible work)
- Dynamic arc selection based on context
- Teaching-oriented guidance for developers new to demo-making
- Examples grounded in real projects (Nexus, CrossCheck)

---

## The one-thing rule

Source: Applied from @Maaztwts's playbook, reinforced by the Figma canvas-agent demo
and CodeRabbit's IDE demo as referenced examples.

> "I'd rather give the strongest feature a complete demonstration than show five features
> so quickly that none of them makes sense."

Decision: The skill enforces this by pushing back when scope exceeds one proof spine,
and by maintaining a cut list rather than letting features accumulate in a single demo.

---

## The proof spine

Source: Adapted from @Maaztwts's formulation:
```
starting state → meaningful action → product response → outcome → verification
```

Decision: The verification step is the most important addition beyond what most demo advice covers.
A demo that shows a result without a verifiable detail asks the viewer to trust without evidence.
For AI and agent products — where outputs can be hallucinated — this step is not optional.

---

## Truth map

Source: @Maaztwts's architecture.

Decision: Classifying claims as verified / conditional / excluded before scripting
prevents demos that accidentally mislead. This is especially important for:
- AI-generated output shown as typical when it's a best case
- Roadmap features shown as shipped
- Conditional behavior (works only with specific data) shown as universal

The truth map is built before the script — not as a post-hoc check.

---

## Proof patterns for invisible work

Source: Original to this skill — developed for agentic products (LangGraph, AI agents)
where the interesting work happens in the background and is not visible on screen.

Decision: Six patterns (artifact reveal, trace reveal, comparison proof, role test,
recovery check, integration handoff) cover the common cases where a standard demo
would show only a spinner and a result — which proves nothing.

---

## Dynamic arc selection

Source: Original to this skill — developed based on the different viewer expectations
across hackathon submissions, X/Twitter, demo day, and LinkedIn.

Decision: A fixed arc template produces demos that feel wrong for their context.
A hackathon demo that leads with the result (X/Twitter arc) feels like marketing to a judge
who needs to understand the problem first. An X post that opens with the problem setup
loses the feed before the product appears.

---

## Teach-as-you-guide design

Source: Original to this skill — developed for developers who build things well but
are new to explaining them on screen.

Decision: Every major decision in the output includes one line explaining why that choice works.
The goal is to build demo-making intuition alongside the immediate output,
so the next demo requires less guidance.

---

## Agent Skills specification

This repo follows the open Agent Skills specification at https://agentskills.io
Originally developed by Anthropic, now an open standard adopted across Claude, OpenAI Codex,
Gemini CLI, GitHub Copilot, Cursor, VS Code, and 20+ other platforms.

A skill is a folder containing a SKILL.md file with YAML frontmatter (name, description)
and instructions. Reference files, examples, and scripts are optional extensions.
The same skill file works across any skills-compatible agent without modification.
