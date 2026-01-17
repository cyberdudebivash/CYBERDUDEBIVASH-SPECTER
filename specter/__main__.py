from specter.banner import show_banner
from specter.core.asset_mapper import AssetMapper
from specter.core.exposure_index import ExposureIndex
from specter.core.risk_scoring import RiskScorer
from specter.reporting.json_report import generate_report

def main():
    show_banner()

    mapper = AssetMapper()
    assets = mapper.collect_assets()

    exposure = ExposureIndex(assets)
    findings = exposure.run()

    scorer = RiskScorer(findings)
    score = scorer.calculate()

    generate_report(findings, score)

if __name__ == "__main__":
    main()
