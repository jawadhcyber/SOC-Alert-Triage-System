SOC Alert Triage System

A Python-based Security Operations Center (SOC) alert triage tool that analyzes simulated security alerts, calculates risk scores, assigns severity levels, and generates a CSV report for investigation.

Features

- Processes multiple security alerts
- Analyzes brute-force, phishing, and login-failure events
- Evaluates failed login attempts
- Checks for suspicious-link indicators
- Calculates a risk score for each alert
- Assigns LOW, MEDIUM, or HIGH severity
- Generates a CSV triage report

Risk Scoring

The tool assigns points based on different security indicators.

Failed Login Attempts

- 5 or more → +3
- 3–4 → +2
- 1–2 → +1

Suspicious Link

- Suspicious link present → +2

Alert Type

- Brute-force alert → +2
- Phishing alert → +2

Severity Classification

- HIGH — Risk score of 5 or more
- MEDIUM — Risk score of 3–4
- LOW — Risk score below 3

Example Results

Alert Type| Source IP| Risk Score| Severity
BRUTE_FORCE| 192.168.1.50| 5| HIGH
PHISHING| 10.0.0.8| 4| MEDIUM
LOGIN_FAILURE| 172.16.0.10| 1| LOW
BRUTE_FORCE| 192.168.1.75| 4| MEDIUM
PHISHING| 203.0.113.20| 2| LOW

Project Files

- "soc_alert_triage.py" — Main Python analyzer
- "alerts.log" — Sample security alerts
- "triage_report.csv" — Generated triage report
- "README.md" — Project documentation

SOC Workflow Demonstrated

1. Receive security alerts
2. Analyze alert indicators
3. Calculate risk scores
4. Assign severity levels
5. Prioritize alerts
6. Generate a report for investigation

Technologies

- Python
- CSV
- Security event analysis
- Google Colab
- GitHub

Skills Demonstrated

- SOC alert triage
- Security event analysis
- Risk scoring
- Alert prioritization
- Python automation
- CSV reporting
- Basic incident-response workflow

Limitations

This project uses a simplified rule-based scoring system and simulated alert data. Real SOC environments use additional context such as threat intelligence, asset criticality, user behavior, authentication history, and SIEM/EDR telemetry.

Future Improvements

- Add timestamps and usernames
- Include asset criticality in risk scoring
- Add IP reputation information
- Add alert status and analyst notes
- Export incident summaries
- Integrate with SIEM-style data sources

Ethical Use

This project is intended for cybersecurity education, defensive security analysis, and SOC training.

Author

Jawad Hussain

Computer Science Graduate | Aspiring Cybersecurity Analyst
