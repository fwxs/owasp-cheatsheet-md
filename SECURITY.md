# Security Policy

## What this project is

`owasp-cheatsheet-md` is a **local, offline Claude Agent Skill**: a Markdown mirror of the OWASP
Cheat Sheet Series, organized into 21 category skills, plus a stdlib-only Python helper script
(`scripts/validate_skill.py`). It is not a hosted service and does not process untrusted input at
runtime.

Trust properties worth knowing:

- **No network calls.** The validator script uses only the Python standard library and touches only
  the files in this repository. It makes no outbound connections and sends no telemetry.
- **No credentials or secrets** are stored, requested, or transmitted by this repository.
- **Local execution only.** Everything runs on your machine (or your Claude runtime); nothing here
  phones home.

If any of the above ever stops being true in a change, that change should be treated as a security-
relevant modification and called out explicitly in review.

## Supported versions

Security fixes are provided for the latest tagged release and the `main` branch. Older tags are not
patched — upgrade to the latest release.

| Version | Supported |
|---------|-----------|
| latest release / `main` | Yes |
| older tags | No |

## Reporting a vulnerability

Please report suspected vulnerabilities **privately**, not in a public issue.

1. **Preferred:** use GitHub's private vulnerability reporting — the **Security** tab →
   **Report a vulnerability**. This opens a private advisory visible only to the maintainers.
2. **Alternative:** email the maintainer at `mrpacmanator@gmail.com`.

In your report, include: a description of the issue, steps to reproduce, the affected file(s) or
script(s), the potential impact, and a suggested fix if you have one.

**Response targets:** acknowledgement within a few business days; for confirmed issues, a fix or
mitigation plan communicated as soon as practical. Please allow a reasonable disclosure window before
publishing details, and act in good faith — no data destruction, privacy violations, or service
disruption while investigating.

## What is in scope

- The helper script in `scripts/` (input handling, path handling, unsafe operations).
- The CI workflow and any repository automation.
- Packaging or install instructions that could lead a user to run something unsafe.

## What is out of scope

- **The defensive-security content itself.** This repository documents hardening guidance from the
  OWASP Cheat Sheet Series. A gap in that guidance is a documentation issue, not a vulnerability in
  this repo — and should ideally be raised with
  [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries) if it also affects the
  upstream source.
- Issues in the upstream OWASP Cheat Sheet Series content — report those to the
  [OWASP CheatSheetSeries project](https://github.com/OWASP/CheatSheetSeries).
