"""
SAFE MODE SCANNER
Passive, non-intrusive reconnaissance only
"""

from specter.recon.dns import check_dns
from specter.recon.cert_transparency import check_ct_logs
from specter.recon.whois import check_whois
from specter.recon.headers import check_headers

def run_safe_scan(domain: str):
    findings = []

    findings.extend(check_dns(domain))
    findings.extend(check_ct_logs(domain))
    findings.extend(check_whois(domain))
    findings.extend(check_headers(domain))

    return findings
