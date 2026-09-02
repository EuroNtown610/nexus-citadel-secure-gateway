import os
import gzip
import shutil
from datetime import datetime

LOG_SRC = "/app/production_traffic.log"
ARCHIVE_DIR = "/app/archived_logs"

def execute_system_log_rotation():
    print("[*] Initializing automated infrastructure log rotation sprint...")
    
    if not os.path.exists(LOG_SRC):
        print(f"[-] Halt: Source log trace file missing at {LOG_SRC}. Execution skipped.")
        return
        
    # Generate an isolated directory lane for your compressed files
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    
    # Formulate a unique chronological timestamp metric for the archive file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_output_path = os.path.join(ARCHIVE_DIR, f"system_logs_{timestamp}.log.gz")
    
    print(f"[*] Compressing plain text data log lines into secure archive: {archive_output_path}")
    
    # Open the source file and stream the data into a compressed GZIP binary layer
    with open(LOG_SRC, 'rb') as f_in:
        with gzip.open(archive_output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            
    # CRITICAL SECURITY PASS: Clear out the raw text file to prevent information leaks
    with open(LOG_SRC, 'w') as f_clear:
        f_clear.write(f"[{datetime.now()}] INFO: Log rotation sweep completed. Data footprint safely archived.\n")
        
    print("[✔] ROTATION SPRINT SUMMARY:")
    print(f"    Raw Text Logs: Compressed safely via GZIP binary packaging.")
    print(f"    Disk Boundary: Restored. Active text log cleared down to 1 baseline row.")

if __name__ == "__main__":
    execute_system_log_rotation()
