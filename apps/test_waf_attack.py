import http.client

def attack_perimeter_waf():
    # Route directly to your stable core app port mapping
    conn = http.client.HTTPConnection("127.0.0.1", 8000, timeout=5)
    
    # Simple, clear URL formatting blocks connection refusal loops
    malicious_url = "/api/v1/process/log-parse?id=1%20UNION%20SELECT%20password%20FROM%20users"
    
    print("[*] Launching simulated SQL Injection payload against SaaS Gateway...")
    conn.request("GET", malicious_url)
    res = conn.getresponse()
    
    print(f"\n[+] WAF Response Status Code: {res.status}")
    print(f"[+] Server Response Payload: {res.read().decode()}")
    conn.close()

if __name__ == "__main__":
    attack_perimeter_waf()

