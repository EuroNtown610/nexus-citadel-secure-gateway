import os

def hunting_incident_matrix():
    print("=" * 65)
    print("⚔️ LAB 6 INDEPENDENT THREAT HUNTING: AUTOMATED INCIDENT RESPONSE")
    print("=" * 65)
    
    nginx_mock_logs = [
        "172.18.0.7 - [25/Sep/2026] - GET /index.html HTTP/1.1 - 200",
        "192.168.45.12 - [25/Sep/2026] - GET /admin/config.php HTTP/1.1 - 403",
        "172.18.0.15 - [25/Sep/2026] - POST /api/v1/health HTTP/1.1 - 200",
        "10.0.99.4 - [25/Sep/2026] - GET /wp-login.php HTTP/1.1 - 200"
    ]
    
    threat_signatures = ["/ADMIN/CONFIG.PHP", "/WP-LOGIN.PHP"]
    flagged_alerts = []
    
    print("[*] Commencing automated log stream correlation analysis...\n")
    
    for log in nginx_mock_logs:
        normalized_entry = log.upper()
        for signature in threat_signatures:
            if signature in normalized_entry:
                log_segments = log.split(" - ")
                offending_ip = log_segments[0]
                target_route = log_segments[2]
                
                flagged_alerts.append({
                    "attacker": offending_ip,
                    "exploit_vector": target_route
                })
                
    if flagged_alerts:
        print(f"[🚨 MITIGATION CRITERIA MATCHED] {len(flagged_alerts)} anomalous indicators identified!")
        print("-" * 65)
        for alert in flagged_alerts:
            print(f" -> ATTACKER SOURCE IP: {alert['attacker']}")
            print(f" -> EXPLOIT VECTOR ENCOUNTERED: {alert['exploit_vector']}")
            print(f" [✔ DEFENSE ACTION] Appending host node to permanent drop list network groups.\n")
    else:
        print("[✔ CODE OK] Log telemetry loops clear of known operational threat vectors.")
    print("=" * 65)

if __name__ == "__main__":
    hunting_incident_matrix()
