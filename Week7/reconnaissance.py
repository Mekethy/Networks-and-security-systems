import socket
import requests
def get_domain_info(domain):
    try:
        # Get IP address (active but low-risk)
        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")
        # Get public WHOIS-like info (passive, using a free API)
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        if response.status_code == 200:
            data = response.json()
            print(f"Organization: {data.get('org', 'Unknown')}")
            print(f"City: {data.get('city', 'Unknown')}")
            print(f"Country: {data.get('country_name', 'Unknown')}")
        else:
            print("Could not fetch WHOIS data.")
    except Exception as e:
        print(f"Error: {e}")
# Example: Use a public domain (never use without permission!)

import requests
def black_box_recon(url):
    try:
        response = requests.head(url)
        print("Black Box Findings:")
        print(f"Server: {response.headers.get('Server', 'Unknown')}")
        print(f"Content-Type: {response.headers.get('Content-Type','Unknown')}")
    except Exception as e:
        print(f"Error: {e}")

url = "http://python.com"
known_info = {"server": "Apache 2.4", "vulns": "Check CVE-2021-1234"}
black_box_recon(url)

import socket
def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

host = "127.0.0.1"
ports = [80, 443, 22, 8080]
open_ports = scan_ports(host, ports)
print(f"Open ports on {host}: {open_ports}")

import nmap
def nmap_scan(host, port_range='1-1024'):
    nm = nmap.PortScanner()
    try:
        nm.scan(host, port_range, arguments='-sV') # -sV for service version detection
        for host in nm.all_hosts():
            print(f"Host: {host} ({nm[host].hostname()})")
            print(f"State: {nm[host].state()}")
            for proto in nm[host].all_protocols():
                print(f"Protocol: {proto}")
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    service = nm[host][proto][port]
                    print(f"Port: {port}\tState: {service['state']}\tService:{service.get('name', 'unknown')} {service.get('version',
                    '')}")
    except Exception as e:
        print(f"Error: {e}")

# Example: Scan localhost
nmap_scan('127.0.0.1', '1-10')