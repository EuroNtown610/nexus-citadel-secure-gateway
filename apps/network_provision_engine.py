import socket

# 1. Define our microservice target network infrastructure directory mapping
citadel_subnet_directory = {
    "sd_fastapi_core": 8000,
    "sd_mongo_engine": 27017,
    "sd_corporate_smb": 445
}

print("=================================================================")
print("🛰️ LAB 9: AUTOMATED MULTI-CONTAINER NETWORK PROBE")
print("=================================================================")

#2. Loop through the key-value dictionary items sequentially
for container_name, target_port in citadel_subnet_directory.items():
    print("Probing node line: " + container_name + " on port: " + str(target_port))

    # 3. Create the unique socket channel for this iteration pass
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((container_name, target_port))

    if result == 0:
        print(" [LIVE] Conection verified operational.")
    else:
        print("[OFFLINE] Handshake refused. Code: " + str(result))

    # 4. Tear down the socket connection block before the loop cycles forward
    s.close()

print("=================================================================")        
