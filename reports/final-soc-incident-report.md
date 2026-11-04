# SOC Phishing Investigation Report

**Case ID:** NS-PHISH-2026-001  
**Organization:** Northstar Technologies (Fictional)  
**Incident Classification:** Authorized Phishing Simulation  
**Severity:** Low — Laboratory Context  
**Status:** Closed — Authorized Simulation  
**Incident Date:** November 3, 2026  
**Analyst Role:** Blue Team / SOC Analyst

---

## 1. Executive Summary

A controlled phishing simulation was conducted against a fictional Northstar Technologies employee.

The simulated email impersonated the organization's IT support department using a lookalike sender domain and an account-verification pretext.

The email was delivered to a local Mailpit testing environment and contained a URL pointing to a locally hosted training landing page.

Analysis identified multiple phishing indicators, including sender-domain inconsistency, account-verification language, and an embedded URL.

The investigation confirmed that Mailpit received the simulated email. However, historical HTTP access logs were unavailable, preventing confirmation of landing-page interaction.

No credential collection or account compromise was demonstrated.

**Final verdict:** Confirmed authorized phishing simulation with no demonstrated compromise.

## 2. Investigation Scope

The investigation examined the original phishing email, its headers, sender information, embedded URL, email authentication visibility, and available supporting evidence.

The analysis was limited to the controlled simulation environment. No real recipients, external phishing infrastructure, or production accounts were involved.

## 3. Evidence Reviewed

| Evidence                   | Description                                       |
| -------------------------- | ------------------------------------------------- |
| phishing-email.eml         | Original email captured by Mailpit                |
| analyze_email.py           | Python email-header analysis script               |
| detect_phishing.py         | Python phishing-indicator detection script        |
| investigation-scope.md     | Investigation scope and evidence handling         |
| email-header-analysis.md   | Header, routing, authentication, and URL findings |
| incident-timeline.md       | Confirmed event timeline                          |
| phishing-indicators.md     | Correlated phishing indicators                    |
| http-log-investigation.md  | HTTP telemetry investigation                      |
| impact-assessment.md       | Potential user and organizational impact          |
| incident-verdict.md        | Severity and classification                       |
| containment-remediation.md | Response recommendations                          |
| mitre-attack-mapping.md    | ATT&CK mapping                                    |
| incident-closure.md        | Closure decision and lessons learned              |

The original EML evidence was transferred to the Blue Team workspace and validated using matching SHA-256 hashes.

## 4. Email Forensic Findings

**Sender:** security@northstar-support.example  
**Recipient:** employee@northstar.example  
**Subject:** Action Required: Account Verification  
**Message-ID:** `<5R1YajMXyxzgLDEUCMFVoX@mailpit>`

The sender domain differed from Northstar Technologies' expected domain, `northstar.example`.

The From and Return-Path addresses matched, but this did not independently establish sender authenticity.

The Received header contained private IP addresses associated with the controlled Docker testing environment.

The email was transmitted in plain text.

## 5. Authentication Analysis

The original EML file contained no:

- Authentication-Results header
- DKIM-Signature header
- Received-SPF header

SPF, DKIM, and DMARC outcomes could not be determined from the available evidence.

The separate authentication-results.txt file contained synthetic training results and was not treated as genuine authentication evidence.

## 6. URL Investigation

**Extracted URL:** `http://127.0.0.1:8080/index.html`

The URL used the IPv4 loopback address and port 8080, corresponding to the local Python HTTP training server.

The link was consistent with the email's account-verification pretext.

No external malicious URL was identified.

The URL's presence in the email did not establish that the recipient visited the landing page.

## 7. Incident Timeline

| Timestamp (UTC)            | Confirmed Event                               |
| -------------------------- | --------------------------------------------- |
| November 3, 2026, 15:07:43 | Mailpit received the simulated phishing email |

Historical HTTP request activity could not be reconstructed from the available preserved logs.

## 8. Detection Engineering

A Python detection script was developed to identify:

1. Sender-domain mismatches.
2. Suspicious account-verification language.
3. Embedded URLs and unusual IP destinations.
4. Presence or absence of email authentication headers.

The script detected the expected indicators in the original phishing email.

These findings support analyst triage but are not independently sufficient to prove malicious activity in an unknown production environment.

## 9. MITRE ATT&CK Mapping

**T1566.002 — Phishing: Spearphishing Link**

Mapping confidence: High for the observed simulation behavior.

The email contained a phishing-themed account-verification link intended to encourage recipient interaction.

Successful initial access was not established.

Other techniques, including infrastructure acquisition and credential theft, were not mapped as observed activities because supporting evidence was unavailable.

## 10. Impact Assessment

- Email delivery to Mailpit: Confirmed
- Recipient interaction: Not established
- Landing-page visit: Not established
- Credential collection: Not performed by the training page
- Account compromise: Not established
- Production organizational impact: None demonstrated

## 11. Containment and Remediation

No production containment was required because the activity occurred within an authorized local environment.

For a comparable production incident, recommended actions would include locating related messages, quarantining confirmed malicious email, investigating URL clicks, examining identity and endpoint telemetry, and responding to confirmed credential exposure.

## 12. Incident Closure

**Disposition:** Closed — Authorized Simulation  
**Severity:** Low — Laboratory Context

The original email was preserved, investigation findings were documented, and the available indicators were analyzed.

The absence of historical HTTP telemetry was recorded as an unresolved visibility limitation.

No demonstrated compromise required operational remediation.

## 13. Lessons Learned

This investigation reinforced the importance of:

- Preserving raw email evidence.
- Validating file integrity with cryptographic hashes.
- Investigating sender identity and email routing.
- Separating real authentication evidence from synthetic data.
- Correlating multiple phishing indicators.
- Preserving HTTP telemetry.
- Distinguishing attempted activity from demonstrated impact.
- Applying evidence-based incident response and closure decisions.

---

**Final Assessment:** The evidence supports a confirmed authorized phishing simulation. The message was successfully captured by Mailpit, but recipient interaction and compromise were not established.
