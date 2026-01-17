import socket

def check_dns(domain):
    findings = []
    try:
        ip = socket.gethostbyname(domain)
        findings.append({
            "asset": domain,
            "exposure": "DNS_RESOLUTION",
            "risk": "LOW",
            "details": f"Domain resolves to IP {ip}"
        })
    except Exception:
        findings.append({
            "asset": domain,
            "exposure": "DNS_FAILURE",
            "risk": "MEDIUM",
            "details": "Domain does not resolve"
        })
    return findings
