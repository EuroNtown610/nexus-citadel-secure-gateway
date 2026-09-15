import http.client
import sys

def attack_perimeter_waf():
    print("=" * 65)
    print("⚔️ NEXUS CITADEL ATTACK SIMULATOR: PERIMETER EXPLORATION STRIKE")
    print("=" * 65)
    print("[*] Target Node: NGINX Edge Proxy (127.0.0.1:8080)")
    print("[*] Launching high-velocity malicious SQL injection payloads...\n")

    # 🚨 FIXED: Explicitly targeting your open public gateway port
    target_host = "127.0.0.1"
    target_port = 8080

    # Malicious injection string that triggers your WAF signatures perfectly
    malicious_url = "/api/v1/process/log-parse?id=1%20UNION%20SELECT%20username,password%20FROM%20users"

    try:
        # Loop 3 times to explicitly pass the WAF threshold block parameters
        for strike in range(1, 4):
            print(f"[+] Launching Payload Injection Wave #{strike:02d}...")
            conn = http.client.HTTPConnection(target_host, target_port, timeout=5)
            conn.request("GET", malicious_url)
            res = conn.getresponse()
            
            print(f" └─> Server Response: {res.status} {res.reason}")
            res.read() # Clear transmission buffers cleanly
            conn.close()
            
        print("\n[✔] Attack campaign execution complete.")
        
    except Exception as e:
        print(f"[❌ FATAL TARGET CONNECTION FAILURE]: {str(e)}")
        print(" -> Verify your 'sd_nginx_edge_proxy' container is actively running on port 8080.")

if __name__ == "__main__":
    attack_perimeter_waf()

