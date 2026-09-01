import os

LOG_FILE_PATH = "./logs/production_traffic.log"
MAX_LOG_LINES = 100

def purge_outdated_system_logs():
    """
    Implements a strict storage optimization gate by stripping old 
    traffic records and archiving only the most recent operational events.
    """
    print("[*] Initiating storage environment baseline check...")
    
    if not os.path.exists(LOG_FILE_PATH):
        print("[-] Target file stream empty. Purge sequence bypassed.")
        return

    # Read all active lines into a local application memory array
    with open(LOG_FILE_PATH, "r") as file:
        all_log_entries = file.readlines()

    total_records = len(all_log_entries)
    print(f"[!] Current data volume: {total_records} lines logged.")

    if total_records > MAX_LOG_LINES:
        # Use clean slicing optimization to capture only the newest entries
        optimized_dataset = all_log_entries[-MAX_LOG_LINES:]
        
        # Overwrite the active server ledger with the trimmed array slice
        with open(LOG_FILE_PATH, "w") as file:
            file.writelines(optimized_dataset)
            
        lines_purged = total_records - MAX_LOG_LINES
        print(f"[✔] CLEANUP COMPLETED: {lines_purged} stale operational lines purged cleanly from disk.")
    else:
        print("[✔] Disk capacity metrics normal. Structural compression threshold not reached.")

if __name__ == "__main__":
    purge_outdated_system_logs()
