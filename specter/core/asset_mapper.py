class AssetMapper:
    def collect_assets(self):
        return {
            "domains": ["example.com"],
            "emails": ["security@example.com"],
            "cloud": ["aws", "azure"],
            "vendors": ["github", "cloudflare"]
        }
