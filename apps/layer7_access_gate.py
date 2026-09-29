import sys

# 1. Define custom resusable console UI decoration banners
def print_divider():
    print("=" * 32)

# 2. Configure our secure Layer-7 whitelist matrix definitions
AUTHORIZED_CLIENT_AGENT = "CitadelCoreApp/v1.0"
incoming_request_payload = {
    "ip": "172.18.0.5",
    "user-agent": "MaliciousPythonBot/v2.4",
    "path": "/api/v1/data"
}

print_divider()
print(" LAB 16: LAYER-7 ACCESS CONTROL GATING")
print_divider()

# 3Request Header Verification Gate: Audit user-agent signatures
if incoming_request_payload["user-agent"] == AUTHORIZED_CLIENT_AGENT:
    print("[ACESS PASS] Client request matches authorized signature profile.")
    print("Routing transaction frame directly to backend databases.")
else:
    print("[GATING ALERT] Unauthorized Layer-7 User-Agent intercepted!")
    print("COUNTERMEASURE: Dropping packets and dropping session from IP: " + incoming_request_payload["ip"])

print_divider()