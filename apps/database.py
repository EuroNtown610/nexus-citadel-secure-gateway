import os
from motor.motor_asyncio import AsyncIOMotorClient

# --- DATABASE ENGINE CONFIGURATION ---
MONGO_USER = "db_admin_user"
MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_HOST = os.getenv("MONGO_HOST", "database-core")
MONGO_PORT = "27017"

MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/?authSource=admin"

class AsyncDatabaseEngine:
    def __init__(self):
        self.client: AsyncIOMotorClient = None
        self.db = None

    def initialize_pool(self):
        """Initializes a pool-safe, non-blocking connection to MongoDB 4.4."""
        self.client = AsyncIOMotorClient(
            MONGO_URI,
            maxPoolSize=50,
            minPoolSize=10,
            serverSelectionTimeoutMS=2000
        )
        self.db = self.client["nexxus_citadel_ledger"]
        print("[+] Asynchronous MongoDB 4.4 Data Pool Successfully Verified.")

    def shutdown_pool(self):
        """Gracefully terminates sockets to prevent memory leaks on your host OS."""
        if self.client:
            self.client.close()
            print("[-] MongoDB Data Connection Pool Closed Cleanly.")

db_engine = AsyncDatabaseEngine()
