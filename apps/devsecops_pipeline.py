import re

# 1. Map the incoming source code payload batch directory
code_deployment_batch = {
    "auth_service.py": "def login(): return input_pass == saved_pass",
    "database_connector.py": "query = 'SELECT * FROM users WHERE id = ' + user_input",
    "payment_gateway.py": "def process_charge(): verify_ssl_cert = True"
}

print("=================================================================")
print("LAB 10: AUTOMATED CI/CD DEVSECOPS HARDENING PIPELINE")
print("=================================================================")

# 2. Iterate through each deployment file and parse the code blocks
for filename, source_code in code_deployment_batch.items():
    print("Analyzing code file asset: " + filename)

    # 3. Security Inspection Logic Gate: Check for insecure SQL additions
    if "SELECT" in source_code and "+" in source_code:
        print("[FAILED CI/CD STAGE] High Severity Threat Encountered.")
        print("Reason: Unsafe raw string concatenation used in database query.")
    else:
        print("[PASSED PIPELINE REVIEW] Source code complies with secure baselines.")

    print("-----------------------------------------------------------------")        