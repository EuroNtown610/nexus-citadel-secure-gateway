import subprocess
import os
import sys

def watch_live_nginx_stream():
    print("=" * 65)
    print("🚨 NEXUS CITADEL ADVANCED SIEM: CONTINUOUS EDGE THREAT RADAR")
    print("=" * 65)
    print("[*] Spawning network intercept socket to 'sd_nginx_edge_proxy'...")
    print("[*] Listening for high-velocity attack campaigns live...\n")

    report_path = "remediation_log.md"
    threat_signatures = ["UNION SELECT", "XMLRPC.PHP", "429", "NIKTO", "DIRB", "WPSCAN"]
    vulnerabilities_found = []

    # ─── 🛡️ THE LOW-LEVEL CONTAINER CONTAINER STREAM HOOK ───
    # Spawns a real-time process listener targeting the NGINX container's stdout loop natively
    cmd = ["docker", "logs", "-f", "--tail", "0", "sd_nginx_edge_proxy"]
    
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        
        for line in iter(process.stdout.readline, ''):
            line_strip = line.strip()
            if not line_strip:
                continue
                
            normalized_line = line_strip.upper()
            threat_detected = False
            
            for sig in threat_signatures:
                if sig in normalized_line:
                    threat_detected = True
                    vulnerabilities_found.append((line_strip, sig))
                    break
            
            if threat_detected:
                # FEATURE 1: EXPLICIT LOG STACK ALERT FOR PROMTAIL / LOKI SIEM MONITORING
                print(f"[🚨 INTERCEPT EVENT] Match Rule: {sig} | Data: {line_strip}", flush=True)
                
                # FEATURE 2: INSTANT LIVE MARKDOWN REMEDIATION REPORT RE-WRITE
                with open(report_path, "a", encoding="utf-8") as report:
                    if os.path.getsize(report_path) == 0 if os.path.exists(report_path) else True:
                        report.write("# 🏛️ Nexxus Citadel Real-Time Perimeter Intrusion Ledger\n\n")
                        report.write("| Real-Time Log Footprint Trace | Rule Signature Violated |\n")
                        report.write("| :--- | :--- |\n")
                    report.write(f"| `{line_strip}` | `{sig}` |\n")
            else:
                print(f"[✔ TRAFFIC CLEAR] {line_strip[:80]}...")
                
    except KeyboardInterrupt:
        print("\n[*] Gracefully disconnecting network tap socket...")
        sys.exit(0)
    except Exception as e:
        print(f"[❌ FATAL PIPELINE EXCEPTION]: {str(e)}")

if __name__ == "__main__":
    watch_live_nginx_stream()
