# Email Header Analysis

## Investigation Summary

The original email was examined using a Python email-parsing script.

The message claims to originate from Northstar IT Support and uses the sender domain `northstar-support.example`, which differs from the organization's expected domain, `northstar.example`.

## Header Findings

| Header       | Observation                                               |
| ------------ | --------------------------------------------------------- |
| From         | Northstar IT Support <security@northstar-support.example> |
| Return-Path  | security@northstar-support.example                        |
| To           | employee@northstar.example                                |
| Subject      | Action Required: Account Verification                     |
| Message-ID   | 5R1YajMXyxzgLDEUCMFVoX@mailpit                            |
| Received     | Private Docker network addresses                          |
| Content-Type | text/plain; charset="utf-8"                               |

## Security Analysis

The From and Return-Path addresses match, but this does not independently establish sender authenticity.

The sender domain resembles the organization's expected domain and warrants further investigation for possible impersonation.

The Received header contains private IP addresses associated with the controlled Docker environment. These addresses do not demonstrate external delivery.

The original message was transmitted in plain text, despite the existence of a separate HTML email template.

## Preliminary Finding

The email exhibits indicators consistent with the controlled phishing simulation.

The available headers alone do not establish successful user interaction, credential theft, or account compromise.

## Email Routing Investigation

### Sender Identity

The email claims to originate from Northstar IT Support using `security@northstar-support.example`.

The `From` and `Return-Path` addresses match. However, this alignment does not independently prove sender authenticity.

The domain `northstar-support.example` differs from the expected organizational domain `northstar.example`, making domain impersonation a relevant investigative concern.

### Received Header Analysis

The message contains the following routing information:

- Sending host identifier: `172.25.217.190`
- SMTP peer address: `172.17.0.1`
- Receiving service: Mailpit
- Recorded delivery time: November 3, 2026, 15:07:43 UTC
- Delivery protocol: SMTP (Simple Mail Transfer Protocol)

Both IP addresses belong to the private `172.16.0.0/12` range.

The routing information is consistent with the controlled Docker environment used during the phishing simulation.

### Message Identification

Message-ID: `<5R1YajMXyxzgLDEUCMFVoX@mailpit>`

The Message-ID can help correlate this email with other available records. It is not proof of sender authenticity.

### Investigation Limitations

The available Received header documents the local SMTP delivery observed by Mailpit.

It does not independently establish the legitimacy of the sender domain, an external transmission path, or successful user interaction.

### Finding

The message was received by the local Mailpit server through the controlled testing infrastructure. Sender authorization has not been independently established through actual email authentication records.

## Email Authentication Analysis

### Evidence Examined

The original `phishing-email.eml` file was examined for authentication-related headers using Python.

### Findings

| Authentication Evidence | Observation          |
| ----------------------- | -------------------- |
| Authentication-Results  | Not present          |
| DKIM-Signature          | Not present          |
| Received-SPF            | Not present          |
| SPF result              | Cannot be determined |
| DKIM result             | Cannot be determined |
| DMARC result            | Cannot be determined |

### Synthetic Evidence

The Red Team project contains `authentication-results.txt`, which was manually created for training.

These results are synthetic and do not represent authentication checks performed by Mailpit.

### SOC Assessment

The absence of authentication headers prevents confirmation of SPF, DKIM, or DMARC outcomes.

No authentication failure or successful authentication can be established from the available message.

The lookalike sender domain remains a relevant phishing indicator, independent of the unavailable authentication results.

### Recommended Investigation

In a production environment, examine the receiving email security gateway's authentication results, verify the sending domain's DNS records, and review SPF/DKIM alignment with DMARC policy.

## URL and Domain Investigation

### Extracted URL

`http://127.0.0.1:8080/index.html`

The URL was extracted from the original `.eml` message body.

### Technical Analysis

- Protocol: HTTP
- Destination: 127.0.0.1
- Port: 8080
- Resource: /index.html
- Address classification: IPv4 loopback
- Known lab purpose: Locally hosted phishing-awareness landing page

### Domain Analysis

The sender domain `northstar-support.example` resembles the expected organization domain `northstar.example`.

This difference is consistent with the domain impersonation scenario established in the Red Team simulation.

The `.example` top-level domain is reserved for documentation and testing. These fictional domains are not evidence of publicly registered malicious infrastructure.

### Threat Intelligence Limitations

The extracted URL uses a loopback address and cannot be meaningfully evaluated as an internet-hosted phishing destination using public reputation services.

No external IP or public malicious domain was identified in the available evidence.

### Investigation Finding

The original email contains an account-verification link directing the recipient to the local training landing page.

The message exhibits simulated phishing characteristics, including an account-verification pretext and a lookalike sender domain.

The presence of the link does not establish that the recipient visited the page or that credentials were compromised.
