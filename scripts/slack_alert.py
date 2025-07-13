# scripts/slack_alert.py

import requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"  # Replace with your webhook

def send_slack_alert(message):
    payload = {"text": f":rotating_light: *SIEM Alert:* {message}"}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        print("✅ Alert sent to Slack.")
    else:
        print(f"❌ Failed: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_slack_alert("🚨 Suspicious activity detected in log-generator container.")

