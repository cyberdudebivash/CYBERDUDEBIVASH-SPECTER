import json
from datetime import datetime

def calculate_risk_score(findings):
    score = 0
    for f in findings:
        if f["risk"] == "LOW":
            score += 5
        elif f["risk"] == "MEDIUM":
            score += 15
        elif f["risk"] == "HIGH":
            score += 30
    return score

def generate_report(findings):
    report = {
        "tool": "CyberDudeBivash SPECTER™",
        "mode": "SAFE_PASSIVE_RECON",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "risk_score": calculate_risk_score(findings),
        "findings": findings
    }

    with open("specter_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("[+] Report written to specter_report.json")
