from fastapi import Request, Response
from fastapi.responses import JSONResponse
import starlette.middleware.base

class CitadelScannerMitigationMiddleware(starlette.middleware.base.BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Extract the inbound request User-Agent parameter signature
        user_agent = request.headers.get("user-agent", "").upper()
        
        # 🚨 THE FREELANCE ANTI-FUZZER SIGNATURE RADAR
        # Instantly isolates automated scanners (sqlmap, nikto, wpscan) by fingerprint
        malicious_scanners = ["SQLMAP", "NIKTO", "WPSCAN", "DIRB", "DIRBUSTER"]
        
        if any(scanner in user_agent for scanner in malicious_scanners):
            print(f"\n[🚨 ANTI-INTRUSION ALARM] Automated attack engine blocked natively!")
            print(f" -> Isolated Signature: {user_agent}")
            print(f" -> Action Enforced: Immediate backend socket termination.")
            
            # Return an ironclad administrative custom drop block
            return JSONResponse(
                status_code=403,
                content={"detail": "SECURITY ENFORCEMENT: Automated scanning behaviors are strictly prohibited on this grid."}
            )
            
        # If the request traffic pattern is clean, pass it smoothly to the application logic
        response = await call_next(request)
        return response
