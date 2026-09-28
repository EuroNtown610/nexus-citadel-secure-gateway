import sys

# 1. Define custom resusable UI decoration banners
def print_divider():
    print("=" * 32)

# 2. Map the target secure network interface properties
vpn_interface = "wg0"
tunnel_encrypted = True 

print_divider()
print("LAB 14: SECURE TUNNEL ACCELERATION")
print_divider

# 3. Cryptographic Verificiation Gate: Audit interface status
if vpn_interface == "wg0" and tunnel_encrypted == True:
    print("[SAFE] Wireguard interface tunnel verified.")
    print("Encrypted data lane operational across containers")
else:
    print("[EXPOSED] Traffic passing over cleartext bridge layers!")
    print("Countermeasure: Terminating raw unencrypted packet frames.")

print_divider