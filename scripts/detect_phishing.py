import re
import ipaddress
from urllib.parse import urlparse

from pathlib import Path
from email import policy
from email.parser import BytesParser

EMAIL_PATH = Path("evidence/phishing-email.eml")
EXPECTED_DOMAIN = "northstar.example"

with EMAIL_PATH.open("rb") as file:
    message = BytesParser(policy=policy.default).parse(file)

from email.utils import parseaddr

sender = parseaddr(message["From"])[1]
sender_domain = sender.rsplit("@", 1)[-1].lower()

print("Sender:", sender)
print("Sender Domain:", sender_domain)

if sender_domain != EXPECTED_DOMAIN:
    print("[ALERT] Sender domain mismatch detected")
else:
    print("[PASS] Sender domain matches expected domain")

subject = message.get("Subject", "")
body_part = message.get_body(preferencelist=("plain",))
body = body_part.get_content() if body_part else ""

email_text = (subject + " " + body).lower()

suspicious_keywords = [
    "account verification",
    "verify your account",
    "action required",
    "password reset",
    "account suspended"
]

detected_keywords = [
    keyword for keyword in suspicious_keywords
    if keyword in email_text
]

if detected_keywords:
    print("[ALERT] Suspicious language detected")
    print("Matched keywords:", ", ".join(detected_keywords))
else:
    print("[PASS] No suspicious keywords detected")

urls = re.findall(r'https?://[^\s<>"\']+', body)

if urls:
    print("[INFO] URLs detected:", len(urls))

    for url in urls:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        print("URL:", url)
        print("Destination:", hostname)

        if hostname:
            try:
                ip = ipaddress.ip_address(hostname)

                if ip.is_loopback:
                    print("[ALERT] Loopback destination detected")
                elif ip.is_private:
                    print("[ALERT] Non-public IP destination detected")
                else:
                    print("[INFO] Public IP destination")

            except ValueError:
                print("[INFO] Domain-based URL requires further investigation")
else:
    print("[INFO] No URLs detected")

print("\n--- Email Authentication Evidence ---")

authentication_headers = [
    "Authentication-Results",
    "DKIM-Signature",
    "Received-SPF"
]

for header in authentication_headers:
    if message.get(header):
        print(f"[FOUND] {header}")
    else:
        print(f"[NOT PRESENT] {header}")