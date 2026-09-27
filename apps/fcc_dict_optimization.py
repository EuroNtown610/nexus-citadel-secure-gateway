def main():
    print("=========================================================")
    print("📚 freeCodeCamp: VERIFIED DICTIONARY FILTERING MATRIX")
    print("=========================================================")
    
    # Flat data dictionary layout
    client_portfolio_registry = {
        "CLIENT_REF_801": {"company": "E-Commerce Engine Hub", "tier": "PREMIUM", "active_gigs": 3},
        "CLIENT_REF_802": {"company": "Local Medical Diagnostics", "tier": "STANDARD", "active_gigs": 1},
        "CLIENT_REF_803": {"company": "Fintech Startup Accelerator", "tier": "PREMIUM", "active_gigs": 0},
        "CLIENT_REF_804": {"company": "Norristown Contractor Network", "tier": "PREMIUM", "active_gigs": 5}
    }
    
    print("[*] Processing dynamic data extraction loops over key registers...\n")
    
    for key_id, info in client_portfolio_registry.items():
        account_name = info["company"]
        account_tier = info["tier"]
        workload_count = info["active_gigs"]
        
        if account_tier == "PREMIUM" and workload_count > 0:
            print(f" -> Account Reference ID: {key_id}")
            print(f"    └── Name: {account_name} | Active Engagements: {workload_count}")
            
    print("=========================================================")

if __name__ == "__main__":
    main()
