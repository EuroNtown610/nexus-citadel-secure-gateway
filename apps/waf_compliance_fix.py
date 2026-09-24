import os
import sys

def execute_perimeter_hardening_injection():
    print("=" * 65)
    print("⚡ NEXUS CITADEL ADD-ON UTILITY: HARDENING HEADER FIX ENGINE")
    print("=" * 65)
    
    config_path = r"C:\Users\Anthony Frazier\OneDrive\Desktop\sd-workspace\nginx-config\default.conf"
    
    if not os.path.exists(config_path):
        print(f"[❌ ERROR] Target Nginx configuration file not found at: {config_path}")
        return

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            content = f.read()

        # ─── 🛡️ THE ENTERPRISE HARDENING INJECTION ARRAYS ───
        hsts_directive = '    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;\n'
        csp_directive = "    add_header Content-Security-Policy \"default-src 'self' http: https: data: blob: 'unsafe-inline'\" always;\n"
        
        modifications_made = False
        
        # Inject production-grade HSTS parameters programmatically if missing
        if "Strict-Transport-Security" not in content:
            print("[*] Strict-Transport-Security (HSTS) target entry missing. Injecting dynamic parameters...")
            content = content.replace("server {", f"server {{\n{hsts_directive}", 1)
            modifications_made = True
            
        # Inject standard CSP matrices if missing
        if "Content-Security-Policy" not in content:
            print("[*] Content-Security-Policy (CSP) target validation layer missing. Injecting blocks...")
            content = content.replace("server {", f"server {{\n{csp_directive}", 1)
            modifications_made = True

        if modifications_made:
            with open(config_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("\n[✔ SUCCESS] Security framework directives successfully merged into configuration lines!")
        else:
            print("\n[✔ CHECK COMPLETE] Configuration already carries optimal production security parameters.")

    except Exception as e:
        print(f"[❌ FATAL PIPELINE EXCEPTION]: {str(e)}")

if __name__ == "__main__":
    execute_perimeter_hardening_injection()
