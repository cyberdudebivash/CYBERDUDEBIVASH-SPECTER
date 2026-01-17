#!/usr/bin/env python3
"""
CYBERDUDEBIVASH SPECTER™
Ghost Recon Exposure Intelligence Platform (SAFE MODE)

© CyberDudeBivash Pvt. Ltd.
"""

import argparse
from specter.core.scanner import run_safe_scan
from specter.reporting.json_report import generate_report

BANNER = r"""
███████╗██████╗ ███████╗ ██████╗████████╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
███████╗██████╔╝█████╗  ██║        ██║   █████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══╝  ██╔══██╗
███████║██║     ███████╗╚██████╗   ██║   ███████╗██║  ██║
╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

CYBERDUDEBIVASH SPECTER™
Ghost Recon Exposure Intelligence Platform
© CyberDudeBivash Pvt. Ltd.
"""

def main():
    print(BANNER)

    parser = argparse.ArgumentParser(
        description="Passive domain reconnaissance (SAFE MODE only)"
    )
    parser.add_argument(
        "--target",
        help="Target domain (example: example.com)",
        required=False
    )

    args = parser.parse_args()
    findings = []

    if args.target:
        print(f"[+] Running SAFE reconnaissance on: {args.target}")
        findings = run_safe_scan(args.target)
    else:
        print("[!] No target provided. Generating empty baseline report.")

    generate_report(findings)

if __name__ == "__main__":
    main()
