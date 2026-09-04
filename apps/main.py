from fastapi import FastAPI, HTTPException, Request
import re
import time

app = FastAPI(title="Nexus Citadel Hardened API Gateway & WAF")

RATE_LIMIT_STORE = {}
MAX_REQUEST_THRESHOLD = 5  
TIME_WINDOW_SECONDS = 10

SQL_INJECTION_PATTERN = re.compile(r"UNION\s+SELECT|SELECT\s+.*\s+FROM|OR\s+['\"]?\d+['\"]?\s*=\s*['\"]?\d+", re.IGNORECASE)

@app.get("/api/v1/process/log-parse")
async def commercial_log_parse_endpoint(request: Request):
    client_ip = request.client.host if request.client else "127.0.0.1"
    query_string = request.url.query if request.url.query else ""
    
    # ─── 🛡️ DEEP PACKET QUERIES MATRIX CHECK ───
    if SQL_INJECTION_PATTERN.search(query_string) or "UNION" in query_string.upper():
        print(f"\n[🚨 WAF ALARM] PERIMETER BREACH INTERCEPTED FROM IP: {client_ip}!")
        raise HTTPException(
            status_code=403,
            detail="Security Incident Mitigation: Malicious payload string detected matching signature [SQL_Injection]."
        )

    # ─── 🤖 STABLE RATE-LIMITER ───
    api_token = request.headers.get("X-Citadel-Token")
    if not api_token:
        raise HTTPException(
            status_code=401,
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
            status_code=429,
            detail=f"BRUTE-FORCE MITIGATION: Request limit exceeded ({MAX_REQUEST_THRESHOLD} hits/10s). Account throttled."
        )

    RATE_LIMIT_STORE[api_token].append(current_timestamp)

    return {
        "execution_state": "SUCCESS",
        "service": "Log Parsing Engine",
        "processed_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }