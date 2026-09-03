from fastapi import FastAPI, Depends, HTTPException, Header, Request, status
import re
import time

app = FastAPI(title="Nexus Citadel Hardened API Gateway & WAF")

RATE_LIMIT_STORE = {}
MAX_REQUEST_THRESHOLD = 5  
TIME_WINDOW_SECONDS = 10

# Hardened Regex Traps
SQL_INJECTION_PATTERN = re.compile(r"UNION\s+SELECT|SELECT\s+.*\s+FROM|OR\s+['\"]?\d+['\"]?\s*=\s*['\"]?\d+", re.IGNORECASE)

def verify_perimeter_security(request: Request, x_citadel_token: str = Header(None)):
    # ─── 🛡️ STEP 1: PARSE LIVE QUERY PARAMS SAFELY TO PREVENT NONE-TYPE CRASHES ───
    query_string = request.url.query if request.url.query else ""
    
    # Run deep packet inspection on the un-parsed query string to catch URL spaces
    if SQL_INJECTION_PATTERN.search(query_string) or "UNION" in query_string.upper():
        print(f"\n[🚨 WAF ALARM] MALICIOUS PARAMETER INTERCEPTED NATIVELY!")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Security Incident Mitigation: Malicious payload string detected matching signature [SQL_Injection]."
        )

    # ─── 🤖 STEP 2: MULTI-TENANT TOKEN RATE-LIMITER ───
    api_token = x_citadel_token
    if not api_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="ACCESS DENIED: Missing X-Citadel-Token initialization key."
        )

    current_timestamp = time.time()
    if api_token not in RATE_LIMIT_STORE:
        RATE_LIMIT_STORE[api_token] = []

    RATE_LIMIT_STORE[api_token] = [
        t for t in RATE_LIMIT_STORE[api_token] if current_timestamp - t < TIME_WINDOW_SECONDS
    ]

    if len(RATE_LIMIT_STORE[api_token]) >= MAX_REQUEST_THRESHOLD:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"BRUTE-FORCE MITIGATION: Request limit exceeded ({MAX_REQUEST_THRESHOLD} hits/10s). Account throttled."
        )

    RATE_LIMIT_STORE[api_token].append(current_timestamp)

@app.get("/api/v1/process/log-parse")
async def commercial_log_parse_endpoint(dependencies=Depends(verify_perimeter_security)):
    return {
        "status": "SUCCESS",
        "service": "Log Parsing Engine",
        "processed_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }
