# Project Chimera — Agent Skills

## What Is a Skill?

A **Skill** is a self-contained capability package that an autonomous agent
can invoke to perform a specific task.

Skills are:
- Declarative (clear input/output contracts)
- Composable
- Testable
- Replaceable

Skills do NOT:
- Contain agent identity
- Make governance decisions
- Bypass safety checks

---

## Skill Design Principles

1. Explicit JSON input/output
2. No hidden side effects
3. Failure must be detectable
4. Safe-by-default behavior

---

## Core Skills (Phase 1)

- skill_fetch_trends
- skill_generate_content
- skill_publish_content
