from fastapi import FastAPI, Depends, Request
from database import db_engine

app = FastAPI(title="Nexxus Citadel Backend Engine")

# --- INSTITUTIONAL SECURITY MIDDLEWARE LAYER ---
@app.middleware("http")
async def inject_hardened_security_headers(request: Request, call_next):
    response = await call_next(request)
    
    # Python formatting requires exactly 4 spaces of indentation inside functions
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


