import os
import sys
import time

# Systemic Lane Context Configuration
TARGET_FILE = r"C:\Users\Martha_Farquhar\Documents\Obsidian Vault\VANDAL\Autoscribe\ASCRB-CORE SPEC.md"
MANIFEST_OUTPUT = r"C:\Users\Martha_Farquhar\Documents\Obsidian Vault\VANDAL\Autoscribe\generated_manifest.py"
MANUAL_OUTPUT = r"C:\Users\Martha_Farquhar\Documents\Obsidian Vault\VANDAL\Autoscribe\USER_MANUAL.md"

def load_file_lines(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()

def calculate_stateless_diff(old_lines, new_lines):
    """ASC-001: Linear token-array comparative differential engine."""
    diff_detected = False
    diff_report = []
    
    # Primitive line matching for low-overhead worker execution
    old_set = set([line.strip() for line in old_lines])
    
    for line in new_lines:
        cleaned = line.strip()
        if cleaned and cleaned not in old_set:
            diff_report.append(f"+ {line.rstrip()}")
            diff_detected = True
            
    return diff_detected, diff_report

def execute_bifurcated_sync(lines):
    """Parses text chunks directly into isolated project destinations."""
    print("\n[Autoscribe Core] Sorting telemetry vectors into parallel lanes...")
    
    manifest_chunks = []
    manual_chunks = []
    
    in_code_block = False
    
    for line in lines:
        if line.startswith("```python"):
            in_code_block = True
            continue
        elif line.startswith("```") and in_code_block:
            in_code_block = False
            continue
            
        if in_code_block:
            manifest_chunks.append(line)
        else:
            manual_chunks.append(line)

    # Write Manifest Code Assets cleanly
    if manifest_chunks:
        with open(MANIFEST_OUTPUT, "w", encoding="utf-8") as f:
            f.writelines(manifest_chunks)
        print(f" -> [MANIFEST UPDATE] Synchronised: {MANIFEST_OUTPUT}")

    # Write Manual Documentation Assets cleanly
    if manual_chunks:
        with open(MANUAL_OUTPUT, "w", encoding="utf-8") as f:
            f.writelines(manual_chunks)
        print(f" -> [MANUAL UPDATE] Synchronised: {MANUAL_OUTPUT}")

def monitor_lane():
    print("[Autoscribe Core] Activating automated cross-talk daemon.")
    print(f"[Autoscribe Core] Monitoring target asset: {TARGET_FILE}")
    print("[Resource Governor] Thread footprint constrained to low-priority loop.")
    
    if not os.path.exists(TARGET_FILE):
        print(f" ERROR: Target path not found. Ensure file exists at {TARGET_FILE}")
        return

    last_mtime = os.path.getmtime(TARGET_FILE)
    cached_lines = load_file_lines(TARGET_FILE)

    try:
        while True:
            # Low-overhead polling tick to insulate real-time ASIO clock graphs
            time.sleep(1.5) 
            
            current_mtime = os.path.getmtime(TARGET_FILE)
            if current_mtime file != last_mtime:
                print("\n[Autoscribe Core] Mutation detected inside target document.")
                current_lines = load_file_lines(TARGET_FILE)
                
                has_changes, diff_data = calculate_stateless_diff(cached_lines, current_lines)
                
                if has_changes:
                    print("\n--- PENDING CHANGES FOR REVIEW ---")
                    for change in diff_data[:15]: # Show first 15 lines max for scannability
                        print(change)
                    if len(diff_data) > 15:
                        print(f"... and {len(diff_data) - 15} more lines.")
                    print("----------------------------------")
                    
                    # Human-in-the-loop execution guardrail
                    user_input = input("[Validation Cascade] Approve synchronization and commit payload? (y/n): ")
                    if user_input.lower().strip() == 'y':
                        execute_bifurcated_sync(current_lines)
                        cached_lines = current_lines
                        print("[Autoscribe Core] Sync completed successfully.")
                    else:
                        print("[Autoscribe Core] Synchronisation aborted by Architect.")
                
                last_mtime = current_mtime
                
    except KeyboardInterrupt:
        print("\n[Autoscribe Core] De-activating daemon. Releasing directory file handles.")

if __name__ == "__main__":
    monitor_lane()