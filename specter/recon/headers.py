import requests

def check_headers(domain):
    findings = []
    try:
        response = requests.head(
            f"https://{domain}",
            timeout=10,
            allow_redirects=True
        )

        server = response.headers.get("Server", "Not disclosed")

        findings.append({
            "asset": domain,
            "exposure": "HTTP_HEADERS",
            "risk": "LOW",
            "details": f"Server header: {server}"
        })
    except Exception:
        pass

    return findings
