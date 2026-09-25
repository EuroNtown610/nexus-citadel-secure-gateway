def process_corporate_telemetry_ledger():
    print("=" * 60)
    print("📚 freeCodeCamp: DATA STREAM LOOP & ARRAY STRING MATCHING")
    print("=" * 60)
    
    connection_log_ledger = [
        "SRC:172.18.0.7 | PORT:445 | STATUS:DENIED",
        "SRC:172.18.0.15 | PORT:445 | STATUS:SUCCESS",
        "SRC:172.18.0.7 | PORT:8080 | STATUS:DENIED",
        "SRC:172.18.0.22 | PORT:445 | STATUS:SUCCESS"
    ]
    
    verified_access_hosts = []
    
    for entry in connection_log_ledger:
        if "STATUS:SUCCESS" in entry:
            parts = entry.split(" | ")
            # 🚨 FIXING DATA STRING REPLACEMENTS
            ip_address = parts[0].replace("SRC:", "")
            port_number = parts[1].replace("PORT:", "")
            
            verified_access_hosts.append(f"Host IP: {ip_address} on open port {port_number}")
            
    print(f"[✔] Total verified access records found: {len(verified_access_hosts)}")
    print("-" * 60)
    for host in verified_access_hosts:
        print(f" -> Active Node: {host}")
    print("=" * 60)

if __name__ == "__main__":
    process_corporate_telemetry_ledger()
