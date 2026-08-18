# Contributing

Thanks for helping improve this skill. Please read the licensing section first — this repository is
dual-licensed, and which license applies depends on which files you touch.

## Licensing of contributions (read before you start)

This repo mixes two licenses (see `LICENSE`, `LICENSE-CODE`, `NOTICE`):

- **Mirrored OWASP content** — every file under `*/resources/**` — is under **CC BY-SA 4.0**. Any
  contribution to these files is accepted **only** under CC BY-SA 4.0. ShareAlike is not optional:
  your changes to this content stay under a CC BY-SA-compatible license, and if your change adapts
  the upstream OWASP Cheat Sheet Series you must keep attribution intact and record the change in
  `NOTICE`.
- **Original code and methodology** — the root `SKILL.md`, every category `SKILL.md`, and
  `scripts/**` — is under **MIT**. Contributions to these files are accepted under MIT.

By opening a pull request you agree that your contribution is licensed under whichever of the two
licenses governs the files you changed (inbound = outbound). Sign your commits with the Developer
Certificate of Origin to certify you have the right to submit the work:

```bash
git commit -s -m "your message"
```

The `-s` adds a `Signed-off-by` line. Do not paste content you do not have the right to relicense.

## Content boundaries

- **Keep it a mirror, not a rewrite.** `*/resources/**` content should track the published OWASP
  Cheat Sheet Series. Fix mirroring errors (broken formatting, missing sections) rather than
  rewriting guidance in your own words — that drifts from the source of truth and breaks
  attribution. For substantive content changes, consider contributing upstream to
  [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries) first.
- **Category `SKILL.md` files are original.** The purpose/usage/resource-list text in each category
  `SKILL.md` is written for this project, not copied from OWASP. Keep it concise and actionable.

## Repository conventions

- **SKILL.md frontmatter:** `name` stays lowercase/hyphen, ≤64 chars, with no reserved words
  (`claude`, `anthropic`). `description` stays third-person, non-empty, ≤1024 characters, with
  concrete trigger terms.
- **One level deep.** The root `SKILL.md` points directly at each category's `SKILL.md`; a category
  `SKILL.md` points directly at its own `resources/*.md` files. Category skills do not link to each
  other's resources.
- **Integrity is enforced.** Every file listed in a category `SKILL.md`'s Resources section must
  exist under that category's `resources/`, and every file physically present in `resources/` must
  be listed. If you add or remove a cheat sheet, update both.
- **Scripts stay stdlib-only.** No third-party dependencies — anything in `scripts/` must run with a
  stock Python 3 interpreter.

## Before you open a pull request

Run the validator locally — CI runs the same check and will block merge on failure:

```bash
python3 scripts/validate_skill.py
```

It verifies frontmatter on every `SKILL.md`, that each category's Resources list matches its
`resources/` directory exactly, and that all scripts compile.

## Pull request process

1. Fork the repository and create a branch (`git checkout -b fix/short-description`).
2. Make your change; run `validate_skill.py` until it passes.
3. Commit with DCO sign-off (`git commit -s`).
4. Open a PR describing **what** changed and **why**. If you touched `*/resources/**`, confirm the
   CC BY-SA / attribution requirements are met.
5. Keep PRs focused — one logical change per PR is easier to review than a sweeping edit.

## Reporting security issues

Do not use public issues or pull requests for security reports. Follow `SECURITY.md`.
