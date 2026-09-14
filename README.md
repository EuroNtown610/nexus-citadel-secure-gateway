# 🏛️ Nexxus Citadel Secure Gateway
### Enterprise-Grade Edge Proxy, Multi-Tenant Rate Limiter & HIPAA Compliance Audit Engine
**Architected by:** Anthony J. Frazier (*Chief Systems Architect, Nexxus Citadel*)

---

## 🛑 The Client Vulnerability Real-World Case Study

### 🏥 The Clinic Pain Point (HIPAA Violation Risk)
Modern medical infrastructure relies heavily on internal microservice communications (Electronic Health Records, scheduling panels, and billing databases). In vanilla configurations, internal database queries pass over virtual bridges in unencrypted plain text. If an attacker gains initial lateral entry into any lower-priority container (e.g., an outdated corporate blog), they can execute low-level packet capture operations (`dumpcap` / `tshark`), sniffing protected health information (PHI) right off the wire. This exposes clinics to severe data breaches, ransomware escalation vectors, and massive regulatory fines.

### 🚀 The Startup Pain Point (Resource Exhaustion & Downtime)
Fast-growing tech startups frequently expose raw application endpoints to the public internet to ship features rapidly. Without a defensive perimeter layer, these endpoints are highly susceptible to malicious automated token sweeps, database brute-forcing, and API resource exhaustion that spikes cloud infrastructure billing and forces system instability.

---

## 🛡️ The Nexxus Citadel Blueprint & Core Engineering Features

This repository acts as a production-ready, fully containerized cyber-range infrastructure blueprint that enforces rigorous perimeter protection, zero-trust network zone isolation, and active telemetry scraping.

### 1. Hardened Edge Gateway Routing & Security Defenses
An **NGINX High-Availability Proxy Engine** acts as the definitive edge barrier facing the WAN. 
* **Zone Masking:** No internal application endpoints (FastAPI core, WordPress core) are exposed to the public internet. All traffic must validate through proxy channels.
* **Perimeter Header Hardening:** Injects ironclad security response headers natively to stop client-side clickjacking and exploitation maneuvers:
  * `X-Frame-Options: DENY`
  * `X-Content-Type-Options: nosniff`
  * `X-XSS-Protection: 1; mode=block`
* **Zero-Trust Input Drops:** Automated rules immediately trap and drop legacy attack vectors (such as unauthenticated `xmlrpc.php` sweeps) at the perimeter with a crisp `HTTP 403 Forbidden` response.

### 2. Atomic Counter-Based Multi-Tenant Rate Limiting
Bypasses standard clock-drift and timestamp synchronization flaws common in basic in-memory limiters. Implements an atomic counter system that tracks query spikes from multi-tenant access tokens at maximum raw execution speeds. Overwhelming the threshold instantly triggers an automated defensive gate block (`HTTP 429 Too Many Requests`).

### 3. Integrated SIEM Monitoring & Live Auditing Passthrough
Utilizes a high-efficiency data collection pipeline consisting of **Promtail**, **Loki**, and **Grafana**. Promtail taps directly into the Docker engine socket, captures container `stdout` alarms the exact millisecond they print, and streams the log volume data to an interactive security dashboard for real-time threat response and forensics tracing.

---

## 📊 Commercial Verification & Lab Operations

### ⚔️ Simulated Perimeter Threat Spray (Rate-Limiter Challenge)
To execute high-velocity traffic loop stress testing against the edge proxy:
```bash
python apps/test_rate_limiter.py
```
**Expected Architectural Enforcement Output:**
```text
[*] Launching zero-delay high-velocity token spray (10 requests)...
Request 01 -> Status Code: 200 | Payload: {"execution_state":"SUCCESS","current_hits":1}
Request 02 -> Status Code: 200 | Payload: {"execution_state":"SUCCESS","current_hits":2}
Request 03 -> Status Code: 200 | Payload: {"execution_state":"SUCCESS","current_hits":3}
Request 04 -> Status Code: 200 | Payload: {"execution_state":"SUCCESS","current_hits":4}
Request 05 -> Status Code: 200 | Payload: {"execution_state":"SUCCESS","current_hits":5}
Request 06 -> Status Code: 429 | Payload: {"detail":"BRUTE-FORCE MITIGATION: Request limit exceeded. Account throttled."}
```

### 📋 HIPAA Compliance Data In-Transit Scraper Audit
To check internal container networks for unencrypted compliance violations:
```bash
python apps/hipaa_audit_tool.py
```
**Expected Automated Assessment Ledger:**
```text
=================================================================
🛡️ NEXUS CITADEL SECURE SYSTEM LEDGER: HIPAA DATA-IN-TRANSIT AUDIT TOOL
=================================================================
[*] Interrogating internal cluster database pathways...

[+] Analyzing Intercepted Frame #01...
 -> 🚨 HIPAA CRITICAL EXPOSURE: Plain-text data in transit isolated!
 -> 🔎 Evidence footprint: "INSERT INTO medical_records (patient_name) VALUES ('John Doe')"

 -> [STATUS]: FAIL ❌
 -> Recommendation: Enforce direct TLS database connection profile parameters instantly.
```

---

## 💼 Available B2B Consulting Services
Nexxus Citadel provides premium contract security implementation and infrastructure engineering services for startups and medical providers:
* **Perimeter Hardening Packages:** NGINX edge routing, custom security header injections, and anti-brute force integration passes.
* **HIPAA Compliance Audits:** Internal network packet inspection, database query encryption verification, and data-in-transit tracing ledger reporting.
* **Managed SIEM Telemetry Setup:** Continuous cloud visibility dashboards and automated automated alert routing architectures.

For private asset consultation, project scoping, or emergency infrastructure hardening response, contact the **Nexxus Citadel Operations Center**.
