# 🛡️ Cloud-Native SIEM Pipeline with Automated Incident Response

This project builds a cloud-native SIEM pipeline on AWS using the ELK Stack (Elasticsearch, Logstash, Kibana), Filebeat, and GitHub Actions for CI/CD and Slack for alerting.

---

## What it Does  

- **Log Ingestion**: Filebeat collects container logs from EC2 instances and forwards them to Logstash.
- **Log Processing**: Logstash parses, enriches, and sends structured logs to Elasticsearch.
- **Visualization**: Kibana visualizes logs and detects anomalies.
- **Detection & Alerts**: Custom detection rules in Kibana trigger alerts.
- **Slack Integration**: Alerts are sent to a Slack channel in real-time.
- **CI/CD Integration**: Filebeat configuration is deployed automatically using GitHub Actions when pushed to this repo.

---

## CI/CD Pipline

1. **Trigger**: Any change in `filebeat.yml` triggers GitHub Actions.
2. **Deploy**: The config is securely copied to the EC2 instance.
3. **Restart**: Filebeat container is restarted to apply the changes.
4. **Verify**: Logs are forwarded live to Logstash & Elasticsearch.

Secrets used:
- `EC2_HOST`: Public IP of EC2 running Logstash
- `EC2_SSH_KEY`: Private SSH key for EC2 login (added in GitHub Secrets)

---

## Alert Flow

1. Detection rule in Kibana matches suspicious pattern.
2. Action triggers a webhook (Python script).
3. Webhook sends structured alert to Slack using `requests` package.

---

## How to Test

1. Push a change in `filebeat.yml`
2. GitHub Action deploys it automatically
3. View logs in Kibana: `Discover > filebeat-*`
4. Trigger test alert → See alert in Slack

---

## 📂 Project Structure

<pre> ## 📂 Project Structure ``` siem-pipeline/ ├── .github/workflows/ │ └── filebeat-deploy.yml ├── filebeat-docker/ │ └── filebeat.yml ├── scripts/ │ └── alert_slack.py ├── README.md ``` </pre>



---

## 🙌 Author

**Rakesh Singh**  
[GitHub](https://github.com/Rakesh04107) | [LinkedIn](https://www.linkedin.com/in/rakesh-singh-0113a1186/) | [Portfolio](https://rakeshinfo.xyz)
