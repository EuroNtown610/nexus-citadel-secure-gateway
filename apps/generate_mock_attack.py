import os
import time

LOG_FILE_PATH = "./logs/production_traffic.log"

def inject_mock_security_events():
    """
    Intentionally injects high-trigger attack patterns into the active 
    log path to validate our automated parser's alert accuracy.
    """
    # Ensure logs directory exists natively
    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
    
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Establish a list of standard exploitation footprint logs
    mock_events = [
        f'[INFO] {timestamp} - Route: "/index.html" - Latency: 12ms - Origin: 192.168.1.100\n',
        f'[WARNING] {timestamp} - Route: "/api/v1/user/1005/invoice" - Latency: 1850ms - Origin: 185.220.101.5\n',
        f'[CRITICAL] {timestamp} - Route: "/admin/config" - Latency: 42ms - Origin: 45.33.22.11 - Exploit: "Nikto Automated Scanner Verified"\n'
    ]
    
    print("[*] Launching target simulation loop...")
    with open(LOG_FILE_PATH, "a") as log_file:
        for event in mock_events:
            log_file.write(event)
            print(f"[+] Injected Mock Event Stream: {event.strip()}")
            time.sleep(0.5) # Simulates natural incoming packet velocity
            
    print("[✔] Mock security injections completed successfully.")

if __name__ == "__main__":
    inject_mock_security_events()
