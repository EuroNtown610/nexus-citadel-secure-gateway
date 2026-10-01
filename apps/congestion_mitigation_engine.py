import sys

# [NEXXUS CITADEL SYSTEMS PROTOCOL 0.1]: UI DECORATION BANNERS
def print_master_border():
    print("=" * 45)

# [NEXXUS CITADEL SYSTEMS PROTOCOL 0.2]: ARCHITECTURE CONFIGURATION MATRIX
monitored_interface = "eth0_core"
current_network_load_pct = 92
CONGESTION_THRESHOLD_PCT = 85

print_master_border()
print("NEXXUS CITADEL OPERATIONAL MONITOR GRID")
print("INTERFACE: " + monitored_interface + " | STATUS AUDIT")
print_master_border()

# 3. Dynamic Mitigation Gate: Inspect network capacity thresholds
if current_network_load_pct > CONGESTION_THRESHOLD_PCT:
    print("[DISPATCH ALERT] HIGH VELOCITY TRAFFIC OVERRUN DETECTED!")
    print("CURRENT CAP: " + str(current_network_load_pct) + "% | LIMIT: " + str(CONGESTION_THRESHOLD_PCT) + "%")
    print("SECURITY MITIGATION ACTION: Activating Layer-3 traffic rate limiting.")
    print("INTERCEPT EXECUTION: Rerouting flood packets to sandboxed null route.")

    # Simulate deploying the system mitigation down the wire
    current_network_load_pct = 45
    print("PROTOCOL STABLE: Interface throttled back to clean load: " + str(current_network_load_pct) + "%")
else:
    print("[STABLE] Traffic throughput registers within normal baseline parameters.")
    print("Load metrics resting safely at: " + str(current_network_load_pct) + "%")

print_master_border()