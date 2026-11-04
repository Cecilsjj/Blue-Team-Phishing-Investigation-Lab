# Phishing Incident Timeline

## Case Information

- Organization: Northstar Technologies (fictional)
- Incident type: Simulated phishing email
- Evidence source: Mailpit SMTP capture
- Investigation date: November 3, 2026
- Time standard: UTC

## Confirmed Timeline

| Timestamp (UTC)     | Activity                                      | Evidence                              |
| ------------------- | --------------------------------------------- | ------------------------------------- |
| 2026-11-03 15:07:43 | Mailpit received the simulated phishing email | Received header in phishing-email.eml |

## Additional Activity — Not Yet Verified

| Activity                     | Evidence Status                                        |
| ---------------------------- | ------------------------------------------------------ |
| Email opened by recipient    | Not established                                        |
| Phishing URL clicked         | Not established                                        |
| HTTP request to landing page | Logs not yet verified                                  |
| Credential submission        | Not observed; landing page did not collect credentials |
| Account compromise           | No supporting evidence identified                      |

## Initial Assessment

The original email provides a confirmed SMTP receipt timestamp.

The available evidence does not establish whether the recipient opened the message or clicked the embedded URL.

Additional HTTP server logs will be investigated before drawing conclusions about landing-page interaction.
