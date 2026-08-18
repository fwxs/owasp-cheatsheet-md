---
name: ai-and-llm
description: Assess AI agent, LLM, RAG, and MCP integrations for prompt injection, agent-payment abuse, model-ops, and AI-assisted-coding risks. Use when reviewing, auditing, or writing code touching this area — for a developer hardening a feature, an AppSec engineer assessing a codebase, or a bug bounty hunter looking for weaknesses in this area. Triggers on "AI and LLM" and related terms in the request or in the code being reviewed.
---

# AI and LLM

## Purpose

Assess AI agent, LLM, RAG, and MCP integrations for prompt injection, agent-payment abuse, model-ops, and AI-assisted-coding risks. Findings should be actionable: point to the specific file/line/pattern in the assessed codebase and cite the relevant cheat sheet section, not generic advice.

## Usage

1. Identify which resource(s) below match the code/feature under review (by filename or by scanning headings).
2. Read the relevant cheat sheet(s) in `resources/` before making recommendations — don't rely on memory of OWASP guidance.
3. Map cheat sheet checklist items against the actual code: confirm what's already handled, flag what's missing, and note anything partially implemented.
4. Report findings as: location → issue → cheat sheet reference → concrete fix. Skip items that don't apply to the stack in use.

## Resources

- `resources/AI_Agent_Security_Cheat_Sheet.md` — AI Agent Security
- `resources/AML_Sanctions_AI_Agent_Payments_Cheat_Sheet.md` — AML Sanctions AI Agent Payments
- `resources/LLM_Prompt_Injection_Prevention_Cheat_Sheet.md` — LLM Prompt Injection Prevention
- `resources/MCP_Security_Cheat_Sheet.md` — MCP Security
- `resources/RAG_Security_Cheat_Sheet.md` — RAG Security
- `resources/Secure_AI_Model_Ops_Cheat_Sheet.md` — Secure AI Model Ops
- `resources/Secure_Coding_with_AI_Cheat_Sheet.md` — Secure Coding with AI
