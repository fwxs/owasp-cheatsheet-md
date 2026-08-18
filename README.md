# OWASP Cheat Sheets — Claude Code Skills

A Markdown mirror of the [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/), organized as
[Claude Code Agent Skills](https://code.claude.com/docs/en/skills) across 21 security domains — authentication,
injection, cryptography, cloud/infra, AI/LLM, containers, and more.

## Usage

Drop this repo into `.claude/skills/` (project) or `~/.claude/skills/` (personal), or point Claude Code at it
directly. The root [`SKILL.md`](SKILL.md) is the entry point: it routes to the matching category skill based on
the code or question at hand, for either a security review/audit or proactive hardening suggestions.

Each category directory contains its own `SKILL.md` (workflow + resource list) and a `resources/` folder with the
underlying cheat sheets.

## Structure

```
SKILL.md                       ← root router: picks the right category
<Category>/
  SKILL.md                     ← category workflow + resource list
  resources/
    *.md                       ← individual OWASP cheat sheets
```

## Development

```bash
python3 scripts/validate_skill.py
```

Checks structural integrity: every `SKILL.md`'s frontmatter, that each category's Resources list
matches its `resources/` directory exactly, and that scripts compile. CI runs the same check on
every push and pull request — run it locally before opening a PR. See `CONTRIBUTING.md` for the
full contribution workflow.

## License and attribution

This repository is dual-licensed:

- **Mirrored OWASP content** — every file under `*/resources/**` — is licensed under
  [CC BY-SA 4.0](LICENSE).
- **Original code and methodology** — `SKILL.md` (root and per-category) and `scripts/**` — is
  licensed under [MIT](LICENSE-CODE).

Content is a mirror of the OWASP Cheat Sheet Series, © OWASP Cheat Sheets Series Team. See `NOTICE`
for what was changed from the original. Not affiliated with or endorsed by OWASP.
