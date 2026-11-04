import email
from pathlib import Path
email_path = Path("evidence/phishing-email.eml")
print(email_path.exists())
with open(email_path, "rb") as file:
    message = email.message_from_binary_file(file)
    print(message["Subject"])

print("From:", message["From"])
print("To:", message["To"])
print("Return-Path:", message["Return-Path"])
print("Received:", message["Received"])
print("Message-ID:", message["Message-ID"])