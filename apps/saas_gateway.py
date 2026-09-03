from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import motor.motor_asyncio # FIXED IMPORT LAYOUT: Direct namespace integration
import time

app = FastAPI(title="Nexus Citadel Sovereign API Gateway")

# Direct, unified async database driver initialization
MONGO_URI = "mongodb://sd_mongo_engine:27017"
db_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = db_client.saas_gateway_ledger

RATE_LIMIT_STORE = {}
MAX_REQUEST_THRESHOLD = 5  
TIME_WINDOW_SECONDS = 10

@app.middleware("http")
async def secure_token_and_rate_limiter_middleware(request: Request, call_next):
    api_token = request.headers.get("X-Citadel-Token")
    
    if not api_token:
        return JSONResponse(
            status_code=401,
            content={"detail": "ACCESS DENIED: Missing X-Citadel-Token initialization key."}
        )

    current_timestamp = time.time()
    if api_token not in RATE_LIMIT_STORE:
        RATE_LIMIT_STORE[api_token] = []

    RATE_LIMIT_STORE[api_token] = [
        t for t in RATE_LIMIT_STORE[api_token] if current_timestamp - t < TIME_WINDOW_SECONDS
    ]

    if len(RATE_LIMIT_STORE[api_token]) >= MAX_REQUEST_THRESHOLD:
        return JSONResponse(
            status_code=429,
            content={"detail": f"BRUTE-FORCE MITIGATION: Request limit exceeded ({MAX_REQUEST_THRESHOLD} hits/10s). Account throttled."}
        )

    RATE_LIMIT_STORE[api_token].append(current_timestamp)
    response = await call_next(request)
    return response

@app.get("/api/v1/process/log-parse")
async def commercial_log_parse_endpoint():
    return {
        "status": "SUCCESS",
        "service": "Log Parsing Engine",
        "processed_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }


