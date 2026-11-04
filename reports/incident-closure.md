# Phishing Investigation — Incident Closure

## 1. Case Summary

An authorized phishing simulation targeted a fictional Northstar Technologies employee.

The simulated email used an IT-support display name, a lookalike sender domain, an account-verification pretext, and a locally hosted training URL.

The message was captured by Mailpit and investigated using the original EML evidence.

## 2. Evidence Validation

| Evidence                | Validation                                                   |
| ----------------------- | ------------------------------------------------------------ |
| Original EML file       | Preserved in Red Team project                                |
| Blue Team EML copy      | SHA-256 hash matched original                                |
| Email headers           | Parsed using Python                                          |
| Sender domain           | Compared against expected organizational domain              |
| Embedded URL            | Extracted from original email                                |
| Authentication results  | No authentication-result headers found                       |
| HTTP logs               | No matching preserved log files identified in project search |
| Python detection script | Successfully detected multiple phishing indicators           |

## 3. Confirmed Findings

1. Mailpit received the simulated phishing email.
2. The sender domain differed from the expected organizational domain.
3. The email contained an account-verification pretext and a loopback URL.
4. The original EML did not contain the inspected authentication headers.
5. The Python detection script identified suspicious characteristics.

## 4. Unresolved Questions

- Was the landing page accessed during the original simulation?
- Were HTTP request details recorded elsewhere?
- What would production email security and identity telemetry reveal?

These questions remain unresolved because the relevant historical telemetry is unavailable.

## 5. Response Validation

No operational containment was required because the activity occurred in an authorized local testing environment.

Production containment and remediation recommendations were documented separately.

## 6. Closure Decision

**Status:** Closed — Authorized Simulation

**Severity:** Low (laboratory context)

**Verdict:** Confirmed simulated phishing attempt

**Compromise:** Not established

**Closure justification:**

The controlled simulation's purpose is known, the original email evidence has been preserved, and the available indicators have been investigated.

Outstanding telemetry limitations are documented. No demonstrated compromise requires further operational response.

## 7. Lessons Learned

1. Email headers must be interpreted alongside message content and contextual evidence.
2. Matching sender addresses do not independently prove legitimacy.
3. Missing authentication headers must not be described as failed authentication.
4. Preserving HTTP access logs improves investigation and event correlation.
5. Automated detection should support, not replace, analyst judgment.
6. Incident closure decisions should reflect actual evidence and documented limitations.
