import time

def run_freecodecamp_log_audit():
    print("🎨 [SD PAINTER ENGINE] Commencing background runtime telemetry audit...")
    
    # 📚 freeCodeCamp core concept: Python Lists and Strings Array
    mock_log_lines = [
        "127.0.0.1 - GET /index.html HTTP/1.1 - 200",
        "192.168.1.45 - GET /api/v1/process/log-parse?id=1%20UNION%20SELECT HTTP/1.1 - 403",
        "10.0.0.8 - POST /wp-login.php HTTP/1.1 - 200",
        "172.21.0.14 - GET /xmlrpc.php HTTP/1.1 - 403"
    ]
    
    signatures = ["UNION SELECT", "XMLRPC.PHP", "WP-LOGIN.PHP"]
    isolated_threats = []

    # 📚 freeCodeCamp core concept: Nested Iteration Loops & String Formatting
    for log in mock_log_lines:
        normalized_log = log.upper()
        for threat in signatures:
            if threat in normalized_log:
                # Target threat string isolated cleanly
                parts = log.split(" - ")
                attacker_ip = parts[0]
                payload_details = parts[1]
                
                isolated_threats.append(f"[❌ BREACH ATTEMPT DETECTED] Host: {attacker_ip} | String: {payload_details}")

    # Output the list items programmatically
    for alert in isolated_threats:
        print(alert)
        time.sleep(0.5)

if __name__ == "__main__":
    run_freecodecamp_log_audit()
