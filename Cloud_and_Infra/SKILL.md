---
name: cloud-and-infra
description: Assess cloud architecture, IaC, network segmentation, serverless, zero-trust, subdomain takeover, and attack-surface exposure. Use when reviewing, auditing, or writing code touching this area — for a developer hardening a feature, an AppSec engineer assessing a codebase, or a bug bounty hunter looking for weaknesses in this area. Triggers on "Cloud and Infra" and related terms in the request or in the code being reviewed.
---

# Cloud and Infra

## Purpose

Assess cloud architecture, IaC, network segmentation, serverless, zero-trust, subdomain takeover, and attack-surface exposure. Findings should be actionable: point to the specific file/line/pattern in the assessed codebase and cite the relevant cheat sheet section, not generic advice.

## Usage

1. Identify which resource(s) below match the code/feature under review (by filename or by scanning headings).
2. Read the relevant cheat sheet(s) in `resources/` before making recommendations — don't rely on memory of OWASP guidance.
3. Map cheat sheet checklist items against the actual code: confirm what's already handled, flag what's missing, and note anything partially implemented.
4. Report findings as: location → issue → cheat sheet reference → concrete fix. Skip items that don't apply to the stack in use.

## Resources

- `resources/Attack_Surface_Analysis_Cheat_Sheet.md` — Attack Surface Analysis
- `resources/Infrastructure_as_Code_Security_Cheat_Sheet.md` — Infrastructure as Code Security
- `resources/Network_Segmentation_Cheat_Sheet.md` — Network Segmentation
- `resources/Secure_Cloud_Architecture_Cheat_Sheet.md` — Secure Cloud Architecture
- `resources/Serverless_FaaS_Security_Cheat_Sheet.md` — Serverless FaaS Security
- `resources/Subdomain_Takeover_Prevention_Cheat_Sheet.md` — Subdomain Takeover Prevention
- `resources/Zero_Trust_Architecture_Cheat_Sheet.md` — Zero Trust Architecture
