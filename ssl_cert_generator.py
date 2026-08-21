#!/usr/bin/env python3
"""
SSL/TLS Certificate Generator and Manager
Demonstrates cryptographic concepts and certificate lifecycle management

Usage:
    python3 ssl_cert_generator.py generate-self-signed
    python3 ssl_cert_generator.py view-cert domain.crt
    python3 ssl_cert_generator.py create-csr domain.com
"""

import os
import sys
import argparse
import subprocess
import json
from datetime import datetime, timedelta
from pathlib import Path
from cryptography import x509
from cryptography.x509.oid import NameOID, ExtensionOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend


class CertificateManager:
    """Manage SSL/TLS certificates"""
    
    def __init__(self, cert_dir="./certs"):
        self.cert_dir = Path(cert_dir)
        self.cert_dir.mkdir(exist_ok=True)
        self.backend = default_backend()
    
    def generate_private_key(self, key_size=2048):
        """Generate RSA private key"""
        print(f"[+] Generating {key_size}-bit RSA private key...")
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=self.backend
        )
    
    def create_self_signed_cert(self, domain, days=365, key_size=2048):
        """Create self-signed certificate"""
        print(f"\n[*] Creating self-signed certificate for: {domain}")
        
        # Generate private key
        private_key = self.generate_private_key(key_size)
        
        # Build certificate
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"State"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, u"City"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Organization"),
            x509.NameAttribute(NameOID.COMMON_NAME, domain),
        ])
        
        cert = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            private_key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.utcnow()
        ).not_valid_after(
            datetime.utcnow() + timedelta(days=days)
        ).add_extension(
            x509.SubjectAlternativeName([
                x509.DNSName(domain),
                x509.DNSName(f"*.{domain}"),
            ]),
            critical=False,
        ).add_extension(
            x509.BasicConstraints(ca=False, path_length=None),
            critical=True,
        ).sign(private_key, hashes.SHA256(), self.backend)
        
        # Save certificate
        cert_path = self.cert_dir / f"{domain}.crt"
        with open(cert_path, "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
        print(f"[✓] Certificate saved: {cert_path}")
        
        # Save private key
        key_path = self.cert_dir / f"{domain}.key"
        with open(key_path, "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))
        print(f"[✓] Private key saved: {key_path}")
        os.chmod(key_path, 0o600)  # Restrict permissions
        
        return cert, private_key
    
    def create_csr(self, domain, key_size=2048):
        """Create Certificate Signing Request (CSR)"""
        print(f"\n[*] Creating CSR for: {domain}")
        
        # Generate private key
        private_key = self.generate_private_key(key_size)
        
        # Build CSR
        csr = x509.CertificateSigningRequestBuilder().subject_name(
            x509.Name([
                x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
                x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"State"),
                x509.NameAttribute(NameOID.LOCALITY_NAME, u"City"),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Organization"),
                x509.NameAttribute(NameOID.COMMON_NAME, domain),
            ])
        ).add_extension(
            x509.SubjectAlternativeName([
                x509.DNSName(domain),
                x509.DNSName(f"*.{domain}"),
            ]),
            critical=False,
        ).sign(private_key, hashes.SHA256(), self.backend)
        
        # Save CSR
        csr_path = self.cert_dir / f"{domain}.csr"
        with open(csr_path, "wb") as f:
            f.write(csr.public_bytes(serialization.Encoding.PEM))
        print(f"[✓] CSR saved: {csr_path}")
        
        # Save private key
        key_path = self.cert_dir / f"{domain}.key"
        with open(key_path, "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))
        print(f"[✓] Private key saved: {key_path}")
        os.chmod(key_path, 0o600)
    
    def view_certificate(self, cert_path):
        """Display certificate information"""
        try:
            with open(cert_path, "rb") as f:
                cert_data = f.read()
            
            cert = x509.load_pem_x509_certificate(cert_data, self.backend)
            
            print(f"\n[*] Certificate Information: {cert_path}")
            print("=" * 60)
            print(f"Subject: {cert.subject.rfc4514_string()}")
            print(f"Issuer: {cert.issuer.rfc4514_string()}")
            print(f"Serial Number: {cert.serial_number}")
            print(f"Valid From: {cert.not_valid_before}")
            print(f"Valid Until: {cert.not_valid_after}")
            
            # Calculate days until expiration
            days_left = (cert.not_valid_after - datetime.utcnow()).days
            if days_left > 0:
                print(f"Days Until Expiration: {days_left}")
            else:
                print(f"[!] Certificate EXPIRED ({abs(days_left)} days ago)")
            
            print(f"Public Key Size: {cert.public_key().key_size} bits")
            print(f"Signature Algorithm: {cert.signature_algorithm_oid._name}")
            
            # Show SANs
            try:
                san_ext = cert.extensions.get_extension_for_oid(ExtensionOID.SUBJECT_ALTERNATIVE_NAME)
                print(f"Subject Alternative Names:")
                for name in san_ext.value:
                    print(f"  - {name.value}")
            except x509.ExtensionNotFound:
                pass
            
            print("=" * 60)
            
        except FileNotFoundError:
            print(f"[!] Certificate not found: {cert_path}")
            sys.exit(1)
        except Exception as e:
            print(f"[!] Error reading certificate: {e}")
            sys.exit(1)
    
    def convert_format(self, input_cert, output_format="pem"):
        """Convert certificate format (PEM <-> DER)"""
        try:
            with open(input_cert, "rb") as f:
                cert_data = f.read()
            
            cert = x509.load_pem_x509_certificate(cert_data, self.backend)
            
            if output_format.lower() == "der":
                output_cert = input_cert.replace(".crt", ".der")
                with open(output_cert, "wb") as f:
                    f.write(cert.public_bytes(serialization.Encoding.DER))
                print(f"[✓] Converted to DER: {output_cert}")
            elif output_format.lower() == "pem":
                print(f"[i] Certificate is already in PEM format")
        
        except Exception as e:
            print(f"[!] Conversion error: {e}")
    
    def verify_certificate_chain(self, cert_file, ca_file=None):
        """Verify certificate chain"""
        print(f"\n[*] Verifying certificate chain...")
        
        if ca_file:
            try:
                # Use OpenSSL for chain verification
                result = subprocess.run([
                    "openssl", "verify", "-CAfile", ca_file, cert_file
                ], capture_output=True, text=True)
                
                print(result.stdout)
                if result.returncode != 0:
                    print(f"[!] Verification failed: {result.stderr}")
                else:
                    print("[✓] Certificate chain verified successfully")
            except FileNotFoundError:
                print("[!] OpenSSL not found. Install it to verify chains.")
        else:
            print("[i] No CA certificate provided for chain verification")


def main():
    parser = argparse.ArgumentParser(
        description="SSL/TLS Certificate Generator and Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create self-signed certificate
  python3 ssl_cert_generator.py generate-self-signed --domain example.com
  
  # View certificate details
  python3 ssl_cert_generator.py view-cert ./certs/example.com.crt
  
  # Create CSR for CA signing
  python3 ssl_cert_generator.py create-csr --domain example.com
  
  # Convert certificate format
  python3 ssl_cert_generator.py convert --input cert.crt --output der
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Generate self-signed certificate
    gen_parser = subparsers.add_parser("generate-self-signed", help="Generate self-signed certificate")
    gen_parser.add_argument("--domain", required=True, help="Domain name")
    gen_parser.add_argument("--days", type=int, default=365, help="Certificate validity days")
    gen_parser.add_argument("--key-size", type=int, default=2048, help="RSA key size")
    gen_parser.add_argument("--cert-dir", default="./certs", help="Certificate directory")
    
    # View certificate
    view_parser = subparsers.add_parser("view-cert", help="View certificate details")
    view_parser.add_argument("cert_file", help="Certificate file path")
    
    # Create CSR
    csr_parser = subparsers.add_parser("create-csr", help="Create Certificate Signing Request")
    csr_parser.add_argument("--domain", required=True, help="Domain name")
    csr_parser.add_argument("--key-size", type=int, default=2048, help="RSA key size")
    csr_parser.add_argument("--cert-dir", default="./certs", help="Certificate directory")
    
    # Convert format
    convert_parser = subparsers.add_parser("convert", help="Convert certificate format")
    convert_parser.add_argument("--input", required=True, help="Input certificate file")
    convert_parser.add_argument("--output", default="der", help="Output format (pem/der)")
    
    # Verify chain
    verify_parser = subparsers.add_parser("verify", help="Verify certificate chain")
    verify_parser.add_argument("--cert", required=True, help="Certificate file")
    verify_parser.add_argument("--ca", help="CA certificate file")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    manager = CertificateManager(getattr(args, "cert_dir", "./certs"))
    
    if args.command == "generate-self-signed":
        manager.create_self_signed_cert(args.domain, args.days, args.key_size)
    
    elif args.command == "view-cert":
        manager.view_certificate(args.cert_file)
    
    elif args.command == "create-csr":
        manager.create_csr(args.domain, args.key_size)
    
    elif args.command == "convert":
        manager.convert_format(args.input, args.output)
    
    elif args.command == "verify":
        manager.verify_certificate_chain(args.cert, args.ca)


if __name__ == "__main__":
    main()
