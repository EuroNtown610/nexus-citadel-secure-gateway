import http.client

def attack_perimeter_waf():
    # Target your live running SaaS Gateway engine
    conn = http.client.HTTPConnection("127.0.0.1", 8001)
    
    # Simulating a highly malicious SQL Injection attack string inside the URL query parameter
    malicious_url = "/api/v1/process/log-parse?id=1%20UNION%20SELECT%20username,password%20FROM%20users"
    headers = {"X-Citadel-Token": "citadel_secret_hash_999"}
    
    print("[*] Launching simulated SQL Injection payload against SaaS Gateway...")
    conn.request("GET", malicious_url, headers=headers)
    res = conn.getresponse()
    
    print(f"\n[+] WAF Response Status Code: {res.status}")
    print(f"[+] Server Response Payload: {res.read().decode()}")
    conn.close()

if __name__ == "__main__":
    attack_perimeter_waf()
