---
name: third-party-and-payments
description: Assess third-party JS and payment gateway integration risk. Use when reviewing, auditing, or writing code touching this area — for a developer hardening a feature, an AppSec engineer assessing a codebase, or a bug bounty hunter looking for weaknesses in this area. Triggers on "Third Party and Payments" and related terms in the request or in the code being reviewed.
---

# Third Party and Payments

## Purpose

Assess third-party JS and payment gateway integration risk. Findings should be actionable: point to the specific file/line/pattern in the assessed codebase and cite the relevant cheat sheet section, not generic advice.

## Usage

1. Identify which resource(s) below match the code/feature under review (by filename or by scanning headings).
2. Read the relevant cheat sheet(s) in `resources/` before making recommendations — don't rely on memory of OWASP guidance.
3. Map cheat sheet checklist items against the actual code: confirm what's already handled, flag what's missing, and note anything partially implemented.
4. Report findings as: location → issue → cheat sheet reference → concrete fix. Skip items that don't apply to the stack in use.

## Resources

- `resources/Third_Party_Javascript_Management_Cheat_Sheet.md` — Third Party Javascript Management
- `resources/Third_Party_Payment_Gateway_Integration_Cheat_Sheet.md` — Third Party Payment Gateway Integration
