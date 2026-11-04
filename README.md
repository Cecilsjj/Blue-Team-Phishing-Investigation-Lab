# Blue Team Phishing Investigation & Incident Response Lab

## Overview

A hands-on Security Operations Center (SOC) investigation of an authorized phishing simulation, using original email evidence generated in a separate Red Team lab.

This project demonstrates email forensics, phishing detection engineering, indicator analysis, incident response decision-making, and professional security reporting.

**Investigation status:** Closed — Authorized Simulation  
**Severity:** Low (laboratory context)  
**Verdict:** Confirmed simulated phishing attempt; no demonstrated compromise

## Investigation Scenario

Northstar Technologies, a fictional organization, received a simulated account-verification email claiming to originate from its IT support department.

The email used a lookalike sender domain and directed the recipient to a locally hosted training page.

The investigation examined the original EML evidence to determine what happened, identify phishing indicators, assess potential impact, and recommend appropriate response actions.

The email was captured by Mailpit in a controlled local environment. No external recipients were targeted or credentials collected.

## Tools and Technologies

- Python — Email parsing and phishing detection
- Mailpit — Local email capture
- SMTP — Email delivery and routing analysis
- Visual Studio Code — Investigation and scripting
- PowerShell — Evidence inspection and SHA-256 validation
- Docker — Local simulation infrastructure
- MITRE ATT&CK — Technique mapping
- GitHub — Evidence and investigation documentation

## Investigation Workflow

| Stage | Activity |
|---|---|
| 1. Evidence Preservation | Copied the original EML and verified SHA-256 integrity |
| 2. Email Forensics | Examined sender identity, routing, message headers, and authentication visibility |
| 3. IOC Analysis | Investigated the lookalike sender domain and embedded URL |
| 4. Evidence Correlation | Established the incident timeline and reviewed available HTTP telemetry |
| 5. Detection Engineering | Built a Python script to flag suspicious email characteristics |
| 6. Incident Response | Assessed severity, potential impact, containment, and remediation |
| 7. ATT&CK Mapping | Mapped the simulated phishing-link technique |
| 8. Incident Closure | Documented findings, limitations, and closure justification |

## Key Investigation Findings

| Indicator | Finding |
|---|---|
| Sender | security@northstar-support.example |
| Expected domain | northstar.example |
| Subject | Action Required: Account Verification |
| Embedded URL | http://127.0.0.1:8080/index.html |
| Email format | Plain text |
| SPF/DKIM/DMARC | Outcomes unavailable from original EML |
| HTTP interaction | Not established |
| Credential compromise | Not established |

The combination of sender-domain inconsistency, IT-support impersonation, and account-verification language supported the simulated phishing classification.

The absence of preserved HTTP access logs prevented confirmation of landing-page interaction.

## Python Phishing Detection

A reusable Python script was developed to identify:

- Sender-domain mismatches
- Suspicious account-verification language
- Embedded URLs
- Loopback and non-public IP destinations
- Presence or absence of email authentication headers

The script produces indicator-level alerts to support analyst triage.

These indicators are not treated as independent proof of malicious activity.

### Run the Detection Script

From the repository root, using Python 3:

```powershell
py scripts/detect_phishing.py
```

### Inspect Email Headers

```powershell
py scripts/analyze_email.py
```

Both scripts use the included fictional EML evidence.

## MITRE ATT&CK

**T1566.002 — Phishing: Spearphishing Link**

The simulated email used an account-verification pretext and included a link to a locally hosted training page.

This mapping describes the simulated phishing delivery technique. Successful initial access or account compromise was not established.

[MITRE ATT&CK T1566.002](https://attack.mitre.org/techniques/T1566/002/)

## Incident Response Assessment

**Incident classification:** Authorized phishing simulation  
**Severity:** Low — Laboratory context  
**Compromise status:** Not established  
**Disposition:** Closed — Authorized Simulation

No production containment was necessary.

For a comparable production incident, appropriate actions could include email quarantine, recipient scoping, URL-click investigation, identity-log review, endpoint investigation, and credential remediation where justified by evidence.

## Project Structure

```text
Blue-Team-Phishing-Investigation-Lab/
├── evidence/
│   └── phishing-email.eml
├── reports/
│   ├── investigation-scope.md
│   ├── email-header-analysis.md
│   ├── incident-timeline.md
│   ├── phishing-indicators.md
│   ├── http-log-investigation.md
│   ├── impact-assessment.md
│   ├── incident-verdict.md
│   ├── containment-remediation.md
│   ├── mitre-attack-mapping.md
│   ├── incident-closure.md
│   └── final-soc-incident-report.md
└── scripts/
    ├── analyze_email.py
    └── detect_phishing.py
```

## Investigation Reports

**Primary deliverable:** [Final SOC Incident Report](reports/final-soc-incident-report.md)

Supporting documentation:

- [Investigation Scope](reports/investigation-scope.md)
- [Email Header and Authentication Analysis](reports/email-header-analysis.md)
- [Incident Timeline](reports/incident-timeline.md)
- [Phishing Indicator Analysis](reports/phishing-indicators.md)
- [HTTP Log Investigation](reports/http-log-investigation.md)
- [Impact Assessment](reports/impact-assessment.md)
- [Incident Verdict](reports/incident-verdict.md)
- [Containment and Remediation](reports/containment-remediation.md)
- [MITRE ATT&CK Mapping](reports/mitre-attack-mapping.md)
- [Incident Closure](reports/incident-closure.md)

## Lessons Learned

This project strengthened practical experience in interpreting raw email evidence, correlating indicators, developing Python-based detection logic, and making evidence-based incident response decisions.

A key lesson was that identifying phishing characteristics does not automatically establish successful compromise.

Investigation conclusions must distinguish confirmed activity from potential risks and acknowledge gaps in available telemetry.

## Related Project

[Red Team Phishing Simulation Lab](https://github.com/Cecilsjj/Red-Team_Phishing-Lab)

The Red Team project generated the original simulated phishing email used in this Blue Team investigation.

---

**Disclaimer:** This project was conducted in an authorized local testing environment using fictional identities and reserved example domains. All findings relate to a controlled cybersecurity training simulation.
