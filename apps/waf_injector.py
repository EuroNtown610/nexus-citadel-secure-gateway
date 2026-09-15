import subprocess
import os
import sys

def execute_active_perimeter_defense():
    nginx_config_path = r"C:\Users\Anthony Frazier\OneDrive\Desktop\sd-workspace\nginx-config\default.conf"
    
    print("=" * 65)
    print("🚨 NEXUS CITADEL ACTIVE MITIGATION: CONTAINER RUNTIME WAF")
    print("=" * 65)
    print("[*] Tapping standard output stream socket for: sd_nginx_edge_proxy")
    print("[*] Monitoring network runtime layers for attack profiles...\n")

    banned_ips = set()
    malicious_activity_log = {}
    malicious_signatures = ["XMLRPC.PHP", "NIKTO", "DIRB", "WPSCAN", "UNION SELECT"]
    TRIGGER_THRESHOLD = 3  # Block the IP after 3 offensive requests

    # ─── 🪓 THE LOW-LEVEL RUNTIME LOG SOCKET STREAM ───
    # Spawns a real-time process listener that intercepts container logs directly from memory
    cmd = ["docker", "logs", "-f", "--tail", "0", "sd_nginx_edge_proxy"]
    
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        
        for line in iter(process.stdout.readline, ''):
            line_strip = line.strip()
            if not line_strip:
                continue
                
            normalized_line = line_strip.upper()
            threat_match = any(sig in normalized_line for sig in malicious_signatures)
            
            if threat_match:
                parts = line_strip.split()
                if not parts:
                    continue
                
                # Extract index 0 to grab the clean IP address string directly
                attacker_ip = parts[0]
                
                if attacker_ip in banned_ips:
                    continue
                    
                if attacker_ip not in malicious_activity_log:
                    malicious_activity_log[attacker_ip] = 0
                    
                malicious_activity_log[attacker_ip] += 1
                print(f"[⚠️ WARNING] Suspicious payload from {attacker_ip} | Hits: {malicious_activity_log[attacker_ip]}/{TRIGGER_THRESHOLD}", flush=True)
                
                # ─── 🪓 AUTOMATED ACTIVE WAN DROPS ───
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
