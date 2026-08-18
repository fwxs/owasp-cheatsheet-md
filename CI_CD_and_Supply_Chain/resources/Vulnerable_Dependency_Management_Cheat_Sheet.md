## Table of Contents
- Introduction
- Context
- Remark about the detection
  - 1. Responsible disclosure
  - 2. Full disclosure
- Remark about the security issue handling decision
- Cases
  - Case 1
    - Context
    - Ideal condition of application of the approach
    - Approach
  - Case 2
    - Context
    - Ideal condition of application of the approach
    - Approach
  - Case 3
    - Context
    - Ideal condition of application of the approach
    - Approach
  - Case 4
    - Context
    - Ideal condition of application of the approach
    - Approach
- Tools
# Vulnerable Dependency Management Cheat Sheet
## Introduction
The objective of the cheat sheet is to provide a proposal of approach regarding
the handling of vulnerable third-party dependencies when they are detected, and
this, depending on different situation.
The cheat sheet is not tools oriented but it contains a tools section informing
the reader about free and commercial solutions that can be used to detect
vulnerable dependencies, depending on the level of support on the technologies
at hand
Note:
Proposals mentioned in this cheat sheet are not silver-bullet (recipes that
work in all situations) yet can be used as a foundation and adapted to your
context.
## Context
Most of the projects use third-party dependencies to delegate handling of
different kind of operations, e.g. generation of document in a specific format,
HTTP communications, data parsing of a specific format, etc.
It's a good approach because it allows the development team to focus on the
real application code supporting the expected business feature. The dependency
brings forth an expected downside where the security posture of the real
application is now resting on it.
This aspect is referenced in the following projects:
    * OWASP_TOP_10_2017 under the point A9_-_Using_Components_with_Known
      Vulnerabilities.
    * OWASP_Application_Security_Verification_Standard_Project under the
      section V14.2 Dependency.
Based on this context, it's important for a project to ensure that all the
third-party dependencies implemented are clean of any security issue, and if
they happen to contain any security issues, the development team needs to be
aware of it and apply the required mitigation measures to secure the affected
application.
It's highly recommended to perform automated analysis of the dependencies from
the birth of the project. Indeed, if this task is added at the middle or end of
the project, it can imply a huge amount of work to handle all the issues
identified and that will in turn impose a huge burden on the development team
and might to blocking the advancement of the project at hand.
Note:
In the rest of the cheat sheet, when we refer to development team then we
assume that the team contains a member with the required application security
skills or can refer to someone in the company having these kind of skills to
analyze the vulnerability impacting the dependency.
## Remark about the detection
It's important to keep in mind the different ways in which a security issue is
handled after its discovery.
### 1. Responsible disclosure
See a description here.
A researcher discovers a vulnerability in a component, and after collaboration
with the component provider, they issue a CVE (sometimes a specific
vulnerability identifier to the provider is created but generally a CVE
identifier is preferred) associated to the issue allowing the public
referencing of the issue as well as the available fixation/mitigation.
If in case the provider doesn't properly cooperate with the researcher, the
following results are expected:
    * CVE gets accepted by the vendor yet the provider refuses_to_fix_the
      issue.
    * Most of the time, if the researcher doesn't receive back a response in 30
      days, they go ahead and do a full_disclosure of the vulnerability.
Here, the vulnerability is always referenced in the CVE_global_database used,
generally, by the detection tools as one of the several input sources used.
### 2. Full disclosure
See a description here, into the section named Computers about Computer
Security.
The researcher decides to release all the information including exploitation
code/method on services like Full_Disclosure_mailing_list, Exploit-DB.
Here a CVE is not always created then the vulnerability is not always in the
CVE global database causing the detection tools to be potentially blind about
unless the tools use other input sources.
## Remark about the security issue handling decision
When a security issue is detected, it's possible to decide to accept the risk
represented by the security issue. However, this decision must be taken by the
Chief_Risk_Officer (fallback possible to Chief_Information_Security_Officer) of
the company based on technical feedback from the development team that have
analyzed the issue (see the Cases section) as well as the CVEs CVSS score
indicators.
## Cases
When a security issue is detected, the development team can meet one of the
situations (named Case in the rest of the cheat sheet) presented in the sub
sections below.
If the vulnerably impact a transitive_dependency then the action will be taken
on the direct dependency of the project because acting on a transitive
dependency often impact the stability of the application.
Acting on a on a transitive dependency require the development team to fully
understand the complete relation/communication/usage from the project first
level dependency until the dependency impacted by the security vulnerability,
this task is very time consuming.
### Case 1
#### Context
Patched version of the component has been released by the provider.
#### Ideal condition of application of the approach
Set of automated unit or integration or functional or security tests exist for
the features of the application using the impacted dependency allowing to
validate that the feature is operational.
#### Approach
Step 1:
Update the version of the dependency in the project on a testing environment.
Step 2:
Prior to running the tests, 2 output paths are possible:
    * All tests succeed, and thus the update can be pushed to production.
    * One or several tests failed, several output paths are possible:
          o Failure is due to change in some function calls (e.g. signature,
            argument, package, etc.). The development team must update their
            code to fit the new library. Once that is done, re-run the tests.
          o Technical incompatibility of the released dependency (e.g. require
            a more recent runtime version) which leads to the following
            actions: 1. Raise the issue to the provider. 2. Apply Case_2 while
            waiting for the provider's feedback.
### Case 2
#### Context
Provider informs the team that it will take a while to fix the issue and, so, a
patched version will not be available before months.
#### Ideal condition of application of the approach
Provider can share any of the below with the development team:
    * The exploitation code.
    * The list of impacted functions by the vulnerability.
    * A workaround to prevent the exploitation of the issue.
#### Approach
Step 1:
If a workaround is provided, it should be applied and validated on the testing
environment, and thereafter deployed to production.
If the provider has given the team a list of the impacted functions, protective
code must wrap the calls to these functions to ensure that the input and the
output data is safe.
Moreover, security devices, such as the Web Application Firewall (WAF), can
handle such issues by protecting the internal applications through parameter
validation and by generating detection rules for those specific libraries. Yet,
in this cheat sheet, the focus is set on the application level in order to
patch the vulnerability as close as possible to the source.
Example using java code in which the impacted function suffers from a Remote
Code_Execution issue:
public void callFunctionWithRCEIssue(String externalInput){
    //Apply input validation on the external input using regex
    if(Pattern.matches("[a-zA-Z0-9]{1,50}", externalInput)){
        //Call the flawed function using safe input
        functionWithRCEIssue(externalInput);
    }else{
        //Log the detection of exploitation
        SecurityLogger.warn("Exploitation of the RCE issue XXXXX detected !");
        //Raise an exception leading to a generic error send to the client...
    }
}
If the provider has provided nothing about the vulnerability, Case_3 can be
applied skipping the step 2 of this case. We assume here that, at least, the
CVE has been provided.
Step 2:
If the provider has provided the team with the exploitation code, and the team
made a security wrapper around the vulnerable library/code, execute the
exploitation code in order to ensure that the library is now secure and doesn't
affect the application.
If you have a set of automated unit or integration or functional or security
tests that exist for the application, run them to verify that the protection
code added does not impact the stability of the application.
Add a comment in the project README explaining that the issue (specify the
related CVE) is handled during the waiting time of a patched version because
the detection tool will continue to raise an alert on this dependency.
Note: You can add the dependency to the ignore list but the ignore scope for
this dependency must only cover the CVE related to the vulnerability because a
dependency can be impacted by several vulnerabilities having each one its own
CVE.
### Case 3
#### Context
Provider informs the team that they cannot fix the issue, so no patched version
will be released at all (applies also if provider does not want to fix the
issue or does not answer at all).
In this case the only information given to the development team is the CVE.
Notes:
    * This case is really complex and time consuming and is generally used as
      last resort.
    * If the impacted dependency is an open source library then we, the
      development team, can create a patch and create pull_request - that way
      we can protect our company/application from the source as well as helping
      others secure their applications.
#### Ideal condition of application of the approach
Nothing specific because here we are in a patch yourself condition.
#### Approach
Step 1:
If we are in this case due to one of the following conditions, it's a good idea
to start a parallel study to find another component better maintained or if
it's a commercial component with support then put pressure on the provider with
the help of your Chief_Risk_Officer (fallback possible to Chief_Information
Security_Officer):
    * Provider does not want to fix the issue.
    * Provider does not answer at all.
In all cases, here, we need to handle the vulnerability right now.
Step 2:
As we know the vulnerable dependency, we know where it is used in the
application (if it's a transitive dependency then we can identify the first
level dependency using it using the IDE built-in feature or the dependency
management system used (Maven, Gradle, NuGet, npm, etc.). Note that IDE is also
used to identify the calls to the dependency.
Identifying calls to this dependency is fine but it is the first step. The team
still lacks information on what kind of patching needs to be performed.
To obtain these information, the team uses the CVE content to know which kind
of vulnerability affects the dependency. The description property provides the
answer: SQL injection, Remote Code Execution, Cross-Site Scripting, Cross-Site
Request Forgery, etc.
After identifying the above 2 points, the team is aware of the type of patching
that needs to be taken (Case_2 with the protective code) and where to add it.
Example:
The team has an application using the Jackson API in a version exposed to the
CVE-2016-3720.
The description of the CVE is as follows:
XML external entity (XXE) vulnerability in XmlMapper in the Data format
extension for Jackson
(aka jackson-dataformat-xml) allows attackers to have unspecified impact via
unknown vectors.
Based on these information, the team determines that the necessary patching
will be to add a pre-validation_of_any_XML_data passed to the Jakson API to
prevent XML_external_entity_(XXE) vulnerability.
Step 3:
If possible, create a unit test that mimics the vulnerability in order to
ensure that the patch is effective and have a way to continuously ensure that
the patch is in place during the evolution of the project.
If you have a set of automated unit or integration or functional or security
tests that exists for the application then run them to verify that the patch
does not impact the stability of the application.
### Case 4
#### Context
The vulnerable dependency is found during one of the following situation in
which the provider is not aware of the vulnerability:
    * Via the discovery of a full disclosure post on the Internet.
    * During a penetration test.
#### Ideal condition of application of the approach
Provider collaborates with you after being notified of the vulnerability.
#### Approach
Step 1:
Inform the provider about the vulnerability by sharing the post with them.
Step 2:
Using the information from the full disclosure post or the pentester's
exploitation feedback, if the provider collaborates then apply Case_2,
otherwise apply Case_3, and instead of analyzing the CVE information, the team
needs to analyze the information from the full disclosure post/pentester's
exploitation feedback.
## Tools
This section lists several tools that can used to analyze the dependencies used
by a project in order to detect the vulnerabilities.
It's important to ensure, during the selection process of a vulnerable
dependency detection tool, that this one:
    * Uses several reliable input sources in order to handle both vulnerability
      disclosure ways.
    * Support for flagging an issue raised on a component as a false-positive.
    * Free
          o OWASP_Dependency_Check:
                # Full support: Java, .Net.
                # Experimental support: Python, Ruby, PHP (composer), NodeJS,
                  C, C++.
          o NPM_Audit
                # Full support: NodeJS, JavaScript.
                # HTML report available via this module.
          o OWASP_Dependency_Track can be used to manage vulnerable
            dependencies across an organization.
          o Trivy
                # Full support: Base OS, Java, NodeJS, JavaScript, Ruby,
                  Python, Go, .NET, Rust, PHP, Dart, Swift
                # Targets: Kubernetes (nodes and containers), Docker (nodes and
                  containers), filesystem, Git repositories, cloud images
          o Grype
                # Full support across mainstream language ecosystems with SBOM-
                  driven scanning
                # Targets: container images, filesystems, and SBOMs produced by
                  Syft
    * Commercial
          o Snyk (open source and free option available):
                # Full_support for many languages and package manager.
          o JFrog_XRay:
                # Full_support for many languages and package manager.
          o Renovate (allow to detect old dependencies):
                # Full_support for many languages and package manager.
          o Requires.io (allow to detect old dependencies - open source and
            free option available):
                # Full_support: Python only.
©Copyright
- Cheat Sheets Series Team - This work is licensed under Creative_Commons
Attribution-ShareAlike_4.0_International.
Made with Material_for_MkDocs
