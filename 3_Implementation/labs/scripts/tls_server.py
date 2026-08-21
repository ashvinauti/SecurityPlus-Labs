#!/usr/bin/env python3
"""Minimal localhost-only TLS server for the Security+ certificate lab."""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
from pathlib import Path

HOST = "127.0.0.1"
PORT = 8443

root = Path(__file__).resolve().parents[1]
cert = root / "server.crt"
key = root / "server.key"

if not cert.exists() or not key.exists():
    raise SystemExit(
        "Missing server.crt/server.key. Generate them first by following the lab."
    )

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=cert, keyfile=key)
server.socket = context.wrap_socket(server.socket, server_side=True)

print(f"TLS lab server listening on https://{HOST}:{PORT}")
print("Press Ctrl+C to stop.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nStopping server.")
finally:
    server.server_close()
