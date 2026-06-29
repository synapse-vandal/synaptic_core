"""
Project Autoscribe Engine — Strategic Socratic Interrogator
Module: socratic_interrogator.py
Specification Reference: ASC-004 (The Socratic Interrogator Daemon)
Runtime Environment: Pure Python 3.14+ (Zero-Dependency Architecture)
Thread Profile: Restricted to 4-6 worker threads max (ASIO-Insulated)
"""

import os
import re
from typing import List, Dict, Set

class SocraticInterrogatorEngine:
    def __init__(self):
        # Establish the current terminal directory as the tracking root
        self.workspace_dir = os.getcwd()
        
        # Hard-coded verification checklist derived from Master Manifest Intent
        self.expected_manifest_files = {
            "synapse_test.py",
            "sovereign_watcher.py",
            "autoscribe_parser.py",
            "novelty_assessor.py",
            "novelty_hunter.py",
            "AUTOSCRIBE_CORE_SPEC.md" # Validated nomenclature anchor
        }

        # Lexical scanners targeting omissions and structural blind spots
        self.scanners = {
            "TODO_MARKERS": re.compile(r"#\s*(TODO|FIXME|HOLD):\s*(.*)", re.IGNORECASE),
            "AMBIGUITY_MARKERS": re.compile(r"\b(TBD|placeholder|temporary|optimize_later|fix_this)\b", re.IGNORECASE),
            "UNDOCUMENTED_FUNCTIONS": re.compile(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(.*?\):(?!\s*\"\"\" )")
        }

    def conduct_ecosystem_gap_analysis(self) -> Dict[str, List[str]]:
        """Scans the physical storage footprint to extract structural omissions and IP gaps."""
        gap_report = {
            "missing_manifest_assets": [],
            "critical_todos": [],
            "architectural_ambiguities": [],
            "undocumented_footprints": []
        }

        # 1. Verify existence of primary architecture assets
        present_files = set(os.listdir(self.workspace_dir))
        missing_assets = self.expected_manifest_files - present_files
        for missing in missing_assets:
            gap_report["missing_manifest_assets"].append(
                f"🚨 WARNING: Intentional asset '{missing}' is missing from the physical directory."
            )

        # 2. Deep traverse code files for internal vulnerabilities
        for root, _, files in os.walk(self.workspace_dir):
            # Enforce strict namespace partitioning to protect environmental files
            if any(part in root for part in ["VANDAL", ".git", "Obsidian Vault", "__pycache__"]):
                continue

            for file in files:
                if file.endswith((".py", ".md")):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.workspace_dir)
                    
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            lines = f.readlines()
                        
                        whole_text = "".join(lines)
                        
                        # Identify functions lacking triple-quote specification contracts
                        for match in self.scanners["UNDOCUMENTED_FUNCTIONS"].finditer(whole_text):
                            gap_report["undocumented_footprints"].append(
                                f"[{rel_path}] Function '{match.group(1)}()' lacks an explicit specification definition."
                            )

                        # Line-by-line inspection for structural markers
                        for line_num, line in enumerate(lines, 1):
                            todo_match = self.scanners["TODO_MARKERS"].search(line)
                            if todo_match:
                                gap_report["critical_todos"].append(
                                    f"[{rel_path}:Line {line_num}] Unresolved {todo_match.group(1).upper()}: {todo_match.group(2).strip()}"
                                )

                            ambig_match = self.scanners["AMBIGUITY_MARKERS"].search(line)
                            if ambig_match:
                                gap_report["architectural_ambiguities"].append(
                                    f"[{rel_path}:Line {line_num}] Ambiguity token '{ambig_match.group(1)}' exposes an IP vulnerability."
                                )

                    except Exception:
                        # Fail cautiously to protect system runtime stability
                        continue

        return gap_report

    def output_socratic_briefing(self, report: Dict[str, List[str]]):
        """Compiles the gap-analysis metrics into an actionable engineering overview."""
        print("\n==================================================================")
        print("   AUTOSCRIBE PROACTIVE SOCRATIC INTERROGATION REPORT (ASC-004)   ")
        print("==================================================================")
        print(f" Root Directory Target: {self.workspace_dir}")

        total_gaps = sum(len(v) for v in report.values())
        print(f" Ecosystem Health:      {total_gaps} Structural Blind Spots Flagged.\n")

        if report["missing_manifest_assets"]:
            print("❌ MISSED MANIFEST TARGETS (Intent vs Execution Gap):")
            for asset in report["missing_manifest_assets"]:
                print(f"  ├─ {asset}")
            print()

        if report["critical_todos"]:
            print("🛑 CRITICAL ARCHITECTURAL HOLES:")
            for todo in report["critical_todos"][:5]:
                print(f"  ├─ {todo}")
            print()

        if report["architectural_ambiguities"]:
            print("🔶 AMBIGUITY REGISTRY (UNPROTECTED CONCEPTUAL FRAGMENTS):")
            for ambig in report["architectural_ambiguities"][:5]:
                print(f"  ├─ {ambig}")
            print()

        if report["undocumented_footprints"]:
            print("🛰️ UNDOCUMENTED FOOTPRINTS (MISSING PRIOR ART SCAFFOLDING):")
            for doc in report["undocumented_footprints"][:5]:
                print(f"  ├─ {doc}")
            print()

        print("==================================================================")
        print(" SOCRATIC DIRECTIVE: Solve these omissions to eliminate drift.     ")
        print("==================================================================")


if __name__ == "__main__":
    # 1. Run the pre-flight integrity check layer first
    try:
        from integrity_guard import FileSystemIntegrityGuard
        guard = FileSystemIntegrityGuard()
        guard.compile_integrity_briefing()
    except ImportError:
        print("⚠️ Integrity Guard module missing from local workspace path.")

    # 2. Trigger the primary Socratic audit loops
    interrogator = SocraticInterrogatorEngine()
    analysis_results = interrogator.conduct_ecosystem_gap_analysis()
    interrogator.output_socratic_briefing(analysis_results)