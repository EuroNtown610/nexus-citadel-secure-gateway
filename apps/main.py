import ssl
from fastapi import FastAPI

app = FastAPI(title="Nexxus Citadel Sovereign mTLS Core Mesh")

def configure_mutual_tls_context():
    """
    Cryptographic Handshake Architecture: Forcefully requires peer validation certificates
    before admitting data packets to inner storage channels.
    """
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # Require absolute client authentication certificate keys
    ssl_context.verify_mode = ssl.CERT_REQUIRED
    ssl_context.load_verify_locations(cafile="certs/ca.crt")
    ssl_context.load_cert_chain(certfile="certs/server.crt", keyfile="certs/server.key")
    return ssl_context



