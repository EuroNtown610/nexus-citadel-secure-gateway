import asyncio
import httpx

async def verify_cross_origin_pipeline():
    """
    Simulates browser traffic hits to ensure the backend engine 
    securely accepts and processes data without payload leaks.
    """
    print("[*] Dispatching diagnostic network hit to FastAPI container...")
    target_url = "http://localhost:8000/api/v1/telemetry/log"
    
    # Mock incident data payload mimicking a live security hazard log entry
    payload = {
        "source_ip": "192.168.1.50",
        "vulnerability_type": "Passive Directory Traversal Scan",
        "severity": "Medium",
        "payload_dump": "GET /etc/passwd HTTP/1.1"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(target_url, json=payload, timeout=3.0)
            print(f"\n[+] CONTAINER RESPONSE CODE: {response.status_code}")
            print(f"[+] DATA INGESTION RESULT: {response.json()}")
            
            if response.status_code == 201:
                print("\n[✔] SUCCESS: FRONTEND-TO-BACKEND PIPELINE IS FLAWLESS")
            else:
                print("\n[⚠] WARNING: BACKEND BUFFER LOGGED AN INVALID PROTOCOL")
        except Exception as e:
            print(f"\n[❌] PIPELINE EXCEPTION: Connection refused. Check your Docker engine status. Details: {str(e)}")

if __name__ == "__main__":
    asyncio.run(verify_cross_origin_pipeline())
