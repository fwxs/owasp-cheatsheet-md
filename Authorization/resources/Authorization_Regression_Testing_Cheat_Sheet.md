## Table of Contents
- Introduction
- Authorization Test Matrix Design
  - Define the Access Policy Model
  - Machine-Readable Rules
- Regression Testing Patterns
  - Horizontal Escalation (IDOR) Validation
  - Vertical Escalation Validation
  - Tenant Isolation Breakage
- Contract-Driven Authorization Validation
- Automated Testing Framework Integration
- CI/CD Gating and SDLC Integration
- References
  - OWASP Resources
  - Related OWASP Cheat Sheets
  - Standards and Specifications
  - Tools
# Authorization Regression Testing Cheat Sheet
## Introduction
Authorization implementation is rarely static. As applications evolve, new API
endpoints are added, data layers are refactored, and microservices are
decoupled. While initial security testing might validate access controls at
launch, the "Day 2" problem emerges quickly: How do engineering teams ensure
that new features or structural changes do not break existing authorization
logic?
Broken_Access_Control_(BAC) was ranked the number-one risk in the OWASP Top Ten
2021, and Insecure_Direct_Object_Reference_(IDOR) is one of its most frequently
exploited sub-categories. This cheat sheet provides actionable, architectural
guidance on implementing automated authorization regression testing within the
Software Development Life Cycle (SDLC). By shifting from manual, point-in-time
penetration testing to continuous, developer-centric regression suites,
engineering teams can catch BAC, IDOR, and tenant isolation failures before
they reach production.
Key topics covered in this cheat sheet include:
    * Designing an automated authorization test matrix.
    * Common regression testing patterns for horizontal, vertical, and tenant
      isolation tests.
    * Validating authorization schemas using API contracts.
    * Integrating authorization tests into CI/CD pipelines.
## Authorization Test Matrix Design
     Relationship to the Authorization Testing Automation Cheat Sheet
     The Authorization_Testing_Automation_Cheat_Sheet provides a
     foundational, XML-driven approach to building and executing an
     authorization matrix against REST services — including a full Java/
     JUnit integration test harness. This cheat sheet extends that
     foundation by focusing on the continuous regression dimension: how to
     design matrices in formats (YAML/JSON) suited to modern test runners,
     which specific failure patterns to prioritize in a regression suite
     (IDOR, vertical escalation, tenant boundary), how to couple tests to
     OpenAPI contracts, and how to gate pull requests automatically in CI/
     CD. If you are new to authorization test matrices, start with the
     Authorization_Testing_Automation_Cheat_Sheet first, then return here
     for SDLC-integration guidance.
The foundation of continuous authorization testing is a structured mapping of
rules that can be consumed by automated frameworks. Rather than writing
scattered, one-off test cases, design a central matrix.
### Define the Access Policy Model
Before writing tests, explicitly define the application's access model using
the Actor-Resource-Action pattern described in OWASP_WSTG_-_Testing_for
Authorization:
    * Actor (Who): The logical role or specific user attempting the operation
      (e.g., Tenant_Admin, Standard_User, Anonymous_User).
    * Resource (What): The object or data being accessed (e.g., Invoice_123, /
      api/v2/users, System_Settings).
    * Action (How): The operation being performed (e.g., READ, CREATE, DELETE,
      EXECUTE).
### Machine-Readable Rules
Store this matrix in a machine-readable format (e.g., JSON, YAML, or structured
test fixtures) rather than a spreadsheet. This allows testing frameworks to
dynamically generate test cases, reducing manual maintenance as the
authorization policy evolves.
# Example Test Fixture Definition
policies:
  - resource: "/api/invoices/{id}"
    method: "GET"
    owner_role: "tenant_user"
    allowed_roles: ["tenant_admin", "system_auditor"]
    denied_roles: ["anonymous", "different_tenant_user"]
    expected_denial_code: 403
## Regression Testing Patterns
Automated tests should specifically target the ways authorization usually
degrades over time. Implement the following test patterns in your regression
suite.
### Horizontal Escalation (IDOR) Validation
Horizontal_privilege_escalation occurs when a user accesses a resource
belonging to another user with the same privilege level. The OWASP_IDOR
Prevention_Cheat_Sheet describes the root cause: missing server-side ownership
checks on object identifiers.
    * Pattern: The "Multi-User Replay."
    * Implementation: Authenticate as User A and create Resource X. Capture the
      resource identifier. Authenticate as User B (same role, different
      account) and attempt to read, update, and delete Resource X.
    * Assertion: The system must return a 403_Forbidden or 404 Not Found (to
      avoid information leakage about resource existence), never a 200 OK.
### Vertical Escalation Validation
Vertical escalation occurs when a lower-privileged user accesses functions
reserved for higher-privileged roles. This maps directly to CWE-269:_Improper
Privilege_Management.
    * Pattern: The "Role Demotion Check."
    * Implementation: Build a suite of tests that target administrative
      endpoints (e.g., /api/admin/users/delete). Iterate through all non-
      administrative roles (including unauthenticated users) and attempt to
      execute the endpoints.
    * Assertion: Ensure the endpoints explicitly reject the requests. Relying
      on UI hiding is insufficient; the_API_layer_must_enforce_the_check —
      client-side controls are trivially bypassed.
### Tenant Isolation Breakage
In multi-tenant SaaS applications, logic changes (like caching or query
modifications) can inadvertently leak data across tenant boundaries, a scenario
covered by the Multi-Tenant_Security_Cheat_Sheet.
    * Pattern: The "Cross-Tenant Boundary Test."
    * Implementation: Provision two distinct tenants (Tenant Alpha and Tenant
      Beta) in the test environment. Seed data into Tenant Alpha. Execute broad
      read queries (e.g., GET /api/all-records) as a user from Tenant Beta.
    * Assertion: Assert that the response payload contains absolutely no
      records belonging to Tenant Alpha. Even a single leaked record identifier
      constitutes a critical failure.
## Contract-Driven Authorization Validation
When building APIs, the authorization schema should be explicitly defined in
the API contract. The OpenAPI_Specification provides securitySchemes and
security fields to formally declare authorization requirements at both the
global and per-operation level.
    * Schema-Aware Testing: Use the OpenAPI definition as the source of truth
      for authorization requirements. If the specification states an endpoint
      requires an OAuth2 scope of read:invoices, the testing framework should
      automatically verify that tokens lacking this scope receive a 401
      Unauthorized or 403 Forbidden response. Tools such as Schemathesis can
      read the OpenAPI document and auto-generate these negative test cases.
    * Middleware Enforcement: Configure API gateways or web frameworks to
      automatically enforce the security definitions present in the OpenAPI
      contract. Regression tests should validate that this middleware has not
      been bypassed or disabled following a refactor.
## Automated Testing Framework Integration
Authorization tests must live alongside functional tests in the developer's
standard toolkit, following the guidance in OWASP_SAMM:_Security_Testing.
    * Test Frameworks: Use standard test runners (e.g., pytest for Python, Jest
      for JavaScript, JUnit for Java) to build authorization suites. This keeps
      the barrier to entry low and ensures the tests run in the same CI
      pipeline as functional tests.
    * Property-Based Testing: Tools like Schemathesis or Dredd can read an
      OpenAPI specification and automatically generate negative test cases
      (e.g., sending requests without tokens, with expired tokens, or with
      tokens missing required scopes) to ensure the API fails securely.
    * Session Switching: Design the test suite to quickly and cheaply swap
      authentication context (e.g., swapping JWTs in the Authorization header
      as defined in RFC_6750) without requiring a full login flow for every
      test.
## CI/CD Gating and SDLC Integration
The value of an authorization regression suite is only realized if it prevents
vulnerable code from merging. The OWASP_CI/CD_Security_Cheat_Sheet describes
broader pipeline hardening; the recommendations below focus specifically on
authorization gates.
    * Blocking PR Builds: The authorization test suite must be a required check
      in the CI/CD pipeline (e.g., GitHub_Actions, GitLab CI). If an
      authorization test fails, the Pull Request cannot be merged.
    * Dedicated Test Suites: Tag or group authorization tests distinctly (e.g.,
      @pytest.mark.authz or a dedicated authz-tests npm script). This allows
      developers to run them quickly and independently during local
      development.
    * Monitoring in Lower Environments: Configure CI environments to flag
      unusual volumes of 401_Unauthorized or 403_Forbidden responses during
      integration testing, which may indicate that a developer's functional
      changes are colliding with existing security controls.
## References
### OWASP Resources
    * OWASP_Top_Ten_2021_—_A01:_Broken_Access_Control
    * OWASP_Web_Security_Testing_Guide_v4.2_—_Authorization_Testing
    * OWASP_WSTG_—_Testing_for_Insecure_Direct_Object_References
    * OWASP_Proactive_Controls_C7:_Enforce_Access_Controls
    * OWASP_Software_Assurance_Maturity_Model_(SAMM):_Security_Testing
    * OWASP_Application_Security_Verification_Standard_(ASVS)_4.0_—_V4:_Access
      Control
### Related OWASP Cheat Sheets
    * Authorization_Cheat_Sheet
    * Authorization_Testing_Automation_Cheat_Sheet
    * Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet
    * Multi-Tenant_Security_Cheat_Sheet
    * CI/CD_Security_Cheat_Sheet
### Standards and Specifications
    * OpenAPI_Specification_3.1.0_—_Security_Scheme_Object
    * OAuth_2.0_Authorization_Framework_(RFC_6749)
    * OAuth_2.0_Bearer_Token_Usage_(RFC_6750)
    * HTTP_Semantics_(RFC_9110)_—_401_Unauthorized
    * HTTP_Semantics_(RFC_9110)_—_403_Forbidden
    * CWE-269:_Improper_Privilege_Management
### Tools
    * Schemathesis_—_Property-based_API_testing
    * Dredd_—_HTTP_API_Testing_Framework
    * pytest_—_Python_test_framework
    * JUnit_5_—_Java_test_framework
    * Jest_—_JavaScript_test_framework
©Copyright
- Cheat Sheets Series Team - This work is licensed under Creative_Commons
Attribution-ShareAlike_4.0_International.
Made with Material_for_MkDocs
