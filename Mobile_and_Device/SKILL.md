---
name: mobile-and-device
description: Assess mobile app, automotive, and drone/embedded device security. Use when reviewing, auditing, or writing code touching this area — for a developer hardening a feature, an AppSec engineer assessing a codebase, or a bug bounty hunter looking for weaknesses in this area. Triggers on "Mobile and Device" and related terms in the request or in the code being reviewed.
---

# Mobile and Device

## Purpose

Assess mobile app, automotive, and drone/embedded device security. Findings should be actionable: point to the specific file/line/pattern in the assessed codebase and cite the relevant cheat sheet section, not generic advice.

## Usage

1. Identify which resource(s) below match the code/feature under review (by filename or by scanning headings).
2. Read the relevant cheat sheet(s) in `resources/` before making recommendations — don't rely on memory of OWASP guidance.
3. Map cheat sheet checklist items against the actual code: confirm what's already handled, flag what's missing, and note anything partially implemented.
4. Report findings as: location → issue → cheat sheet reference → concrete fix. Skip items that don't apply to the stack in use.

## Resources

- `resources/Automotive_Security_Cheat_Sheet.md` — Automotive Security
- `resources/Drone_Security_Cheat_Sheet.md` — Drone Security
- `resources/Mobile_Application_Security_Cheat_Sheet.md` — Mobile Application Security
