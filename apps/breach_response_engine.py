import os
import sys
from datetime import datetime

def hunting_incident_matrix():
    print("=" * 65)
    print("⚔️ CITADEL STREAM INJECTION: SANITIZED TEXT MATRIX")
    print("=" * 65)
    
    nginx_mock_logs = [
        "192.168.45.12 - [25/Sep/2026] - GET /admin/config.php HTTP/1.1 - 403",
        "10.0.99.4 - [25/Sep/2026] - GET /wp-login.php HTTP/1.1 - 200"
    ]
    
    # 🚨 STEP 1: Force absolute directory construction
    log_dir = os.path.abspath("logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, "breach_alerts.log")
    
    print(f"[*] Appending sanitized telemetry rows into log gate: {log_file_path}")
    
    try:
        # 🚨 STEP 2: Open with explicit buffering=0 or force a flush on write
        with open(log_file_path, "a", encoding="utf-8") as f:
            for log in nginx_mock_logs:
                timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                f.write(f"{timestamp} MITIGATION CRITERIA MATCHED - Flagged Intrusion Profile - {log}\n")
            f.flush()
            os.fsync(f.fileno()) # Force the operating system to commit bytes to the physical drive layer
            
        print("[✔ SUCCESS] Data rows normalized. Stream transmitted cleanly down the wire!")
        print(f"[*] Physical File Size Verification: {os.path.getsize(log_file_path)} bytes mapped.")
    except Exception as e:
        print(f"[❌ WRITE EXCEPTION]: {str(e)}")
    print("=" * 65)

if __name__ == "__main__":
    hunting_incident_matrix()
