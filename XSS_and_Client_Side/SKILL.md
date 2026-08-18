---
name: xss-and-client-side
description: Assess client-side rendering, XSS, CSP, clickjacking, DOM clobbering, and browser-extension risk. Use when reviewing, auditing, or writing code touching this area — for a developer hardening a feature, an AppSec engineer assessing a codebase, or a bug bounty hunter looking for weaknesses in this area. Triggers on "XSS and Client Side" and related terms in the request or in the code being reviewed.
---

# XSS and Client Side

## Purpose

Assess client-side rendering, XSS, CSP, clickjacking, DOM clobbering, and browser-extension risk. Findings should be actionable: point to the specific file/line/pattern in the assessed codebase and cite the relevant cheat sheet section, not generic advice.

## Usage

1. Identify which resource(s) below match the code/feature under review (by filename or by scanning headings).
2. Read the relevant cheat sheet(s) in `resources/` before making recommendations — don't rely on memory of OWASP guidance.
3. Map cheat sheet checklist items against the actual code: confirm what's already handled, flag what's missing, and note anything partially implemented.
4. Report findings as: location → issue → cheat sheet reference → concrete fix. Skip items that don't apply to the stack in use.

## Resources

- `resources/AJAX_Security_Cheat_Sheet.md` — AJAX Security
- `resources/Browser_Extension_Vulnerabilities_Cheat_Sheet.md` — Browser Extension Vulnerabilities
- `resources/Clickjacking_Defense_Cheat_Sheet.md` — Clickjacking Defense
- `resources/Content_Security_Policy_Cheat_Sheet.md` — Content Security Policy
- `resources/Cross_Site_Scripting_Prevention_Cheat_Sheet.md` — Cross Site Scripting Prevention
- `resources/DOM_based_XSS_Prevention_Cheat_Sheet.md` — DOM based XSS Prevention
- `resources/DOM_Clobbering_Prevention_Cheat_Sheet.md` — DOM Clobbering Prevention
- `resources/HTML5_Security_Cheat_Sheet.md` — HTML5 Security
- `resources/Securing_Cascading_Style_Sheets_Cheat_Sheet.md` — Securing Cascading Style Sheets
- `resources/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md` — Unvalidated Redirects and Forwards
- `resources/XS_Leaks_Cheat_Sheet.md` — XS Leaks
- `resources/XSS_Filter_Evasion_Cheat_Sheet.md` — XSS Filter Evasion
