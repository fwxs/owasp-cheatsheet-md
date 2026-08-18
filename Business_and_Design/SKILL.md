---
name: business-and-design
description: Assess design-level and process risks: abuse cases, threat models, secure-by-design gaps, legacy code, review process, virtual patching. Use when reviewing, auditing, or writing code touching this area — for a developer hardening a feature, an AppSec engineer assessing a codebase, or a bug bounty hunter looking for weaknesses in this area. Triggers on "Business and Design" and related terms in the request or in the code being reviewed.
---

# Business and Design

## Purpose

Assess design-level and process risks: abuse cases, threat models, secure-by-design gaps, legacy code, review process, virtual patching. Findings should be actionable: point to the specific file/line/pattern in the assessed codebase and cite the relevant cheat sheet section, not generic advice.

## Usage

1. Identify which resource(s) below match the code/feature under review (by filename or by scanning headings).
2. Read the relevant cheat sheet(s) in `resources/` before making recommendations — don't rely on memory of OWASP guidance.
3. Map cheat sheet checklist items against the actual code: confirm what's already handled, flag what's missing, and note anything partially implemented.
4. Report findings as: location → issue → cheat sheet reference → concrete fix. Skip items that don't apply to the stack in use.

## Resources

- `resources/Abuse_Case_Cheat_Sheet.md` — Abuse Case
- `resources/Business_Logic_Security_Cheat_Sheet.md` — Business Logic Security
- `resources/Legacy_Application_Management_Cheat_Sheet.md` — Legacy Application Management
- `resources/Secure_Code_Review_Cheat_Sheet.md` — Secure Code Review
- `resources/Secure_Product_Design_Cheat_Sheet.md` — Secure Product Design
- `resources/Threat_Modeling_Cheat_Sheet.md` — Threat Modeling
- `resources/Virtual_Patching_Cheat_Sheet.md` — Virtual Patching
