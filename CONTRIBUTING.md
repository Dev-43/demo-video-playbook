# Contributing

Thanks for wanting to improve this skill.

## What's worth contributing

- New proof patterns for product types not covered in `references/proof-patterns.md`
- New example files for different product categories
- New eval cases in `evals/cases.md` that catch real failure modes
- Fixes to existing files where guidance is ambiguous or wrong
- New context modes in `references/modes.md` (e.g. YouTube tutorial, Product Hunt launch)

## What doesn't belong here

- Generic video production advice not specific to software demos
- Platform-specific editing tutorials (that's what YouTube is for)
- Anything that adds polish decisions before the proof spine is complete

## How to contribute

1. Fork the repo
2. Make your changes in a branch
3. Add or update the relevant eval case in `evals/cases.md`
4. Open a pull request with a one-line description of what changed and why

## Eval case format

Every new behavior added to the skill should have a corresponding case in `evals/cases.md`:

```markdown
## Case N — [what behavior this tests]

**Input:** [the prompt or scenario]

**Expected behavior:**
- [what the skill should decide or produce]

**Fail signal:**
- [what wrong output looks like]
```

## Guiding principle

A contribution is good if it makes the skill catch a real mistake earlier,
or handle a real product type more honestly.
It is not good if it adds complexity without changing a decision the skill makes.
