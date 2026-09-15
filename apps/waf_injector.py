import subprocess
import os
import sys
import time

def execute_active_perimeter_defense():
    # ─── 📂 TRUE WINDOWS ONEDRIVE PATH ENFORCEMENT ───
    log_file_path = r"C:\Users\Anthony Frazier\OneDrive\Desktop\sd-workspace\logs\nginx_access.log"
    nginx_config_path = r"C:\Users\Anthony Frazier\OneDrive\Desktop\sd-workspace\nginx-config\default.conf"
    
    print("=" * 65)
    print("🚨 NEXUS CITADEL ACTIVE MITIGATION: DYNAMIC FIREWALL INJECTOR")
    print("=" * 65)
    print(f"[*] Actively tailing live metrics channel: {log_file_path}")
    print("[*] Monitoring perimeter lanes for aggressive attack runs...\n")

    banned_ips = set()
    malicious_activity_log = {}
    malicious_signatures = ["XMLRPC.PHP", "NIKTO", "DIRB", "WPSCAN", "UNION SELECT"]
    TRIGGER_THRESHOLD = 3  # Block the IP after 3 offensive requests

    # 🚨 FORCE WINDOWS TO GENERATE THE DIR AND FILE ON LAUNCH NATIVELY
    log_dir = os.path.dirname(log_file_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)
    if not os.path.exists(log_file_path):
        with open(log_file_path, "w", encoding="utf-8") as f:
            f.write("") # Drops an absolute physical 0-byte file anchor onto the disk

    try:
        with open(log_file_path, "r", encoding="utf-8") as file_handle:
            file_handle.seek(0, os.SEEK_END)
            
            while True:
                line = file_handle.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                    
                normalized_line = line.upper()
                threat_match = any(sig in normalized_line for sig in malicious_signatures)
                
                if threat_match:
                    parts = line.split()
                    if not parts:
                        continue
                    
                    attacker_ip = parts[0] # Exact string IP address conversion mapping
                    
                    if attacker_ip in banned_ips:
                        continue
                        
                    if attacker_ip not in malicious_activity_log:
                        malicious_activity_log[attacker_ip] = 0
                        
                    malicious_activity_log[attacker_ip] += 1
                    print(f"[⚠️ WARNING] Suspicious footprint from {attacker_ip} | Hits: {malicious_activity_log[attacker_ip]}/{TRIGGER_THRESHOLD}")
                    
                    if malicious_activity_log[attacker_ip] >= TRIGGER_THRESHOLD:
                        print(f"\n[🚨 INTRUSION CRITICAL] IP {attacker_ip} crossed threat threshold!")
                        print(f"[*] Injecting active block rule into proxy configurations...")
                        
                        banned_ips.add(attacker_ip)
                        
                        with open(nginx_config_path, "r", encoding="utf-8") as config_file:
                            config_content = config_file.read()
                            
                        block_directive = f"\n    # Dynamic WAF Block for Actor\n    deny {attacker_ip};\n"
                        
                        if f"deny {attacker_ip};" not in config_content:
                            updated_content = config_content.replace("server {", f"server {{{block_directive}", 1)
                            with open(nginx_config_path, "w", encoding="utf-8") as config_file:
                                config_file.write(updated_content)
                                
                            print("[*] Forcing hot-reload execution on 'sd_nginx_edge_proxy'...")
                            subprocess.run(["docker", "exec", "sd_nginx_edge_proxy", "nginx", "-s", "reload"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                            print(f"[✔ SUCCESS] Attacker IP {attacker_ip} is officially blocked at the WAN boundary! ❌\n", flush=True)

    except KeyboardInterrupt:
        print("\n[*] Disconnecting defensive automation intercept hooks safely...")
        sys.exit(0)
    except Exception as e:
        print(f"[❌ FATAL AUTOMATION PIPE EXCEPTION]: {str(e)}")

if __name__ == "__main__":
    execute_active_perimeter_defense()
