from fastapi import FastAPI, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
import os
import time

app = FastAPI(title="Shield & Scale Enterprise Engine")

# --- ASYNCHRONOUS DATABASE CONNECTION POOL CONFIGURATION ---
MONGO_URI = os.getenv("MONGO_URI", "mongodb://db_admin_user:SecureVaultPassword2026!@database-core:27017")

class DatabaseClientManager:
    """Manages an isolated, persistent asynchronous connection pool to MongoDB."""
    def __init__(self):
        self.client: AsyncIOMotorClient = None
        self.db = None

    def connect(self):
        # Establish an active pool size that handles concurrency safely without memory leaks
        self.client = AsyncIOMotorClient(
            MONGO_URI, 
            maxPoolSize=50, 
            minPoolSize=10,
            maxIdleTimeMS=10000
        )
        self.db = self.client["production_data_ledger"]

    def disconnect(self):
        if self.client:
            self.client.close()

db_manager = DatabaseClientManager()

# Native lifespan lifecycle events to preserve system memory boundaries
@app.on_event("startup")
async def startup_event():
    db_manager.connect()

@app.on_event("shutdown")
async def shutdown_event():
    db_manager.disconnect()

# --- SECURITY SCHEMAS ---
class SecurityLogEntry(BaseModel):
    source_ip: str = Field(..., example="127.0.0.1")
    vulnerability_type: str = Field(..., example="BOLA Endpoint Leak")
    severity: str = Field(..., example="High")
    payload_dump: str

# Dependency Injection pattern to pull database context safely without leaks
async def get_database_context():
    return db_manager.db

@app.post("/api/v1/telemetry/log", status_code=201)
async def ingest_security_incident(entry: SecurityLogEntry, db = Depends(get_database_context)):
    """
    Ingests live application perimeter traffic data asynchronously 
    without causing background thread blocking.
    """
    start_time = time.time()
    try:
        # Non-blocking async database injection
        result = await db.incidents.insert_one(entry.dict())
        execution_latency = (time.time() - start_time) * 1000
        
        return {
            "status": "INGESTED",
            "record_id": str(result.inserted_id),
            "telemetry_latency_ms": round(execution_latency, 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database pipeline failure: {str(e)}")
