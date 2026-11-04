# Blue Team Phishing Investigaiton

## 1. Investigation Objective

Determine whether the email received by the user is legitimate or a phishing attempt by examining its headers, sender information, and embedded URLs.

Investigate the available evidence to determine what activity occurred, identify potential security risks, and assess whether there is evidence of compromise.

## 2. Evidence Inventory

| Evidence                   | Source             | Classification                    |
| -------------------------- | ------------------ | --------------------------------- |
| phishing-email.eml         | Mailpit            | Original evidence (verified copy) |
| authentication-results.txt | Red Team Lab       | Synthetic training data           |
| phishing-email.html        | Red Team Lab       | Template, not transmitted         |
| HTTP server logs           | Python HTTP Server | Availability not yet verified     |

## 3. Evidence Handling

1. Preserve the original Red Team evidence without modification.
2. Conduct the investigation using verified working copies.
3. Use SHA-256 hashes to validate evidence integrity.
4. Clearly distinguish observed evidence from synthetic training data.
5. Document investigative findings and conclusions based on supporting evidence.
6. Do not claim user interaction or compromise without supporting logs.

## 4. Investigation Boundaries

1. This investigation examines an authorized phishing simulation conducted in a controlled local environment.
2. All sender and recipient identities are fictional.
3. Mailpit captured the email locally; no external email delivery occurred.
4. The landing page did not collect usernames or passwords.
5. SPF, DKIM, and DMARC results were synthetically created for training and cannot establish actual authentication outcomes.
6. HTTP access logs have not yet been verified and cannot currently establish whether the recipient visited the landing page.
7. Investigation conclusions must be limited to the available evidence.
