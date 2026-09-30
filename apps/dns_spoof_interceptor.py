import sys

# 1. Define custom reusuable console UI decoration banners
def print_divider():
    print("=" * 32)

# 2. Configure our secure internal DNS mapping table values
AUTHENTIC_IP_MAP = "172.18.0.4"
resolved_domain_ip = "172.18.0.99"

print_divider()
print("Lab 17: DNS SPOOF INTERCEPTOR")
print_divider

# 3. Security Evaluation Logic Gate: Cross-check live wire routing
if resolved_domain_ip == AUTHENTIC_IP_MAP:
    print("[ACCESS PASS] Name resolution matches authentic registry.")
    print("Routing connection frame to target database cluster.")
else:
    print("[CRITICAL ALERT] DNS CACHE POISONING DETECTED!")
    print("Threat Vector: Domain redirected to unauthorized IP: " + resolved_domain_ip)
    print("Action: Severing network interface to protect enterprise records.")

print_divider()