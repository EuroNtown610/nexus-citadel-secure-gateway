from PIL import Image
import os
import time

INPUT_DIR = "/app/unoptimized_images"
OUTPUT_DIR = "/app/optimized_assets"

def execute_batch_compression_sprint():
    """
    Sweeps the local staging workspace, automatically converting and 
    compressing raw heavy media formats into highly optimized WebP files.
    """
    print("[*] Initializing automated asset performance compression loop...")
    
    # Establish staging directory paths inside the container
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Auto-generate a test file if the folder is empty to verify data flow
    if not os.listdir(INPUT_DIR):
        dummy_img = Image.new('RGB', (1920, 1080), color = (20, 40, 80))
        dummy_img.save(os.path.join(INPUT_DIR, "placeholder_hero.jpg"))
        print("[!] Staging workspace empty. Created placeholder_hero.jpg to verify data loops.")

    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
    total_saved_bytes = 0
    file_count = 0

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(valid_extensions):
            file_count += 1
            raw_path = os.path.join(INPUT_DIR, filename)
            
            # Formulate the clean WebP output filename parameter
            base_name = os.path.splitext(filename)[0]
            export_path = os.path.join(OUTPUT_DIR, f"{base_name}.webp")
            
            initial_size = os.path.getsize(raw_path)
            
            # Convert and compress inside local hardware memory bounds
            with Image.open(raw_path) as img:
                # quality=80 provides a massive file reduction with zero visual quality loss
                img.save(export_path, "WEBP", quality=80, method=6)
                
            optimized_size = os.path.getsize(export_path)
            saved_bytes = initial_size - optimized_size
            total_saved_bytes += saved_bytes
            
            print(f"[+] Compressed: {filename} // Weight Reduced by: {round(saved_bytes / 1024, 2)} KB")

    print("\n[✔] PERFORMANCE SPRINT SUMMARY:")
    print(f"    Total Processed Files: {file_count}")
    print(f"    Total Storage Reclaimed from Disk: {round(total_saved_bytes / (1024 * 1024), 2)} MB")

if __name__ == "__main__":
    execute_batch_compression_sprint()
