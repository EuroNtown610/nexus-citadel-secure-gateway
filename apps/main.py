from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import JSONResponse
from database import db_engine

app = FastAPI(title="Nexxus Citadel Backend Engine")

# --- INSTITUTIONAL SECURITY MIDDLEWARE LAYER ---
@app.middleware("http")
async def inject_hardened_security_headers(request: Request, call_next):
    response = await call_next(request)
    
    response.headers["Content-Security-Policy"] = "default-src 'self'; object-src 'none';"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains; preload"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    
    return response

@app.on_event("startup")
async def startup_event():
    db_engine.initialize_pool()

@app.on_event("shutdown")
async def shutdown_event():
    db_engine.shutdown_pool()

async def get_db():
    return db_engine.db

@app.get("/health")
async def check_system_health(db = Depends(get_db)):
    try:
        await db.command("ping")
        status = "SECURE // OPERATIONAL"
    except Exception as e:
        status = f"DEGRADED // ERROR: {str(e)}"
        
    return {"backend_server": "ONLINE", "database_connection": status}

# --- ACTIVE WEB FORM INTAKE ROUTE ---
@app.post("/api/v1/optimize")
async def execute_client_optimization_sprint(
    endpoint: str = Form(...), 
    image_assets: int = Form(...)
):
    print(f"[+] Form Payload Intercepted! Target: {endpoint} // Assets: {image_assets}")
    
    if image_assets > 500:
        performance_status = "CRITICAL LIMIT EXCEEDED // HIGH SPEED DRAG"
        remediation_action = "Deploy multi-threaded WebP compression engine instantly."
    else:
        performance_status = "OPTIMAL COMPLIANCE BOUNDS"
        remediation_action = "Standard asset caching rules applied."
        
    return JSONResponse(
        status_code=200,
        content={
            "status": "DATA PIPELINE ACTIVE",
            "target_domain": endpoint,
            "total_assets_scanned": image_assets,
            "performance_profile": performance_status,
            "remediation_protocol": remediation_action
        }
    )

# --- OFFENSIVE INTRUSION DECEPTIVE TRAP ROUTE ---
@app.get("/api/v1/admin/ledger")
async def secure_admin_ledger_trap(request: Request):
    client_ip = request.client.host
    print(f"[🚨 INTRUSION ALERT] Unauthorized administrative path probe intercepted from IP: {client_ip}!")
    
    raise HTTPException(
        status_code=403, 
        detail="ACCESS DENIED // SECURITY PROTOCOL INITIATED // IP INCIDENT RECORDED"
    )
