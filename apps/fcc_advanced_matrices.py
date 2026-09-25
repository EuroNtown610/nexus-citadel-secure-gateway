def analyze_multi_dimensional_telemetry():
    print("=" * 65)
    print("🛰️ freeCodeCamp ADVANCED: MULTI-DIMENSIONAL SYSTEM MATRIX")
    print("=" * 65)
    
    # 📚 freeCodeCamp core concept: Multi-Dimensional Array (Nested Data Lists)
    # Structure Matrix: [Host IP, Destination Port, Payload Size in MB, Transaction Status]
    system_traffic_matrix = [
        ["172.18.0.4", 445, 120.5, "SUCCESS"],
        ["172.18.0.7", 80, 15.2, "DENIED"],
        ["172.18.0.15", 445, 450.8, "SUCCESS"],
        ["172.18.0.22", 8080, 0.0, "TIMEOUT"],
        ["172.18.0.15", 445, 88.3, "SUCCESS"]
    ]
    
    total_data_transferred = 0.0
    successful_connections_count = 0
    monitored_ips = []
    
    print("[*] Iterating through system data frames...\n")
    
    # 📚 freeCodeCamp core concept: Nested Element Extraction & Arithmetic Iteration Loops
    for session in system_traffic_matrix:
        ip_address = session[0]
        port = session[1]
        data_weight = session[2]
        status = session[3]
        
        if status == "SUCCESS" and port == 445:
            successful_connections_count += 1
            total_data_transferred += data_weight
            
            # Avoid repeating host IPs inside our status matrix list tracker
            if ip_address not in monitored_ips:
                monitored_ips.append(ip_address)
                
    print("-" * 65)
    print(f"[✔] Total Verified Samba Sessions: {successful_connections_count}")
    print(f"[✔] Total Volume Data Extracted: {total_data_transferred:.2f} MB")
    print(f"[✔] Target Node Source Inventory: {monitored_ips}")
    print("=" * 65)

if __name__ == "__main__":
    analyze_multi_dimensional_telemetry()
