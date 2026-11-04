# MITRE ATT&CK Mapping — Phishing Investigation

## Investigation Context

This mapping examines the authorized Northstar Technologies phishing simulation using the original email evidence and investigation findings.

## Primary Technique

**T1566.002 — Phishing: Spearphishing Link**

- Tactic: Initial Access
- Mapping confidence: High
- Evidence classification: Observed simulation behavior

### Supporting Evidence

1. A phishing-themed email was submitted to and captured by Mailpit.
2. The message impersonated Northstar IT Support using a lookalike sender domain.
3. The subject used an account-verification pretext.
4. The email contained `http://127.0.0.1:8080/index.html`.

These findings demonstrate simulated delivery of a phishing link. They do not establish successful initial access.

## Additional Technique Considered

**T1583.001 — Acquire Infrastructure: Domains**

- Tactic: Resource Development
- Mapping confidence: Not supported
- Evidence classification: Hypothetical real-world technique

Attackers may acquire lookalike domains to support phishing campaigns.

However, the domain `northstar-support.example` was fictional. No domain registration or acquisition occurred during this simulation.

Therefore, T1583.001 is not classified as observed activity.

## Behaviors Not Established

The available evidence does not demonstrate:

- A recipient clicking the phishing link
- Credential harvesting or theft
- Malware execution
- Account compromise
- Persistence or lateral movement

These behaviors must not be represented as observed ATT&CK techniques.

## Detection Opportunities

Relevant defensive opportunities include:

1. Detecting lookalike sender domains.
2. Identifying phishing-related language and embedded URLs.
3. Correlating suspicious emails with URL-click telemetry.
4. Reviewing authentication and identity logs for subsequent suspicious activity.
5. Investigating endpoint activity when user interaction is confirmed.

## Final Assessment

The strongest supported mapping is T1566.002 — Phishing: Spearphishing Link.

This mapping describes an authorized phishing simulation, not a successful compromise of a production environment.

Other ATT&CK techniques require additional evidence before they can be assigned as observed activity.

## Reference

https://attack.mitre.org/techniques/T1566/002/

https://attack.mitre.org/techniques/T1583/001/
