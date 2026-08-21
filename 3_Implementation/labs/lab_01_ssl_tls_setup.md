# Lab 01 — TLS Certificate Setup and Validation

**Security+ domain:** Security Architecture / Implementation  
**Difficulty:** Intermediate

## Scenario

Protect a development web service with TLS and demonstrate certificate inspection, trust, expiry, and hostname validation.

## Objectives

- Generate a private key and self-signed certificate.
- Inspect X.509 certificate fields.
- Start a local TLS service.
- Validate certificate trust with OpenSSL.
- Explain common certificate failures.

## Prerequisites

- OpenSSL
- Python 3

## Part 1 — Generate a Private Key

```bash
mkdir -p tls-lab
cd tls-lab
openssl genrsa -out server.key 2048
chmod 600 server.key
```

## Part 2 — Create a Self-Signed Certificate

```bash
openssl req -new -x509 \
  -key server.key \
  -out server.crt \
  -days 30 \
  -subj "/C=GB/O=SecurityPlusLab/CN=localhost" \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"
```

## Part 3 — Inspect the Certificate

```bash
openssl x509 -in server.crt -noout -subject -issuer -dates -serial
openssl x509 -in server.crt -noout -text
```

Identify the subject, issuer, validity period, public-key algorithm, signature algorithm, and SAN.

## Part 4 — Start a Local TLS Listener

Copy `server.crt` and `server.key` into this lab directory, then run:

```bash
python3 scripts/tls_server.py
```

## Part 5 — Validate the Connection

```bash
openssl s_client -connect 127.0.0.1:8443 -servername localhost
```

Then explicitly trust the lab certificate:

```bash
openssl s_client \
  -connect 127.0.0.1:8443 \
  -servername localhost \
  -CAfile server.crt \
  -verify_return_error
```

## Part 6 — Failure Analysis

Describe what happens when:

1. A certificate is expired.
2. The hostname does not match the SAN.
3. The issuer is not trusted.
4. The private key is exposed.
5. A certificate is revoked.

## Verification

Explain the difference between:

- Encryption and identity
- Public key and private key
- Self-signed and CA-signed certificates
- Common Name and Subject Alternative Name
- Expiry and revocation

## Cleanup

Stop the TLS server with `Ctrl+C` and delete the lab private key when finished.

## Portfolio Summary

> Built and validated a local TLS service using OpenSSL, inspected X.509 certificate attributes, tested trust validation, and documented common certificate failure conditions.
