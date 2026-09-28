import os

# 1. Define custom resuable console UI decoration banners 
def print_divder():
    print("=" * 32)

# 2. Map the target container filesystem path for Nginx access streams
target_log_dir = "logs"
target_log_file = "logs/nginx_access.log"

# Fire the custom function commands to render your UI walls automatically
print_divder()
print("LAB 13: LOCAL NGINX LOG ENCAPSULATION")
print_divder()

# 3. Verify target logging directories exist on disk arrays
if os.path.exists(target_log_dir):
    print("[SYSTEM OK] Target logging infrastructure path verified.")
else:
    print("[ALERT] Target path missing! Initializing fallback directory...")
    os.makedirs(target_log_dir)

# 4. Open and securely read the upstream Nginx acces log lines
with open(target_log_file, "r") as log_file:
    for log_line in log_file:
        print("Raw Log Captured: " + log_line.strip())