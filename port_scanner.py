#!/usr/bin/env python3
"""
Basic Network Port Scanner
Educational tool for learning about network services and vulnerabilities

Usage:
    python3 port_scanner.py scan --host 192.168.1.1
    python3 port_scanner.py scan --host 192.168.1.0/24 --common
    python3 port_scanner.py scan --host example.com --ports 1-65535
"""

import socket
import sys
import argparse
import ipaddress
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple
import time


class PortScanner:
    """Basic port scanner with multi-threading support"""
    
    # Common ports and their services
    COMMON_PORTS = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
        443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP",
        5432: "PostgreSQL", 5900: "VNC", 8080: "HTTP-Alt",
        8443: "HTTPS-Alt", 27017: "MongoDB"
    }
    
    def __init__(self, timeout=2, max_workers=50):
        self.timeout = timeout
        self.max_workers = max_workers
        self.open_ports = []
    
    def get_service_name(self, port):
        """Get service name for a port"""
        try:
            return socket.getservbyport(port)
        except OSError:
            return self.COMMON_PORTS.get(port, "Unknown")
    
    def scan_port(self, host, port):
        """Scan a single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            
            if result == 0:
                service = self.get_service_name(port)
                return (port, service, True)
            else:
                return (port, None, False)
        except socket.gaierror:
            print(f"[!] Error: Cannot resolve hostname {host}")
            sys.exit(1)
        except socket.error:
            print(f"[!] Error connecting to {host}")
            sys.exit(1)
        except Exception as e:
            return (port, None, False)
    
    def scan_host(self, host, ports):
        """Scan multiple ports on a host"""
        print(f"\n[*] Scanning {host}...")
        print(f"[*] Scan started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)
        
        open_ports = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self.scan_port, host, port): port 
                for port in ports
            }
            
            for i, future in enumerate(as_completed(futures), 1):
                port, service, is_open = future.result()
                
                if is_open:
                    open_ports.append((port, service))
                    print(f"[+] Port {port:5d} - {service:15s} OPEN")
                
                # Progress indicator
                if i % 100 == 0:
                    print(f"[*] Scanned {i} ports...")
        
        return open_ports
    
    def scan_network(self, network, ports, common_only=False):
        """Scan multiple hosts on a network"""
        try:
            network_obj = ipaddress.ip_network(network, strict=False)
            hosts = [str(ip) for ip in network_obj.hosts()]
        except ValueError:
            print(f"[!] Invalid network: {network}")
            sys.exit(1)
        
        print(f"[*] Network scan: {network}")
        print(f"[*] Hosts to scan: {len(hosts)}")
        print(f"[*] Ports per host: {len(ports)}")
        
        all_results = {}
        
        for host in hosts:
            if host == str(network_obj.network_address) or host == str(network_obj.broadcast_address):
                continue
            
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((host, 22))  # Quick ping via SSH port
                sock.close()
                
                if result == 0:
                    print(f"[+] Host {host} is alive")
                    results = self.scan_host(host, ports)
                    if results:
                        all_results[host] = results
            except Exception as e:
                pass
        
        return all_results
    
    def generate_report(self, host, ports):
        """Generate a detailed scan report"""
        print("\n" + "=" * 60)
        print(f"SCAN REPORT - {host}")
        print("=" * 60)
        print(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Ports Scanned: {len(ports)}")
        print(f"Open Ports Found: {len(self.open_ports)}")
        print("-" * 60)
        
        if self.open_ports:
            print("\nOpen Ports:")
            for port, service in self.open_ports:
                print(f"  {port:5d}/{socket.getprotobyname('tcp'):3s} {service}")
        else:
            print("\nNo open ports found")
        
        print("=" * 60)


def parse_port_range(port_string):
    """Parse port range string (e.g., '80,443,1000-2000')"""
    ports = []
    parts = port_string.split(',')
    
    for part in parts:
        if '-' in part:
            start, end = part.split('-')
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(part))
    
    return sorted(list(set(ports)))


def main():
    parser = argparse.ArgumentParser(
        description="Network Port Scanner - Educational Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scan common ports
  python3 port_scanner.py scan --host 192.168.1.1 --common
  
  # Scan specific ports
  python3 port_scanner.py scan --host 192.168.1.1 --ports 22,80,443,3306
  
  # Scan port range
  python3 port_scanner.py scan --host 192.168.1.1 --ports 1-1000
  
  # Scan network
  python3 port_scanner.py scan --host 192.168.1.0/24 --common

Note: Ensure you have permission to scan before running!
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    scan_parser = subparsers.add_parser("scan", help="Scan for open ports")
    scan_parser.add_argument("--host", required=True, help="Target host or network (e.g., 192.168.1.1 or 192.168.1.0/24)")
    scan_parser.add_argument("--ports", help="Ports to scan (e.g., '80,443,1000-2000')")
    scan_parser.add_argument("--common", action="store_true", help="Scan only common ports")
    scan_parser.add_argument("--timeout", type=int, default=2, help="Connection timeout in seconds")
    scan_parser.add_argument("--workers", type=int, default=50, help="Number of worker threads")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    if args.command == "scan":
        scanner = PortScanner(timeout=args.timeout, max_workers=args.workers)
        
        # Determine ports to scan
        if args.common:
            ports = list(scanner.COMMON_PORTS.keys())
        elif args.ports:
            ports = parse_port_range(args.ports)
        else:
            # Default: common ports
            ports = list(scanner.COMMON_PORTS.keys())
        
        # Check if network scan
        if '/' in args.host:
            results = scanner.scan_network(args.host, ports, args.common)
            print("\n" + "=" * 60)
            print("NETWORK SCAN SUMMARY")
            print("=" * 60)
            for host, open_ports in results.items():
                print(f"{host}: {len(open_ports)} open ports")
                for port, service in open_ports:
                    print(f"  - Port {port}: {service}")
        else:
            # Single host scan
            scanner.open_ports = scanner.scan_host(args.host, ports)
            scanner.generate_report(args.host, ports)


if __name__ == "__main__":
    main()
