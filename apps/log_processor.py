import time
import re
import os

# Define local structural workspace path paths
LOG_FILE_PATH = "/var/log/app/production_traffic.log"
ALERT_OUTPUT_PATH = "/workspace/security_alerts.md"

def monitor_live_application_traffic():
    """
    Actively tracks data logs in real-time, pulling raw connection metrics 
    and outputting clear, actionable client data ledgers.
    """
    print("[*] Diagnostic Ledger Monitoring Active. Listening for live system traffic...")
    
    # Initialize basic log file infrastructure if missing
    if not os.path.exists(LOG_FILE_PATH):
        os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
        with open(LOG_FILE_PATH, "w") as f:
            f.write("--- LOG ENGINE INITIALIZED ---\n")

    # Lock into the active file stream end
    with open(LOG_FILE_PATH, "r") as file:
        file.seek(0, os.SEEK_END)
        
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1) # Prevents system processor burnouts
                continue
                
            # Print live container routing events straight to terminal view
            print(f"[LIVE TRAFFIC] {line.strip()}")
            
            # Automated High-Trigger Hazard Parsing
            if "nikto" in line.lower() or "nmap" in line.lower() or "404" in line:
                log_perimeter_alert(line)

def log_perimeter_alert(raw_log_entry):
    """
    Pipes suspicious incoming connections into a clean, client-facing markdown ledger.
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    clean_message = f"*   **[HAZARD DETECTED - {timestamp}]** Pre-exploit automated scanning footprint verified: `{raw_log_entry.strip()}`\n"
    
    # Write directly to the shared security workspace volume
    with open(ALERT_OUTPUT_PATH, "a") as alert_file:
        alert_file.write(clean_message)

if __name__ == "__main__":
    try:
        monitor_live_application_traffic()
    except KeyboardInterrupt:
        print("\n[-] Log telemetry engine shut down cleanly.")
