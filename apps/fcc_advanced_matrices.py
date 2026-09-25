import sys

def analyze_multi_dimensional_telemetry():
    print("=" * 65)
    print("🛰️ freeCodeCamp HARDENED: MULTI-DIMENSIONAL ERROR EXCEPTION MESH")
    print("=" * 65)
    
    # Dirty corporate log simulation containing type corruption bugs
    system_traffic_matrix = [
        ["172.18.0.4", 445, 120.5, "SUCCESS"],
        ["172.18.0.7", 80, 15.2, "DENIED"],
        ["172.18.0.99", 445, "CORRUPTED_STRING_BUG", "SUCCESS"], # 🚨 Intentional crash vector
        ["172.18.0.15", 445, 450.8, "SUCCESS"],
        ["172.18.0.22", 8080, None, "TIMEOUT"]                     # 🚨 Null element bug
    ]
    
    total_data_transferred = 0.0
    successful_connections_count = 0
    
    print("[*] Parsing network packet fields safely...\n")
    
    for index, session in enumerate(system_traffic_matrix):
        try:
            # 📚 freeCodeCamp Core: Defensive Value Unpacking & Type Casting
            ip, port, data_weight, status = session
            
            if status == "SUCCESS" and port == 445:
                # Force dynamic float casting inside an explicit try block
                parsed_weight = float(data_weight)
                successful_connections_count += 1
                total_data_transferred += parsed_weight
                
        except (ValueError, TypeError) as e:
            # 🛡️ RESILIENCE GATING: Catches anomalies without breaking code loops
            print(f"[🚨 LINE EXCEPTION CAPTURED] Row indexing marker: Index [{index}] carries invalid log parameters.")
            print(f" └─> Trace Exception Details: {str(e)}\n")
            continue
            
    print("-" * 65)
    print(f"[✔ VALIDATED SESSIONS]: {successful_connections_count}")
    print(f"[✔ TOTAL DATA ISOLATED]: {total_data_transferred:.2f} MB")
    print("=" * 65)

if __name__ == "__main__":
    analyze_multi_dimensional_telemetry()
