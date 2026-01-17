class RiskScorer:
    def __init__(self, findings):
        self.findings = findings

    def calculate(self):
        score = 0
        for f in self.findings:
            if f["risk"] == "HIGH":
                score += 30
            elif f["risk"] == "MEDIUM":
                score += 15
        return min(score, 100)
