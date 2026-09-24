import http.client
import sys

def audit_target_perimeter():
    print("=" * 65)
    print("🛡️ NEXUS CITADEL SECURITY AUDIT: COMPLIANCE ENFORCEMENT ENGINE")
    print("=" * 65)
    
    target_host = "127.0.0.1"
    target_port = 9095  # Targeting your live Nginx edge gateway
    
    print(f"[*] Dispatching validation probes to gateway lane: {target_host}:{target_port}\n")
    
    try:
        conn = http.client.HTTPConnection(target_host, target_port, timeout=5)
        conn.request("GET", "/")
        response = conn.getresponse()
        
        headers = response.getheaders()
        header_dict = {h[0].upper(): h[1] for h in headers}
        
        # 📊 MANDATORY COMPLIANCE CHECKLIST MATRICES
        required_security_headers = [
            "X-FRAME-OPTIONS", 
            "X-CONTENT-TYPE-OPTIONS", 
            "X-XSS-PROTECTION", 
            "CONTENT-SECURITY-POLICY"
        ]
        
        compliance_score = 100
        deduction_weight = 25
        report_lines = []
        
        for rule in required_security_headers:
            if rule in header_dict:
                report_lines.append(f"[✔ PASS] {rule} is actively deployed. Value: {header_dict[rule]}")
            else:
                report_lines.append(f"[🚨 CRITICAL HARDENING VIOLATION] Missing mandatory header rule: {rule}")
                compliance_score -= deduction_weight
                
        print("-" * 65)
        print(f"📋 FINAL SECURITY POSTURE COMPLIANCE SCORE: {compliance_score}%")
        print("-" * 65)
        for log_line in report_lines:
            print(log_line)
            
        # Programmatically write the technical report sheet directly onto the host disk
        with open("security_compliance_report.md", "w", encoding="utf-8") as f:
            f.write(f"# NEXUS CITADEL COMPLIANCE SHEET\n\n## Score: {compliance_score}%\n\n")
            for line in report_lines:
                f.write(f"* {line}\n")
        print("\n[✔ SUCCESS] Hardening report ledger successfully compiled: security_compliance_report.md")
        
    except Exception as e:
        print(f"[❌ AUDIT ABORTED]: Connection failure down target subnet - {str(e)}")

if __name__ == "__main__":
    audit_target_perimeter()
