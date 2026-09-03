import csv

ALERT_FILE = "alerts.log"
REPORT_FILE = "triage_report.csv"

alerts = []

try:
    with open(ALERT_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) < 4:
                continue

            alert_type = parts[0].strip()
            source_ip = parts[1].strip()
            failed_attempts = int(parts[2].strip())
            suspicious_link = parts[3].strip().lower()

            score = 0

            if failed_attempts >= 5:
                score += 3
            elif failed_attempts >= 3:
                score += 2
            elif failed_attempts > 0:
                score += 1

            if suspicious_link == "yes":
                score += 2

            if alert_type == "BRUTE_FORCE":
                score += 2
            elif alert_type == "PHISHING":
                score += 2

            if score >= 5:
                severity = "HIGH"
            elif score >= 3:
                severity = "MEDIUM"
            else:
                severity = "LOW"

            alerts.append([
                alert_type,
                source_ip,
                failed_attempts,
                suspicious_link,
                score,
                severity
            ])

except FileNotFoundError:
    print(f"Error: {ALERT_FILE} was not found.")
    exit()

print("=== SOC Alert Triage System ===")
print()

for alert in alerts:
    print(f"Alert Type: {alert[0]}")
    print(f"Source IP: {alert[1]}")
    print(f"Risk Score: {alert[4]}")
    print(f"Severity: {alert[5]}")
    print()

with open(REPORT_FILE, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([
        "Alert Type",
        "Source IP",
        "Failed Attempts",
        "Suspicious Link",
        "Risk Score",
        "Severity"
    ])

    writer.writerows(alerts)

print(f"Triage report saved to {REPORT_FILE}")
