import os

LOG_PATH = "/app/logs/juice_shop_audit.txt"
REPORT_PATH = "/app/logs/GitHub_Security_Summary.md"

def extract_high_severity_liabilities():
    print("[*] Parsing Nikto audit artifacts for high-severity items...")
    
    if not os.path.exists(LOG_PATH):
        print(f"[-] Halt: Source log missing at {LOG_PATH}")
        return

    findings = []
    with open(LOG_PATH, "r") as f:
        for line in f:
            if "missing:" in line.lower() or ".json" in line.lower() or "history" in line.lower():
                findings.append(line.strip())

    print(f"[+] Isolated {len(findings)} critical points. Building GitHub Summary markdown...")
    
    with open(REPORT_PATH, "w") as repo_file:
        repo_file.write("# 🛡️ Automated Perimeter Audit Summary\n")
        repo_file.write(f"**Scan Source:** Node.js Target Infrastructure Cluster  \n")
        repo_file.write(f"**Status:** Analysis Complete  \n\n")
        repo_file.write("## Isolated Vulnerability Ledger\n")
        for idx, finding in enumerate(findings, 1):
            repo_file.write(f"{idx}. ⚠️ **System Liability:** `{finding}`\n")
            
    print(f"[✔] GitHub portfolio asset compiled successfully at: {REPORT_PATH}")

if __name__ == "__main__":
    extract_high_severity_liabilities()
