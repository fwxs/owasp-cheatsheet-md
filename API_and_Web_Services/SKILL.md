---
name: api-and-web-services
description: Assess REST, GraphQL, gRPC, WebSocket APIs and HTTP header/SSRF exposure in service-to-service and client-facing endpoints. Use when reviewing, auditing, or writing code touching this area — for a developer hardening a feature, an AppSec engineer assessing a codebase, or a bug bounty hunter looking for weaknesses in this area. Triggers on "API and Web Services" and related terms in the request or in the code being reviewed.
---

# API and Web Services

## Purpose

Assess REST, GraphQL, gRPC, WebSocket APIs and HTTP header/SSRF exposure in service-to-service and client-facing endpoints. Findings should be actionable: point to the specific file/line/pattern in the assessed codebase and cite the relevant cheat sheet section, not generic advice.

## Usage

1. Identify which resource(s) below match the code/feature under review (by filename or by scanning headings).
2. Read the relevant cheat sheet(s) in `resources/` before making recommendations — don't rely on memory of OWASP guidance.
3. Map cheat sheet checklist items against the actual code: confirm what's already handled, flag what's missing, and note anything partially implemented.
4. Report findings as: location → issue → cheat sheet reference → concrete fix. Skip items that don't apply to the stack in use.

## Resources

- `resources/GraphQL_Cheat_Sheet.md` — GraphQL
- `resources/gRPC_Security_Cheat_Sheet.md` — gRPC Security
- `resources/HTTP_Headers_Cheat_Sheet.md` — HTTP Headers
- `resources/REST_Assessment_Cheat_Sheet.md` — REST Assessment
- `resources/REST_Security_Cheat_Sheet.md` — REST Security
- `resources/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md` — Server Side Request Forgery Prevention
- `resources/Web_Service_Security_Cheat_Sheet.md` — Web Service Security
- `resources/WebSocket_Security_Cheat_Sheet.md` — WebSocket Security
