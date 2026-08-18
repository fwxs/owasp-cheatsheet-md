---
name: framework-and-language
description: Assess language- and framework-specific security config across Java, .NET, Node.js, PHP, Django, Rails, Laravel, Symfony, and C toolchains. Use when reviewing, auditing, or writing code touching this area — for a developer hardening a feature, an AppSec engineer assessing a codebase, or a bug bounty hunter looking for weaknesses in this area. Triggers on "Framework and Language" and related terms in the request or in the code being reviewed.
---

# Framework and Language

## Purpose

Assess language- and framework-specific security config across Java, .NET, Node.js, PHP, Django, Rails, Laravel, Symfony, and C toolchains. Findings should be actionable: point to the specific file/line/pattern in the assessed codebase and cite the relevant cheat sheet section, not generic advice.

## Usage

1. Identify which resource(s) below match the code/feature under review (by filename or by scanning headings).
2. Read the relevant cheat sheet(s) in `resources/` before making recommendations — don't rely on memory of OWASP guidance.
3. Map cheat sheet checklist items against the actual code: confirm what's already handled, flag what's missing, and note anything partially implemented.
4. Report findings as: location → issue → cheat sheet reference → concrete fix. Skip items that don't apply to the stack in use.

## Resources

- `resources/Bean_Validation_Cheat_Sheet.md` — Bean Validation
- `resources/C-Based_Toolchain_Hardening_Cheat_Sheet.md` — C-Based Toolchain Hardening
- `resources/Django_REST_Framework_Cheat_Sheet.md` — Django REST Framework
- `resources/Django_Security_Cheat_Sheet.md` — Django Security
- `resources/DotNet_Security_Cheat_Sheet.md` — DotNet Security
- `resources/JAAS_Cheat_Sheet.md` — JAAS
- `resources/Java_Security_Cheat_Sheet.md` — Java Security
- `resources/Laravel_Cheat_Sheet.md` — Laravel
- `resources/Nodejs_Security_Cheat_Sheet.md` — Nodejs Security
- `resources/PHP_Configuration_Cheat_Sheet.md` — PHP Configuration
- `resources/Ruby_on_Rails_Cheat_Sheet.md` — Ruby on Rails
- `resources/Symfony_Cheat_Sheet.md` — Symfony
