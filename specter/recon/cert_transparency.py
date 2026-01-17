import requests

def check_ct_logs(domain):
    findings = []
    url = f"https://crt.sh/?q={domain}&output=json"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and response.text.strip():
            findings.append({
                "asset": domain,
                "exposure": "CERT_TRANSPARENCY",
                "risk": "MEDIUM",
                "details": "Certificates publicly exposed via CT logs"
            })
    except Exception:
        pass

    return findings
