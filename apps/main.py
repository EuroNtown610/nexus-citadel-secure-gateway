from fastapi import FastAPI, HTTPException

app = FastAPI(title="Nexus Citadel Hardened API Gateway & WAF")

@app.get("/api/v1/process/log-parse")
def commercial_log_parse_endpoint(id: str = ""):
    # ─── 🛡️ THE BULLETPROOF STRING INSPECTION FILTER ───
    if "UNION" in id.upper() and "SELECT" in id.upper():
        print(f"\n[🚨 WAF ALARM] MALICIOUS PARAMETER INTERCEPTED NATIVELY! Payload: {id}", flush=True)
        raise HTTPException(
            status_code=403,
            detail="Security Incident Mitigation: Malicious payload string detected matching signature [SQL_Injection]."
        )
        
    return {
        "execution_state": "SUCCESS",
        "service": "Log Parsing Engine"
    }


