import whois

def check_whois(domain):
    findings = []
    try:
        w = whois.whois(domain)
        registrar = w.registrar if w.registrar else "Unknown"

        findings.append({
            "asset": domain,
            "exposure": "WHOIS_METADATA",
            "risk": "LOW",
            "details": f"Registrar: {registrar}"
        })
    except Exception:
        pass

    return findings
