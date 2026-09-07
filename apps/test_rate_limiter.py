import http.client

def simulate_brute_force_spray():
    print("[*] Launching high-velocity token spray (10 requests)...")
    
    for i in range(1, 11):
        try:
            conn = http.client.HTTPConnection("127.0.0.1", 8080, timeout=3)
            url = "/api/v1/process/log-parse?id=rate_check&token=citadel_secret_hash_999"
            conn.request("GET", url)
            res = conn.getresponse()
            print(f"Request {i:02d} -> Status Code: {res.status} | Payload: {res.read().decode()}")
            conn.close()
        except Exception as e:
            print(f"Request {i:02d} -> Transport Error: {str(e)}")

if __name__ == "__main__":
    simulate_brute_force_spray()
