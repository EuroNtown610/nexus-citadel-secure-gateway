import sys
import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from apps.security_middleware import CitadelScannerMitigationMiddleware

app = FastAPI(title="Nexus Citadel Sovereign Reserve Gateway")
app.add_middleware(CitadelScannerMitigationMiddleware)

@app.get("/", response_class=HTMLResponse)
def serve_citadel_matrix_dashboard():
    # 🚨 ANTHONY'S CUSTOM ARCHITECT LANDING DECK NATIVE HTML INJECTION
    return """
    <html>
        <head>
            <title>NEXUS CITADEL CORE</title>
            <style>
                body { background-color: #0d1117; color: #00ff66; font-family: 'Courier New', monospace; padding: 50px; }
                h1 { border-bottom: 2px solid #00ff66; padding-bottom: 10px; color: #ffffff; text-shadow: 0 0 10px #00ff66; }
                .grid-status { background-color: #161b22; padding: 20px; border-radius: 5px; border: 1px solid #30363d; margin-top: 20px; }
                .pulse { animation: blinker 1.5s linear infinite; color: #ff3333; font-weight: bold; }
                @keyframes blinker { 50% { opacity: 0; } }
            </style>
        </head>
        <body>
            <h1>🏛️ SECURE DATA DEFENSE MATRIX HUB</h1>
            <div class="grid-status">
                <p><strong>[SYSTEM STATUS]</strong> <span style="color: #00ff66;">ONLINE // AIR-GAPPED SECURE</span></p>
                <p><strong>[INFRASTRUCTURE FLEET]</strong> 19 Active Containers Running Mesh Subnets</p>
                <p><strong>[WAF SHIELD INJECTION]</strong> ModSecurity Core Rule Sets Engaged</p>
                <p><strong>[SD PAINTER WORKER]</strong> <span class="pulse">STANDBY // AUDITING BACKEND THREAT METRICS</span></p>
            </div>
        </body>
    </html>
    """

@app.get("/api/v1/health")
def system_health_check():
    return {"status": "ONLINE", "mesh": "STABLE", "middleware": "ACTIVE"}





