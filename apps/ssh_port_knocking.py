import sys

# 1. Define custom reusable UI banners
def print_divider():
    print("=" * 32)

# 2. Configure the secret sequence array code required to open the port
SECRET_KNOCK_SEQUENCE = [7000, 8000, 9000]
current_connection_attempts = [7000, 8000, 9000]

print_divider()
print("LAB 15:  SSH PORT KNOCKING DEFENSE")
print_divider

# 3. Dynamic Firewall Verification Gate: Match knock signatures
if current_connection_attempts == SECRET_KNOCK_SEQUENCE:
    print("[ACCESS UNLOCKED] Valid port knock sequence intercepted.")
    print(" Action: Temporarily opening SSH Port 22 for administration.")
else:
    print("LOCKDOWN ENFORCED Sequence mismatch detected!")
    print("Action: Dropping all packet frames and maintaining Port 22 stealth mode.")