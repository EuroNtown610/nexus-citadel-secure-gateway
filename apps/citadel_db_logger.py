import sys
from pymongo import MongoClient

def log_telemetry_to_citadel_vault():
    print("=" * 65)
    print("🍃 LAB 7: MONGODB PERSISTENT LOGGING & SYSTEM INGESTION")
    print("=" * 65)
    
    mongo_uri = "mongodb://sd_mongo_engine:27017"
    print(f"[*] Opening raw database driver connection line to: {mongo_uri}")
    
    try:
        # Standard synchronous client database initialization map layout
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
        db = client.citadel_security_vault
        collection = db.incident_records
        
        mock_incident_payload = {
            "source_ip": "192.168.45.12",
            "target_port": 445,
            "exploit_vector": "/ADMIN/CONFIG.PHP",
            "mitigation_status": "ISOLATED_DROP_GROUP",
            "severity_weight": "CRITICAL"
        }
        
        print("[*] Transmitting raw metric payload data package down database lanes...")
        result = collection.insert_one(mock_incident_payload)
        
        print("-" * 65)
        print(f"[✔ SUCCESS] Incident token successfully logged inside persistent storage!")
        print(f" └─> Database Object Entry ID: {result.inserted_id}")
        print("=" * 65)
        
    except Exception as e:
        print(f"\n[❌ DATABASE INGESTION CRASH]: FAILED TO WRITE PACKET FRAME - {str(e)}")
        print("=" * 65)

if __name__ == "__main__":
    log_telemetry_to_citadel_vault()
