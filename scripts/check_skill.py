#!/usr/bin/env python3
"""
check_skill.py — Local audit script for demo-video-playbook

Checks that all reference files are present, SKILL.md frontmatter is valid,
and eval cases have the required fields.

Run from the repo root:
    python scripts/check_skill.py
"""

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "references/modes.md",
    "references/proof-patterns.md",
    "references/workflow.md",
    "references/capture.md",
    "references/templates.md",
    "references/review-rubric.md",
    "examples/nexus-demo.md",
    "examples/agent-tool-demo.md",
    "examples/hackathon-submission.md",
    "evals/cases.md",
    "docs/research-basis.md",
]

SKILL_MD_REQUIRED_FRONTMATTER = ["name:", "description:"]

EVAL_REQUIRED_SECTIONS = ["**Input:**", "**Expected behavior:**", "**Fail signal:**"]


def check_required_files():
    print("Checking required files...")
    missing = []
    for f in REQUIRED_FILES:
        path = os.path.join(REPO_ROOT, f)
        if not os.path.exists(path):
            missing.append(f)
        else:
            print(f"  ✅ {f}")
    if missing:
        print(f"\n  ❌ Missing files:")
        for f in missing:
            print(f"     - {f}")
    return len(missing) == 0


def check_skill_frontmatter():
    print("\nChecking SKILL.md frontmatter...")
    skill_path = os.path.join(REPO_ROOT, "SKILL.md")
    if not os.path.exists(skill_path):
        print("  ❌ SKILL.md not found")
        return False

    with open(skill_path, "r") as f:
        content = f.read()

    if not content.startswith("---"):
        print("  ❌ SKILL.md does not start with YAML frontmatter (---)")
        return False

    missing = []
    for field in SKILL_MD_REQUIRED_FRONTMATTER:
        if field not in content:
            missing.append(field)
        else:
            print(f"  ✅ {field}")

    if missing:
        print(f"\n  ❌ Missing frontmatter fields: {', '.join(missing)}")
        return False

    # Check description length (should be descriptive enough for agent routing)
    desc_start = content.find("description:")
    desc_end = content.find("\n---", desc_start)
    desc = content[desc_start:desc_end] if desc_end > desc_start else ""
    if len(desc) < 100:
        print("  ⚠️  description: is short — agents use this to decide whether to activate the skill")
    else:
        print(f"  ✅ description length: {len(desc)} chars")

    return True


def check_eval_cases():
    print("\nChecking eval cases...")
    cases_path = os.path.join(REPO_ROOT, "evals/cases.md")
    if not os.path.exists(cases_path):
        print("  ❌ evals/cases.md not found")
        return False

    with open(cases_path, "r") as f:
        content = f.read()

    # Count cases
    case_count = content.count("## Case ")
    print(f"  Found {case_count} eval cases")

    if case_count < 3:
        print("  ⚠️  Fewer than 3 eval cases — consider adding more to cover edge cases")

    # Check each case has required sections
    issues = []
    cases = content.split("## Case ")
    for i, case in enumerate(cases[1:], 1):
        for section in EVAL_REQUIRED_SECTIONS:
            if section not in case:
                issues.append(f"Case {i} missing: {section}")

    if issues:
        print("  ❌ Issues found:")
        for issue in issues:
            print(f"     - {issue}")
        return False
    else:
        print("  ✅ All cases have required sections")
        return True


def check_reference_files_not_empty():
    print("\nChecking reference files are not empty...")
    ref_dir = os.path.join(REPO_ROOT, "references")
    all_ok = True
    for f in os.listdir(ref_dir):
        if f.endswith(".md"):
            path = os.path.join(ref_dir, f)
            size = os.path.getsize(path)
            if size < 200:
                print(f"  ⚠️  references/{f} looks too short ({size} bytes) — may be a stub")
                all_ok = False
            else:
                print(f"  ✅ references/{f} ({size} bytes)")
    return all_ok


def main():
    print("=" * 50)
    print("demo-video-playbook skill audit")
    print("=" * 50)

    results = [
        check_required_files(),
        check_skill_frontmatter(),
        check_eval_cases(),
        check_reference_files_not_empty(),
    ]

    print("\n" + "=" * 50)
    if all(results):
        print("✅ All checks passed — skill is ready to use")
        sys.exit(0)
    else:
        print("❌ Some checks failed — see above for details")
        sys.exit(1)


if __name__ == "__main__":
    main()
