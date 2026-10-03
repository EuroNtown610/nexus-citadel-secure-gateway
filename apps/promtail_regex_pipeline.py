import sys
import re

# [NEXXUS SITADEL SYSTEMS PROTOCOL 4.1]: OPERATIONAL UI BANNERS
def print_master_border():
    print("=" * 60)

# [NEXXUS CITADEL SYSTEMS PROTOCOL 4.2]: RAW TELEMETRY LOG BUFFER STREAM
raw_nginx_log_stream = '192.168.1.105 - - [03/Oct/2026:17:10:00] "GET /admin/login HTTP/1.1" 404 234'

print_master_border()
print("NEXXUS CITADEL DATA SECURITY OPERATION CENTER")
print("PIPELINE AUDIT CONTROL: HIGH-VELOCITY PROMTAIL PARSER")
print_master_border()

# Parse out the exact client IP address and the trailing HTTP status code field
# Using regex capturing groups to parse components out of log line text
log_pattern = re.compile(r"^([\d.]+) .* \"[A-Z]+ .*\" (\d{3}) \d+")
match_object = log_pattern.match(raw_nginx_log_stream)

# 3. Dynamic Parser Logic Gate: Intercept routing anomalies
if match_object:
    client_ip = match_object.group(1)
    status_code = match_object.group(2)

    print("Log parsing successful. Evaluating Metrics...")

    if status_code == "404":
        print("[SECURITY ANOMALY EVENT DETECTED] PATH BRUTE-FORCE PROBING CAUGHT!")
        print("SOURCE CLIENT IP: " + client_ip)
        print("CAPTURED RESPONSE OVERRUN STATUS: " + status_code + "NOT FOUND")
        print("PROMTAIL PIPELINE RUTE: Pushing metrics to centralized Loki/grafana index pools")
    else:
        print("[EXTRACTION FAILURE] Log pattern does not match expected schema baseline frameworks.")

print_master_border()