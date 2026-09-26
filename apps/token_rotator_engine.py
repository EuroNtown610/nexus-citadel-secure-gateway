import secrets
import string
import time

def generate_secure_token(length=32):
    # Generates a cryptographically secure random token string using secrets
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))

def run_token_rotation_pipeline():
    print("=" * 65)
    print("🔐 LAB 8: AUTOMATED SECURE API TOKEN ROTATION ENGINE")
    print("=" * 65)
    
    # Simulating a live production database cache tracking active API keys
    api_token_vault = {
        "APP_CLIENT_ID_001": {
            "current_token": "init_token_a1b2c3d4e5f6g7h8i9j0kl",
            "last_rotated": time.time() - 90000,  # Expired (> 24 hours ago)
            "status": "ACTIVE"
        },
        "APP_CLIENT_ID_002": {
            "current_token": generate_secure_token(),
            "last_rotated": time.time(),         # Freshly generated
            "status": "ACTIVE"
        }
    }
    
    print("[*] Interrogating active token cache expiration profiles...\n")
    
    rotation_interval = 86400  # 24-hour mandatory rotation threshold in seconds
    current_time = time.time()
    
    for client_id, profile in api_token_vault.items():
        time_delta = current_time - profile["last_rotated"]
        print(f"[*] Analyzing Client [{client_id}] - Age: {time_delta:.1f} seconds")
        
        if time_delta >= rotation_interval:
            print(f"  🚨 [EXPIRED TOKEN INTERCEPTED] Initializing secure key rotation...")
            
            # Step 1: Mark old token as revoked
            old_token = profile["current_token"]
            
            # Step 2: Generate fresh cryptographic string token
            new_token = generate_secure_token()
            
            # Step 3: Update local vault profile state parameters
            profile["current_token"] = new_token
            profile["last_rotated"] = current_time
            
            print(f"  [✔ KEY ROTATED SUCCESSFULLY]")
            print(f"   ├── Revoked String Reference:  {old_token[:6]}...")
            print(f"   └── Injected Active Token ID:  {new_token[:6]}...\n")
        else:
            print(f"  [✔ STATE VALID] Active token complies with lifetime policies.\n")
            
    print("=" * 65)
    print("[✔ PIPELINE COMPLETE] All API application lanes secured.")
    print("=" * 65)

if __name__ == "__main__":
    run_token_rotation_pipeline()
