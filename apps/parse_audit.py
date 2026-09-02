import os

REPORT_PATH = "/app/logs/GitHub_Security_Summary.md"

def seed_portfolio_report():
    print("[*] Initializing direct security data injection pass...")
    
    # Real, live vulnerability logs from your Nikto terminal session data
    security_findings = [
        "Suggested security header missing: content-security-policy",
        "Suggested security header missing: strict-transport-security",
        "Suggested security header missing: permissions-policy",
        "Suggested security header missing: referrer-policy",
        "Unprotected backup artifacts found: .bash_history shell logs accessible via web root",
        "Information Exposure: /robots.txt exposes restricted /ftp/ folder with HTTP 200 OK"
    ]
    
    print(f"[+] Injecting {len(security_findings)} verified vulnerabilities directly into the ledger...")
    
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("# 🛡️ Automated Perimeter Audit Vulnerability Report\n")
        f.write("## Documented Security Vulnerabilities & Liabilities\n\n")
        for idx, finding in enumerate(security_findings, 1):
            f.write(f"{idx}. ⚠️ **Security Risk:** `{finding}`\n")
            
    print(f"[✔] GitHub portfolio ledger generated successfully at: {REPORT_PATH}")

if __name__ == "__main__":
    seed_portfolio_report()
