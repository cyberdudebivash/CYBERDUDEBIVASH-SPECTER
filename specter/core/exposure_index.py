class ExposureIndex:
    def __init__(self, assets):
        self.assets = assets

    def run(self):
        findings = []
        for domain in self.assets.get("domains", []):
            findings.append({
                "asset": domain,
                "exposure": "CERT_TRANSPARENCY",
                "risk": "MEDIUM"
            })
        return findings
