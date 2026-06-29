
"""
Project Sovereign Sandbox — Ecosystem Tracking Daemon
Module: sovereign_watcher.py
Runtime: Pure Python 3.14+ (Zero-Dependency Architecture)
Thread Profile: Single-threaded lazy-polling loop (ASIO-Insulated)
"""

import os
import subprocess
import time
import sys
from datetime import datetime

class SovereignWatcher:
    def __init__(self, check_interval_seconds: int = 10):
        self.interval = check_interval_seconds
        # Automatically detect the workspace directory this script lives in
        self.workspace_dir = os.path.dirname(os.path.abspath(__file__))
        
    def _execute_git_command(self, args: list) -> str:
        """Executes a system Git command natively within the workspace path."""
        try:
            result = subprocess.run(
                ["git"] + args,
                cwd=self.workspace_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"ERROR: {e.stderr.strip()}"
        except FileNotFoundError:
            return "ERROR: Git binary not detected in system path."

    def evaluate_sync_state(self):
        """Performs a forensic sweep of local and cloud repository synchronization status."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[{timestamp}] Runing ecosystem synchronization audit...")

        # 1. Fetch latest changes from the cloud remote without modifying local files
        fetch_status = self._execute_git_command(["fetch", "origin"])
        if "ERROR" in fetch_status:
            print(f" ⚠️  Cloud Handshake Failed: Offline or Repository URL invalid.")
            return

        # 2. Check for local modifications (uncommitted changes)
        status_porcelain = self._execute_git_command(["status", "--porcelain"])
        
        # 3. Compare local timeline branch position against the cloud origin branch
        local_branch = self._execute_git_command(["rev-parse", "--abbrev-ref", "HEAD"])
        tracking_status = self._execute_git_command(["rev-parse", f"@{'{u}'}"]) # Queries upstream tracking branch
        
        # Determine tracking differences mathematically
        local_hash = self._execute_git_command(["rev-parse", "HEAD"])
        remote_hash = self._execute_git_command(["rev-parse", f"origin/{local_branch}"])

        print(f" -> Active Project Lane: [PROJ_LANE: {local_branch.upper()}]")
        print(f" -> Local Root Location: {self.workspace_dir}")

        # 4. Process State Combinations
        if status_porcelain:
            print(" 🛑 STATE: LOCAL DRIFT DETECTED (Uncommitted changes exist)")
            lines = status_porcelain.split("\n")
            for line in lines:
                print(f"    ├─ File Modified: {line.strip()}")
            print(" -> Action Required: Execute 'Phaze:Sync' or stage changes via VS Code Source Control.")
        else:
            print("  State Check: Local working directory is pristine and stable.")

        if local_hash == remote_hash:
            if not status_porcelain:
                print(" ✅ SYSTEM METRIC: PERFECT SYNC (1:1 Mirror Confirmation)")
                print("    Cloud ledger and local storage are structurally identical.")
            else:
                print(" 🛟 SYSTEM METRIC: Cloud ledger matches your last committed local block.")
        else:
            # Check if local is ahead or behind
            base_check = self._execute_git_command(["merge-base", "HEAD", f"origin/{local_branch}"])
            if base_check == remote_hash:
                print(" ⬆️  STATE: PRIOR ART DELAY (Local commits are ahead of Cloud Moat)")
                print("    Your changes are safely saved locally, but not pushed to GitHub.")
                print("    -> Action Required: Click 'Sync Changes' or run 'git push' to arm public prior art.")
            elif base_check == local_hash:
                print(" ⬇️  STATE: COGNITIVE AMNESIA WARNING (Behind Cloud Origin)")
                print("    The cloud repository contains tracking blocks missing from this machine.")
                print("    -> Action Required: Run 'git pull' to update local files.")
            else:
                print(" ⚠️  STATE: TIMELINE DIVERGENCE (Branches have split tracks)")

    def start_daemon(self):
        """Launches the infinite lazy-polling loop."""
        print("==================================================================")
        print(" INITIALISING SOVEREIGN WATCHER BACKGROUND DAEMON")
        print(f" Throttling Governor Active: Polling frequency set to {self.interval}s")
        print(" Real-time ASIO audio graph safety ceiling: INSULATED")
        print("==================================================================")
        
        try:
            while True:
                self.evaluate_sync_state()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("\n[Watcher Daemon] Shutdown sequence triggered cleanly. Tracking suspended.")

if __name__ == "__main__":
    # Initialise the daemon loop with a relaxed 10-second sleep pattern to keep CPU usage at ~0.0%
    watcher = SovereignWatcher(check_interval_seconds=10)
    watcher.start_daemon()