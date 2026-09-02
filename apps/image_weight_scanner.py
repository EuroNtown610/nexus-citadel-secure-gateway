import os
import time

TARGET_DIR = "/app/unoptimized_images"
REPORT_OUTPUT_PATH = "./logs/Website_Image_Weight_Audit.txt"
SIZE_THRESHOLD_KB = 500.0  # Files larger than 500KB hurt mobile load times

def execute_image_weight_audit():
    print(f"[*] Initializing website asset file weight audit inside: {TARGET_DIR}...")
    
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR, exist_ok=True)
        print(f"[!] Directory was missing. Created empty folder at: {TARGET_DIR}")
        return

    file_list = os.listdir(TARGET_DIR)
    if not file_list:
        print("[!] No assets found to scan. Add raw images to target folder.")
        return

    flagged_assets = []
    total_images_scanned = 0

    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

    for filename in file_list:
        if filename.lower().endswith(valid_extensions):
            total_images_scanned += 1
            file_path = os.path.join(TARGET_DIR, filename)
            file_size_kb = os.path.getsize(file_path) / 1024
            
            # Flag any image file that exceeds our performance weight limits
            if file_size_kb > SIZE_THRESHOLD_KB:
                flagged_assets.append({"name": filename, "size": round(file_size_kb, 2)})
                print(f"[⚠️ WARNING] Heavy Asset Identified: {filename} ({round(file_size_kb, 2)} KB)")

    write_audit_report(total_images_scanned, flagged_assets)

def write_audit_report(total_scanned, flagged_list):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    report_text = (
        f"====================================================\n"
        f"      NEXXUS CITADEL WEBSITE IMAGE WEIGHT REPORT     \n"
        f"      GENERATED: {timestamp}                       \n"
        f"====================================================\n"
        f"Total Graphic Assets Scanned: {total_scanned}\n"
        f"Total Performance-Throttling Files Flagged: {len(flagged_list)}\n"
        f"----------------------------------------------------\n\n"
    )

    if flagged_list:
        report_text += "DETAILED PERFORMANCE LIABILITY PROFILE:\n"
        for asset in flagged_list:
            report_text += f" -> [FLAGGED] File: {asset['name']} | Weight: {asset['size']} KB (Exceeds {SIZE_THRESHOLD_KB}KB Limit)\n"
        report_text += f"\nRECOMMENDED ACTION:\n Run automated WebP batch-compression engine sprint instantly to reclaim disk boundaries.\n"
    else:
        report_text += "[✔] SUCCESS: All scanned image file assets sit safely within optimal web performance limits.\n"

    os.makedirs(os.path.dirname(REPORT_OUTPUT_PATH), exist_ok=True)
    with open(REPORT_OUTPUT_PATH, "w") as report_file:
        report_file.write(report_text)
        
    print(f"\n[✔] Structural weight report cleanly written onto disk: {REPORT_OUTPUT_PATH}")

if __name__ == "__main__":
    execute_image_weight_audit()
