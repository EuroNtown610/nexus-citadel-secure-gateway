import http.client
import urllib.parse

def attack_perimeter_waf():
    # Route directly to your stable core app port mapping
    conn = http.client.HTTPConnection("127.0.0.1", 8000, timeout=5)
    
    # Safe URL formatting targets the exact endpoint route directly
    payload = {"id": "1 UNION SELECT password FROM users"}
    encoded_payload = urllib.parse.urlencode(payload)
    malicious_url = f"/api/v1/process/log-parse?{encoded_payload}"
    
    print("[*] Launching simulated SQL Injection payload against SaaS Gateway...")
    conn.request("GET", malicious_url)
    res = conn.getresponse()
    
    print(f"\n[+] WAF Response Status Code: {res.status}")
    print(f"[+] Server Response Payload: {res.read().decode()}")
    conn.close()

if __name__ == "__main__":
    attack_perimeter_waf()

