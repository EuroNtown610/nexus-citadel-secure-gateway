import socket
import ssl
import time
import os

LOG_OUTPUT_PATH = "./logs/Automated_Security_Audit_Log.txt"

def run_perimeter_diagnostic(target_host, target_port=443):
    """
    Executes a high-velocity connection test to analyze server 
    handshake latency and verify SSL certificate profiles.
    """
    print(f"[*] Initializing network diagnostic pass against: {target_host}...")
    
    # Establish standard socket connection layers
    base_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    base_socket.settimeout(3.0)
    
    # Create a secure SSL context engine
    ssl_context = ssl.create_default_context()
    secure_socket = ssl_context.wrap_socket(base_socket, server_hostname=target_host)
    
    start_time = time.time()
    try:
        # Measure true infrastructure connection handshake speed
        secure_socket.connect((target_host, target_port))
        handshake_latency_ms = (time.time() - start_time) * 1000
        
        cert_data = secure_socket.getpeercert()
        ssl_status = "VERIFIED // ENCRYPTED"
        print(f"[+] Diagnostic complete. Connection Latency: {round(handshake_latency_ms, 2)} ms")
        
    except Exception as e:
        handshake_latency_ms = (time.time() - start_time) * 1000
        ssl_status = f"EXPOSED // ERROR: {str(e)}"
        print(f"[❌] Network handshake failed or timed out.")
        
    finally:
        secure_socket.close()
        
    write_audit_log_entry(target_host, ssl_status, handshake_latency_ms)

def write_audit_log_entry(host, ssl_state, latency):
    """Pipes the real-time network diagnostics to a local text log file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
        f"--- INFRASTRUCTURE DIAGNOSTIC RECORD ({timestamp}) ---\n"
        f"Target Host Asset: {host}\n"
        f"SSL Perimeter Layer: {ssl_state}\n"
        f"Connection Handshake Speed: {round(latency, 2)} ms\n"
        f"----------------------------------------------------\n\n"
    )
    
    os.makedirs(os.path.dirname(LOG_OUTPUT_PATH), exist_ok=True)
    with open(LOG_OUTPUT_PATH, "a") as log_file:
        log_file.write(log_entry)
    print(f"[+] Diagnostic metrics successfully written to: {LOG_OUTPUT_PATH}")

if __name__ == "__main__":
    # Test your script using a standard external domain target
    run_perimeter_diagnostic("google.com")
