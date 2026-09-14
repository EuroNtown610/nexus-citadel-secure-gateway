import http.client

def audit_production_headers():
    print("[*] Interrogating NGINX Edge Proxy on Port 8080 for security profiles...")
    
    try:
        # Full, untruncated route connects directly to your open host socket channel
        conn = http.client.HTTPConnection("127.0.0.1", 8080, timeout=5)
        conn.request("HEAD", "/")
        res = conn.getresponse()
        
        print(f"\n[+] Connection Established Status: {res.status} {res.reason}")
        print("=" * 50)
        print("LIVE SECURITY HEADER INVENTORY:")
        print("=" * 50)
        
        # Enumerate and print out the raw headers returned by NGINX
        for header, value in res.getheaders():
            if header.lower() in ["server", "x-frame-options", "x-content-type-options", "x-xss-protection", "x-cache-status"]:
                print(f" -> {header}: {value}")
                
        conn.close()
    except Exception as e:
        print(f"[🚨] Transport Error: {str(e)}")

if __name__ == "__main__":
    audit_production_headers()
