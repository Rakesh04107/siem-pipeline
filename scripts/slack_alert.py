# scripts/slack_alert.py

import requests

# ✅ Replace this with the new working Webhook URL
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

def send_slack_alert(message):
    payload = {"text": f":rotating_light: *SIEM Alert:* {message}"}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        print("✅ Alert sent to Slack.")
    else:
        print(f"❌ Slack alert failed: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_slack_alert("🚨 Suspicious activity detected in log-generator container.")

