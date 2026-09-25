import socket

def run_scanner():
    print("==================================================")
    print("🛰️ CITADEL REAL-TIME DIRECT NETWORK PROBE")
    print("==================================================")
    
    subnet = "172.18.0."
    port = 445
    
    for ip in range(1, 255):
        target_ip = f"{subnet}{ip}"
        print(f"[*] Probing node line: {target_ip}")
        
        # Create a basic low-level TCP socket connection channel
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.15)
        
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"\n[✔ MATCH FOUND] Active Target Share IP: {target_ip}\n")
            
        s.close()

if __name__ == "__main__":
    run_scanner()
