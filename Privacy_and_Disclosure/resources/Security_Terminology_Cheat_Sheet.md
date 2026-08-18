## Table of Contents
- Introduction
- Table of Contents
- Data Handling: Encoding, Escaping, Sanitization, and Serialization
  - Encoding
  - Escaping
  - Sanitization
  - Serialization
- Cryptography: Encryption, Hashing, and Signatures
  - Encryption
  - Hashing
  - Signatures (Digital Signatures)
- Identity: Authentication and Authorization
  - Authentication (AuthN)
  - Authorization (AuthZ)
- Federated Identity Terms
- References
# Security Terminology Cheat Sheet
## Introduction
This cheat sheet provides clear definitions and distinctions for security
terminology that is often confused, even by experienced developers.
Understanding these terms is critical for correctly implementing security
controls and following standards like the OWASP_ASVS.
## Table of Contents
    * Data_Handling:_Encoding,_Escaping,_Sanitization,_and_Serialization
    * Cryptography:_Encryption,_Hashing,_and_Signatures
    * Identity:_Authentication_and_Authorization
    * Federated_Identity_Terms
    * References
## Data Handling: Encoding, Escaping, Sanitization, and Serialization
These terms relate to how data is transformed for transport, storage, or
display.
### Encoding
Definition: Transforming data into a different format using a publicly
available scheme, so that it can be safely consumed by a different system.
    * Purpose: Not for security, but for data usability and compatibility.
    * Reversibility: Always reversible.
    * Examples: Base64, URL Encoding, HTML Entity Encoding.
    * Security Context: Using the wrong encoding can lead to vulnerabilities,
      but encoding itself is not a security control.
### Escaping
Definition: A sub-type of encoding where specific characters are prefixed with
a "signal" character (like a backslash) to prevent them from being
misinterpreted by a parser as control characters.
    * Purpose: To ensure the interpreter treats the data as text rather than
      code/commands.
    * Examples: \' in SQL, \n in strings, &lt; in HTML.
    * Security Context: Essential for preventing Injection attacks (XSS, SQLi).
### Sanitization
Definition: The process of cleaning or filtering input by removing, replacing,
or modifying potentially dangerous characters or content.
    * Purpose: To make "dirty" input "clean" according to a security policy.
    * Examples: Stripping <script> tags from HTML input, removing special
      characters from a filename.
    * Security Context: Use as a secondary defense; prefer parameterized
      queries or output escaping where possible.
### Serialization
Definition: Converting an object or data structure into a format that can be
stored or transmitted (e.g., a byte stream) and later reconstructed.
    * Purpose: Data persistence and communication.
    * Security Context: Insecure Deserialization occurs when untrusted data is
      used to reconstruct an object, potentially leading to Remote Code
      Execution (RCE).
===============================================================================
## Cryptography: Encryption, Hashing, and Signatures
These terms relate to protecting the confidentiality, integrity, and
authenticity of data.
### Encryption
Definition: Transforming data (plaintext) into an unreadable format
(ciphertext) using a secret key.
    * Purpose: Confidentiality. Only authorized parties with the key can read
      the data.
    * Reversibility: Reversible (Decryption) with the correct key.
    * Types: Symmetric (same key) and Asymmetric (public/private keys).
### Hashing
Definition: Transforming data into a fixed-size string (a "hash" or "digest")
using a mathematical function.
    * Purpose: Integrity. A small change in the input results in a completely
      different hash.
    * Reversibility: One-way (non-reversible).
    * Security Context: Used for password storage (with salt) and verifying
      file integrity.
    * Examples: SHA-256, Argon2, bcrypt.
### Signatures (Digital Signatures)
Definition: Using asymmetric cryptography to provide proof of the origin and
integrity of a message.
    * Purpose: Authenticity and Non-repudiation. Proves who sent the message
      and that it wasn't altered.
    * Mechanism: The sender signs a hash of the message with their private key;
      the receiver verifies it with the sender's public key.
    * Example: JWT signatures, GPG signatures.
===============================================================================
## Identity: Authentication and Authorization
### Authentication (AuthN)
Definition: The process of verifying who a user is.
    * Question: "Who are you?"
    * Factors: Something you know (password), something you have (token),
      something you are (biometrics).
### Authorization (AuthZ)
Definition: The process of verifying what a user has permission to do.
    * Question: "Are you allowed to do this?"
    * Security Context: Occurs after successful authentication.
    * Examples: Role-Based Access Control (RBAC), Attribute-Based Access
      Control (ABAC).
===============================================================================
## Federated Identity Terms
When working with OAuth2, SAML, or OIDC, these terms are frequently used:
Term                    Definition                    Context
                        The system that creates,
                        maintains, and manages
Identity Provider (IdP) identity information and      Google, Okta, Azure AD
                        provides authentication
                        services.
                        An application or service     Your web app using "Login
Relying Party (RP)      that relies on an IdP to      with Google"
                        authenticate users.
Service Provider (SP)   In SAML, the equivalent of a  Your enterprise app using
                        Relying Party.                SAML
Principal               The entity (user, service, or The user logging in
                        device) being authenticated.
===============================================================================
## References
    * OWASP_ASVS_Standard
    * OWASP_Key_Management_Cheat_Sheet
    * OWASP_Password_Storage_Cheat_Sheet
    * OWASP_Input_Validation_Cheat_Sheet
©Copyright
- Cheat Sheets Series Team - This work is licensed under Creative_Commons
Attribution-ShareAlike_4.0_International.
Made with Material_for_MkDocs
