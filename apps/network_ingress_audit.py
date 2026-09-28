import sys

# 1. Structure the network ingress telemetry directory matrix
ingress_traffic_log = [
    {"source": "sd_nginx_edge_proxy", "destination": "sd_fastapi_core", "port": 8000, "protocol": "HTTP"},
    {"source": "sd_kali_sandbox", "destination": "sd_mongo_engine", "port": 27017, "protocol": "MONGODB"},
    {"source": "sd_target_rogue_nginx", "destination": "sd_corporate_smb", "port": 445, "protocol": "SMB"},
]

print("================================")
print("LAB 12: AUTOMATED DOCKER NETWORK INGRESS AUDITING")
print("================================")

# 2. Iterate through the network Log array matrix dynamically
for log_entry in ingress_traffic_log:
    source_node = log_entry["source"]
    target_node = log_entry["destination"]
    target_port = log_entry["port"]

    print("Auditing stream link: " + source_node + " to" + target_node)

    # 3. Dynamic Isolation Logic Gate: Block lateral invasion vectors
    if target_node == "sd_corporate_smb" and source_node != "sd_nginx_edge_proxy":
        print("[CRITICAL ACCESS INCIDENT IN PROGRESS]")
        print("EXPLOIT THREAT: Rogue lateral connection intercepted on port " + str(target_port))
        print("DEFENSE CONTAINER ACTION: Dropping packets and sandboxing node: " + source_node + "\n")
    else:
        print("[ACCESS PASS] Interference lane complies with routing tables.\n")

print("================================")
