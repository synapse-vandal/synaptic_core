"""
Project Autoscribe Engine — File System Integrity Guard
Module: integrity_guard.py
Specification Reference: ASC-004-EXT (Pre-Flight Integrity Layer)
Runtime Environment: Pure Python 3.14+ (Zero-Dependency Architecture)
Thread Profile: Single-threaded pre-flight validator (ASIO-Insulated)
"""

import os
import re
from typing import List, Dict, Set

class FileSystemIntegrityGuard:
    def __init__(self):
        """
        Initialises the pre-flight integrity verification layer. 
        Binds the current active workspace directory and default vault layout targets.
        """
        self.workspace_dir = os.getcwd()
        self.expected_manifest_files = {
            "synapse_test.py",
            "sovereign_watcher.py",
            "autoscribe_parser.py",
            "novelty_assessor.py",
            "novelty_hunter.py",
            "socratic_interrogator.py",
            "AUTOSCRIBE_CORE_SPEC.md"
        }
        
        # Malformed extension patterns indicating local tracking anomalies
        self.anomaly_patterns = {
            "DOUBLE_MD": re.compile(r"\.md\.md$", re.IGNORECASE),
            "MARKDOWN_SUFFIX": re.compile(r"\.py\.md$", re.IGNORECASE),
            "DOUBLE_PY": re.compile(r"\.py\.py$", re.IGNORECASE)
        }

    def _execute_fuzzy_search(self, target_filename: str) -> List[str]:
        """Traverses directories fuzzily to locate misnamed or drifted variants of expected assets."""
        found_variants = []
        base_name = os.path.splitext(target_filename)[0]
        
        for root, _, files in os.walk(self.workspace_dir):
            # Skip hidden and environmental directories to protect compute cycles
            if any(part in root for part in [".git", "__pycache__", "VANDAL"]):
                continue
                
            for file in files:
                # Catch if the file contains the base name but has a corrupted extension
                if base_name.lower() in file.lower() and file != target_filename:
                    rel_path = os.path.relpath(os.path.join(root, file), self.workspace_dir)
                    found_variants.append(rel_path)
        return found_variants

    def verify_system_integrity(self) -> Dict:
        """Runs a rigid dual-verification loop checking for missing assets and anomalous extensions."""
        present_files = set(os.listdir(self.workspace_dir))
        missing_assets = self.expected_manifest_files - present_files
        
        report = {
            "integrity_status": "PRISTINE",
            "missing_critical_files": [],
            "detected_extension_anomalies": [],
            "remediation_steps": []
        }

        # 1. Inspect physical directory for raw anomalies
        for root, _, files in os.walk(self.workspace_dir):
            if any(part in root for part in [".git", "__pycache__", "VANDAL"]):
                continue
                
            for file in files:
                file_path = os.path.relpath(os.path.join(root, file), self.workspace_dir)
                
                if self.anomaly_patterns["DOUBLE_MD"].search(file):
                    report["detected_extension_anomalies"].append(f"Double Markdown extension found: [{file_path}]")
                    report["remediation_steps"].append(f"Rename file directly to strip the trailing duplicate extension: {file_path}")
                    
                elif self.anomaly_patterns["MARKDOWN_SUFFIX"].search(file):
                    report["detected_extension_anomalies"].append(f"Executable script trapped with Markdown suffix: [{file_path}]")
                    report["remediation_steps"].append(f"Strip the trailing '.md' extension to allow execution: {file_path}")

        # 2. Process missing targets via fuzzy cross-referencing
        if missing_assets:
            report["integrity_status"] = "COMPROMISED"
            for missing in missing_assets:
                variants = self._execute_fuzzy_search(missing)
                file_log_entry = f"Missing Core File: '{missing}' is absent from the runtime root."
                
                if variants:
                    file_log_entry += f" -> [Fuzzy match located at: {', '.join(variants)}]"
                    report["remediation_steps"].append(
                        f"Bridge file out of vault layout: Copy-Item -Path '{variants[0]}' -Destination '{missing}' -Force"
                    )
                else:
                    report["remediation_steps"].append(
                        f"Initialise missing component template on disk: New-Item -ItemType File -Path '{missing}'"
                    )
                report["missing_critical_files"].append(file_log_entry)

        return report

    def compile_integrity_briefing(self):
        """Compiles integrity matrix tracking statistics directly into the dashboard console."""
        metrics = self.verify_system_integrity()
        
        print("\n==================================================================")
        print("   AUTOSCRIBE FILE SYSTEM INTEGRITY GUARD REPORT (ASC-004-EXT)   ")
        print("==================================================================")
        print(f" Context Path Anchor: {self.workspace_dir}")
        print(f" Integrity Metric:    Ecosystem State is {metrics['integrity_status']}")
        print("==================================================================\n")

        if metrics["missing_critical_files"]:
            print("🚨 CRITICAL FILE CONTEXT DRIFT:')")
            for missing in metrics["missing_critical_files"]:
                print(f"  ├─ {missing}")
            print()

        if metrics["detected_extension_anomalies"]:
            print("🔶 MALFORMED EXTENSION REGISTRY (OBSIDIAN CONFLICTS):")
            for anomaly in metrics["detected_extension_anomalies"]:
                print(f"  ├─ {anomaly}")
            print()

        if metrics["remediation_steps"]:
            print("🔱 PRESCRIBED RECOVERY ACTIONS (MANUAL RUNTIME OVERRIDES):")
            for step in metrics["remediation_steps"]:
                print(f"  ├─ {step}")
            print()
        else:
            print("✅ ZERO DRIFT CONFIRMED: Local storage configuration is pristine.")
            
        print("==================================================================")

if __name__ == "__main__":
    guard = FileSystemIntegrityGuard()
    guard.compile_integrity_briefing()