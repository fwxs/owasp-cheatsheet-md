---
name: injection
description: Assess SQL, OS command, LDAP, NoSQL injection, unsafe deserialization, mass assignment, and prototype pollution. Use when reviewing, auditing, or writing code touching this area — for a developer hardening a feature, an AppSec engineer assessing a codebase, or a bug bounty hunter looking for weaknesses in this area. Triggers on "Injection" and related terms in the request or in the code being reviewed.
---

# Injection

## Purpose

Assess SQL, OS command, LDAP, NoSQL injection, unsafe deserialization, mass assignment, and prototype pollution. Findings should be actionable: point to the specific file/line/pattern in the assessed codebase and cite the relevant cheat sheet section, not generic advice.

## Usage

1. Identify which resource(s) below match the code/feature under review (by filename or by scanning headings).
2. Read the relevant cheat sheet(s) in `resources/` before making recommendations — don't rely on memory of OWASP guidance.
3. Map cheat sheet checklist items against the actual code: confirm what's already handled, flag what's missing, and note anything partially implemented.
4. Report findings as: location → issue → cheat sheet reference → concrete fix. Skip items that don't apply to the stack in use.

## Resources

- `resources/Deserialization_Cheat_Sheet.md` — Deserialization
- `resources/Injection_Prevention_Cheat_Sheet.md` — Injection Prevention
- `resources/LDAP_Injection_Prevention_Cheat_Sheet.md` — LDAP Injection Prevention
- `resources/Mass_Assignment_Cheat_Sheet.md` — Mass Assignment
- `resources/NoSQL_Security_Cheat_Sheet.md` — NoSQL Security
- `resources/OS_Command_Injection_Defense_Cheat_Sheet.md` — OS Command Injection Defense
- `resources/Prototype_Pollution_Prevention_Cheat_Sheet.md` — Prototype Pollution Prevention
- `resources/Query_Parameterization_Cheat_Sheet.md` — Query Parameterization
- `resources/SQL_Injection_Prevention_Cheat_Sheet.md` — SQL Injection Prevention
