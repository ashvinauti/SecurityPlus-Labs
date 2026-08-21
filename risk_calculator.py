#!/usr/bin/env python3
"""
Risk Assessment Calculator
Calculate risk scores using various methodologies

Usage:
    python3 risk_calculator.py calculate --threat-name "SQL Injection" --likelihood 4 --impact 5 --vulnerability 3
    python3 risk_calculator.py analyze-file risks.csv
"""

import json
import csv
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict
from enum import Enum


class RiskLevel(Enum):
    """Risk severity levels"""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


@dataclass
class RiskAssessment:
    """Risk assessment data structure"""
    threat_name: str
    likelihood: int  # 1-5
    impact: int      # 1-5
    vulnerability: int  # 1-5
    description: str = ""
    mitigation: str = ""
    
    def calculate_risk_score(self) -> int:
        """Calculate risk score using standard formula"""
        return self.likelihood * self.impact * self.vulnerability
    
    def get_risk_level(self) -> RiskLevel:
        """Determine risk level based on score"""
        score = self.calculate_risk_score()
        
        if score >= 101:
            return RiskLevel.CRITICAL
        elif score >= 61:
            return RiskLevel.HIGH
        elif score >= 26:
            return RiskLevel.MEDIUM
        else:
            return RiskLevel.LOW
    
    def get_risk_color(self) -> str:
        """Get ANSI color code for risk level"""
        level = self.get_risk_level()
        colors = {
            RiskLevel.CRITICAL: "\033[91m",  # Red
            RiskLevel.HIGH: "\033[93m",      # Yellow
            RiskLevel.MEDIUM: "\033[94m",    # Blue
            RiskLevel.LOW: "\033[92m",       # Green
        }
        return colors.get(level, "\033[0m")
    
    def reset_color(self) -> str:
        """Reset ANSI color"""
        return "\033[0m"


class RiskCalculator:
    """Calculate and analyze risks"""
    
    # Risk factor scales
    LIKELIHOOD_SCALE = {
        1: "Very Unlikely (< 10% chance)",
        2: "Unlikely (10-30%)",
        3: "Possible (30-50%)",
        4: "Likely (50-80%)",
        5: "Very Likely (> 80%)"
    }
    
    IMPACT_SCALE = {
        1: "Minimal (Low financial/reputational impact)",
        2: "Low (Some financial/operational impact)",
        3: "Medium (Significant impact)",
        4: "High (Major impact)",
        5: "Critical (Catastrophic impact)"
    }
    
    VULNERABILITY_SCALE = {
        1: "Well-defended (difficult to exploit)",
        2: "Fairly defended",
        3: "Moderately defended",
        4: "Poorly defended",
        5: "Undefended (trivial to exploit)"
    }
    
    def __init__(self):
        self.risks: List[RiskAssessment] = []
    
    def add_risk(self, assessment: RiskAssessment):
        """Add a risk assessment"""
        self.risks.append(assessment)
    
    def print_assessment(self, assessment: RiskAssessment):
        """Print detailed risk assessment"""
        score = assessment.calculate_risk_score()
        level = assessment.get_risk_level()
        color = assessment.get_risk_color()
        reset = assessment.reset_color()
        
        print(f"\n{color}{'=' * 70}{reset}")
        print(f"{color}RISK ASSESSMENT: {assessment.threat_name}{reset}")
        print(f"{color}{'=' * 70}{reset}")
        
        print(f"\nFactors:")
        print(f"  Likelihood: {assessment.likelihood}/5 - {self.LIKELIHOOD_SCALE[assessment.likelihood]}")
        print(f"  Impact:     {assessment.impact}/5 - {self.IMPACT_SCALE[assessment.impact]}")
        print(f"  Vulnerability: {assessment.vulnerability}/5 - {self.VULNERABILITY_SCALE[assessment.vulnerability]}")
        
        print(f"\nCalculation:")
        print(f"  Risk Score = Likelihood × Impact × Vulnerability")
        print(f"  Risk Score = {assessment.likelihood} × {assessment.impact} × {assessment.vulnerability} = {score}")
        
        print(f"\n{color}Risk Level: {level.value.upper()}{reset}")
        print(f"Risk Score: {score}/125 ({score/125*100:.1f}%)")
        
        if assessment.description:
            print(f"\nDescription:")
            print(f"  {assessment.description}")
        
        if assessment.mitigation:
            print(f"\nRecommended Mitigation:")
            print(f"  {assessment.mitigation}")
        
        print(f"\n{color}{'=' * 70}{reset}\n")
    
    def generate_risk_matrix(self):
        """Generate 5x5 risk matrix"""
        print("\n" + "=" * 70)
        print("RISK MATRIX (Likelihood × Impact)")
        print("=" * 70)
        print("\nLikelihood ↓ / Impact →")
        print("┌─────────┬──────────┬──────────┬──────────┬──────────┐")
        print("│ Level   │ Minimal  │ Low      │ Medium   │ High     │ Critical │")
        print("├─────────┼──────────┼──────────┼──────────┼──────────┼──────────┤")
        
        labels = ["Very Low", "Low", "Medium", "High", "Very High"]
        
        for likelihood in range(1, 6):
            print(f"│ {labels[likelihood-1]:7s} ", end="")
            for impact in range(1, 6):
                score = likelihood * impact * 3  # Using average vulnerability of 3
                
                if score >= 101:
                    symbol = "🔴"  # Critical
                elif score >= 61:
                    symbol = "🟠"  # High
                elif score >= 26:
                    symbol = "🟡"  # Medium
                else:
                    symbol = "🟢"  # Low
                
                print(f"│ {symbol} {score:3d}  ", end="")
            print("│")
        
        print("└─────────┴──────────┴──────────┴──────────┴──────────┴──────────┘")
    
    def generate_summary_report(self):
        """Generate risk summary report"""
        if not self.risks:
            print("[!] No risks to report")
            return
        
        print("\n" + "=" * 70)
        print("RISK SUMMARY REPORT")
        print("=" * 70)
        print(f"Total Risks Assessed: {len(self.risks)}")
        
        # Count by risk level
        by_level = {}
        for risk in self.risks:
            level = risk.get_risk_level()
            by_level[level] = by_level.get(level, 0) + 1
        
        print("\nRisks by Severity:")
        colors = {
            RiskLevel.CRITICAL: "\033[91m",
            RiskLevel.HIGH: "\033[93m",
            RiskLevel.MEDIUM: "\033[94m",
            RiskLevel.LOW: "\033[92m",
        }
        for level in [RiskLevel.CRITICAL, RiskLevel.HIGH, RiskLevel.MEDIUM, RiskLevel.LOW]:
            count = by_level.get(level, 0)
            color = colors[level]
            reset = "\033[0m"
            print(f"  {color}{level.value:10s}: {count:3d}{reset}")
        
        # Sort by risk score
        print("\nTop 10 Risks (by score):")
        sorted_risks = sorted(
            self.risks,
            key=lambda x: x.calculate_risk_score(),
            reverse=True
        )[:10]
        
        print("┌─────┬────────────────────────┬──────────┬────────────┐")
        print("│ Rank│ Threat                 │ Score    │ Level      │")
        print("├─────┼────────────────────────┼──────────┼────────────┤")
        
        for i, risk in enumerate(sorted_risks, 1):
            score = risk.calculate_risk_score()
            level = risk.get_risk_level()
            name = risk.threat_name[:22]
            
            color = colors[level]
            reset = "\033[0m"
            
            print(f"│ {i:3d} │ {name:22s} │ {score:3d}/125 │ {color}{level.value:10s}{reset} │")
        
        print("└─────┴────────────────────────┴──────────┴────────────┘")
        
        # Calculate average risk
        avg_score = sum(r.calculate_risk_score() for r in self.risks) / len(self.risks)
        print(f"\nAverage Risk Score: {avg_score:.1f}/125")
        print("=" * 70)
    
    def export_csv(self, filename="risk_assessment.csv"):
        """Export risks to CSV"""
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Threat Name", "Likelihood", "Impact", "Vulnerability",
                    "Risk Score", "Risk Level", "Description", "Mitigation"
                ])
                
                for risk in self.risks:
                    writer.writerow([
                        risk.threat_name,
                        risk.likelihood,
                        risk.impact,
                        risk.vulnerability,
                        risk.calculate_risk_score(),
                        risk.get_risk_level().value,
                        risk.description,
                        risk.mitigation
                    ])
            
            print(f"[✓] Risk assessment exported to {filename}")
        except Exception as e:
            print(f"[!] Error exporting: {e}")
    
    def import_csv(self, filename):
        """Import risks from CSV"""
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    assessment = RiskAssessment(
                        threat_name=row['Threat Name'],
                        likelihood=int(row['Likelihood']),
                        impact=int(row['Impact']),
                        vulnerability=int(row['Vulnerability']),
                        description=row.get('Description', ''),
                        mitigation=row.get('Mitigation', '')
                    )
                    self.add_risk(assessment)
            
            print(f"[✓] Imported {len(self.risks)} risks from {filename}")
        except Exception as e:
            print(f"[!] Error importing: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Risk Assessment Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Calculate single risk
  python3 risk_calculator.py calculate --threat-name "SQL Injection" --likelihood 4 --impact 5 --vulnerability 3
  
  # Analyze CSV file
  python3 risk_calculator.py analyze-file risks.csv
  
  # Show risk matrix
  python3 risk_calculator.py matrix
  
  # Interactive mode
  python3 risk_calculator.py interactive
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Calculate single risk
    calc_parser = subparsers.add_parser("calculate", help="Calculate risk score")
    calc_parser.add_argument("--threat-name", required=True, help="Threat name")
    calc_parser.add_argument("--likelihood", type=int, required=True, choices=range(1, 6), help="Likelihood (1-5)")
    calc_parser.add_argument("--impact", type=int, required=True, choices=range(1, 6), help="Impact (1-5)")
    calc_parser.add_argument("--vulnerability", type=int, required=True, choices=range(1, 6), help="Vulnerability (1-5)")
    calc_parser.add_argument("--description", help="Threat description")
    calc_parser.add_argument("--mitigation", help="Mitigation strategy")
    
    # Analyze CSV file
    csv_parser = subparsers.add_parser("analyze-file", help="Analyze risk CSV file")
    csv_parser.add_argument("filename", help="CSV file path")
    
    # Risk matrix
    subparsers.add_parser("matrix", help="Display risk matrix")
    
    # Interactive mode
    subparsers.add_parser("interactive", help="Interactive risk assessment")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    calculator = RiskCalculator()
    
    if args.command == "calculate":
        assessment = RiskAssessment(
            threat_name=args.threat_name,
            likelihood=args.likelihood,
            impact=args.impact,
            vulnerability=args.vulnerability,
            description=getattr(args, 'description', ''),
            mitigation=getattr(args, 'mitigation', '')
        )
        calculator.add_risk(assessment)
        calculator.print_assessment(assessment)
        calculator.generate_summary_report()
    
    elif args.command == "analyze-file":
        calculator.import_csv(args.filename)
        calculator.generate_summary_report()
        calculator.generate_risk_matrix()
    
    elif args.command == "matrix":
        calculator.generate_risk_matrix()
    
    elif args.command == "interactive":
        print("\n" + "=" * 70)
        print("INTERACTIVE RISK ASSESSMENT")
        print("=" * 70)
        
        while True:
            print("\nEnter threat details (or 'exit' to quit):")
            threat_name = input("Threat name: ").strip()
            
            if threat_name.lower() == 'exit':
                break
            
            try:
                likelihood = int(input("Likelihood (1-5): "))
                impact = int(input("Impact (1-5): "))
                vulnerability = int(input("Vulnerability (1-5): "))
                
                if not all(1 <= x <= 5 for x in [likelihood, impact, vulnerability]):
                    print("[!] Values must be between 1 and 5")
                    continue
                
                assessment = RiskAssessment(
                    threat_name=threat_name,
                    likelihood=likelihood,
                    impact=impact,
                    vulnerability=vulnerability
                )
                calculator.add_risk(assessment)
                calculator.print_assessment(assessment)
            
            except ValueError:
                print("[!] Invalid input")
        
        calculator.generate_summary_report()


if __name__ == "__main__":
    main()
