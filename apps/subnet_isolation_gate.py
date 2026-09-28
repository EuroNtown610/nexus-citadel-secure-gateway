import sys

# 1. Define the internal IP address segments for our air-gapped zones
public_dmz_gateway = "172.18.0.2"
isolated_data_vault = "172.18.0.4"

print("================================")
print("LAB 11: AIR-GAPPED SUBNET ISOLATION GATING")
print("================================")

# 2. Simulate an incoming network packet frame request
incoming_source_ip = "172.18.0.2"
incoming_target_ip = "172.18.0.4"

# 3. Dynamic Firewall LOgic Gate: Evaluate connection Legitimacy
if incoming_source_ip == public_dmz_gateway and incoming_target_ip == isolated_data_vault:
    print("[ACCESS GRANTED] Traffic verified from legal DMZ proxy.")
    print("Forwarding packet frame to isolated storage array.")
else:
    print("[DROP ACTION] Unauthorized cross-subnet connection intercepted!")
    print("Terminating interface session to isolate vault storage.")    