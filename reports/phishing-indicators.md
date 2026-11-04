# Phishing Indicator Analysis

## Case Overview

A simulated email claiming to originate from Northstar IT Support was delivered to the fictional recipient `employee@northstar.example`.

The message requested account verification and contained a link to a locally hosted training page.

## Identified Indicators

| Indicator       | Observation                           | Security Relevance                                                     |
| --------------- | ------------------------------------- | ---------------------------------------------------------------------- |
| Sender domain   | northstar-support.example             | Differs from the expected northstar.example domain                     |
| Display name    | Northstar IT Support                  | Claims organizational IT authority                                     |
| Subject         | Action Required: Account Verification | Encourages prompt action                                               |
| Message content | Account flagged for verification      | Uses an account-security pretext                                       |
| Embedded URL    | http://127.0.0.1:8080/index.html      | Directs recipient to a local training page                             |
| Authentication  | SPF/DKIM/DMARC outcomes unavailable   | Sender authenticity cannot be established from authentication evidence |

## Indicator Correlation

The message combines a lookalike sender domain, an IT-support identity, an account-verification pretext, and an embedded URL.

Together, these indicators are consistent with the phishing scenario established in the controlled simulation.

No individual indicator independently establishes malicious intent. The assessment relies on the combination of indicators and the documented simulation context.

## Investigation Finding

The message represents an authorized simulated phishing attempt.

The current evidence confirms email delivery to Mailpit but does not establish that the recipient visited the linked page or that an account was compromised.
