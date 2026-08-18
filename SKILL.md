---
name: owasp-cheat-sheets
description: Entry point for OWASP Cheat Sheets security guidance across 21 domains (auth, injection, crypto, cloud, AI/LLM, containers, and more). Use when reviewing or auditing code for vulnerabilities, when suggesting hardening improvements to an existing codebase, when writing new code that touches a security-sensitive area, or when unsure which specific security category applies. Routes to the matching category skill for detailed cheat sheets and workflow.
---

# OWASP Cheat Sheets

## Purpose

Single entry point into 21 domain-specific security skills, each backed by official OWASP cheat sheets. Two use cases:

- **Security review / audit**: find and report vulnerabilities in existing code.
- **Improvement suggestions**: proactively harden a codebase — recommend fixes, safer patterns, or missing controls even when nothing is broken yet, for developers and AppSec engineers alike.

Both use cases route through the same category skills; only the framing of the findings differs (see Usage).

## Usage

1. Identify which categor(ies) below match the code, feature, or question at hand — by keyword, filename, or the tech stack involved. Multiple categories may apply (e.g., a login endpoint touches both Authentication and API_and_Web_Services).
2. Invoke the matching category's own `SKILL.md` — it lists the exact cheat sheets to read and the checklist workflow to follow. Do not skip straight to a cheat sheet in `resources/` without reading the category `SKILL.md` first; it scopes which sheets are relevant and how to report findings.
3. Frame the output for the actual goal:
   - **Reviewing/auditing**: report as location → issue → cheat sheet reference → concrete fix.
   - **Suggesting improvements**: report as location → current state → cheat sheet reference → recommended hardening, even absent an active exploit — call out gaps against the checklist, not just confirmed bugs.
4. If no category matches cleanly, or the concern spans architecture/process rather than code (e.g. threat modeling, secure-by-design review), start with Business_and_Design.

## Categories

| Category | Covers |
|---|---|
| [AI_and_LLM](AI_and_LLM/SKILL.md) | AI agent, LLM, RAG, and MCP integrations — prompt injection, agent-payment abuse, model-ops, AI-assisted-coding risks |
| [API_and_Web_Services](API_and_Web_Services/SKILL.md) | REST, GraphQL, gRPC, WebSocket APIs, HTTP header/SSRF exposure |
| [Authentication](Authentication/SKILL.md) | Login, credential, MFA, password-reset, token/SAML/OAuth2 flows |
| [Authorization](Authorization/SKILL.md) | Access-control logic, role/permission checks, IDOR, authz regression testing |
| [Business_and_Design](Business_and_Design/SKILL.md) | Abuse cases, threat models, secure-by-design gaps, legacy code, review process, virtual patching |
| [CI_CD_and_Supply_Chain](CI_CD_and_Supply_Chain/SKILL.md) | Build pipelines, GitHub Actions, dependency/SBOM management, npm supply-chain exposure |
| [CSRF_and_Session](CSRF_and_Session/SKILL.md) | Session handling, cookies, CSRF defenses, transport security headers |
| [Cloud_and_Infra](Cloud_and_Infra/SKILL.md) | Cloud architecture, IaC, network segmentation, serverless, zero-trust, subdomain takeover, attack surface |
| [Container_and_Orchestration](Container_and_Orchestration/SKILL.md) | Docker and Kubernetes configs, container runtime hardening |
| [Cryptography_and_Keys](Cryptography_and_Keys/SKILL.md) | Cryptographic storage, key management, certificate pinning, TLS configuration |
| [Data_and_Input_Validation](Data_and_Input_Validation/SKILL.md) | Input validation, file upload handling, email validation, error-handling info leakage |
| [Database_and_Storage](Database_and_Storage/SKILL.md) | Database access controls, multi-tenant data isolation, secrets storage |
| [DoS_and_Bot](DoS_and_Bot/SKILL.md) | Denial-of-service resilience, automated/bot abuse |
| [Framework_and_Language](Framework_and_Language/SKILL.md) | Language/framework security config — Java, .NET, Node.js, PHP, Django, Rails, Laravel, Symfony, C toolchains |
| [Injection](Injection/SKILL.md) | SQL, OS command, LDAP, NoSQL injection, unsafe deserialization, mass assignment, prototype pollution |
| [Logging_and_Monitoring](Logging_and_Monitoring/SKILL.md) | Logging completeness, tamper-resistance, safe log-field vocabulary |
| [Microservices](Microservices/SKILL.md) | Microservices security architecture, inter-service trust boundaries |
| [Mobile_and_Device](Mobile_and_Device/SKILL.md) | Mobile app, automotive, and drone/embedded device security |
| [Privacy_and_Disclosure](Privacy_and_Disclosure/SKILL.md) | User privacy handling, vulnerability disclosure process, security terminology |
| [Third_Party_and_Payments](Third_Party_and_Payments/SKILL.md) | Third-party JS and payment gateway integration risk |
| [XML_and_Data_Formats](XML_and_Data_Formats/SKILL.md) | XML parsing, XXE, general XML security misconfigurations |
| [XSS_and_Client_Side](XSS_and_Client_Side/SKILL.md) | Client-side rendering, XSS, CSP, clickjacking, DOM clobbering, browser-extension risk |
