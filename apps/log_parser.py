import time

# A Python list containing nested dictionary logs
server_telemetry_feed = [
    {"timestamp": "2026-09-02 02:10:15", "component": "API_GATEWAY", "status": "INFO", "message": "Uvicorn port 8000 handling incoming GET payload safely."},
    {"timestamp": "2026-09-02 02:11:03", "component": "SECURITY_MIDDLEWARE", "status": "CRITICAL", "message": "Missing content-security-policy header detected on outbound transmission."},
    {"timestamp": "2026-09-02 02:12:45", "component": "DATABASE_POOL", "status": "INFO", "message": "Asynchronous connection pool verified. 14 available sockets active."},
    {"timestamp": "2026-09-02 02:14:22", "component": "PERIMETER_SCANNER", "status": "CRITICAL", "message": "DIRB brute-force tool attempting dictionary traversal attack on route /docs."}
]

def execute_security_log_sweep():
    print("[*] Initializing automated infrastructure alert parsing sequence...")
    time.sleep(1) # Simulates a 1-second system hardware delay
    
    critical_incident_count = 0
    
    print("\n================== SECURITY ALERTS IDENTIFIED ==================")
    
    # The Core Parsing Loop
    for log_entry in server_telemetry_feed:
        # Check if the 'status' key inside the current dictionary matches our metric
        if log_entry["status"] == "CRITICAL":
            critical_incident_count += 1
            print(f"[⚠️ LAUNCH THREAT] Component: {log_entry['component']}")
            print(f"    Time:    {log_entry['timestamp']}")
            print(f"    Details: {log_entry['message']}\n")
            
    print("================================================================")
    print(f"[✔] Parsing sequence complete. Total critical liabilities isolated: {critical_incident_count}")

if __name__ == "__main__":
    execute_security_log_sweep()
