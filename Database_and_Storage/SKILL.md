---
name: database-and-storage
description: Assess database access controls, multi-tenant data isolation, and secrets storage. Use when reviewing, auditing, or writing code touching this area — for a developer hardening a feature, an AppSec engineer assessing a codebase, or a bug bounty hunter looking for weaknesses in this area. Triggers on "Database and Storage" and related terms in the request or in the code being reviewed.
---

# Database and Storage

## Purpose

Assess database access controls, multi-tenant data isolation, and secrets storage. Findings should be actionable: point to the specific file/line/pattern in the assessed codebase and cite the relevant cheat sheet section, not generic advice.

## Usage

1. Identify which resource(s) below match the code/feature under review (by filename or by scanning headings).
2. Read the relevant cheat sheet(s) in `resources/` before making recommendations — don't rely on memory of OWASP guidance.
3. Map cheat sheet checklist items against the actual code: confirm what's already handled, flag what's missing, and note anything partially implemented.
4. Report findings as: location → issue → cheat sheet reference → concrete fix. Skip items that don't apply to the stack in use.

## Resources

- `resources/Database_Security_Cheat_Sheet.md` — Database Security
- `resources/Multi_Tenant_Security_Cheat_Sheet.md` — Multi Tenant Security
- `resources/Secrets_Management_Cheat_Sheet.md` — Secrets Management
