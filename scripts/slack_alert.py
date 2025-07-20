# scripts/slack_alert.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_alert(message):
    payload = {"text": f":rotating_light: *SIEM Alert:* {message}"}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        print("✅ Alert sent to Slack.")
    else:
        print(f"❌ Slack alert failed: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_slack_alert("🚨 Suspicious activity detected in log-generator container.")



