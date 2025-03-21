# Exercise 8: Network Scanner

In this exercise, you'll create a network scanner that can discover active hosts on a network, scan for open ports, and identify running services. This will help you understand IP addressing, network protocols, and security concepts.

## Objectives
- Understand IP addressing and network ranges
- Implement network host discovery techniques
- Create a port scanner to identify open services
- Parse and interpret network responses
- Implement proper error handling and timeouts

## Tasks

### 1. IP Address Utilities
Create a module (`ip_utils.py`) that:
- Validates IP addresses and CIDR notation
- Converts between IP addresses and their binary representations
- Generates a list of all IP addresses in a given network range
- Determines if an IP is within a specific subnet

### 2. Host Discovery Tool
Create a script (`host_discovery.py`) that:
- Pings all addresses in a specified network range
- Uses ICMP Echo requests to identify live hosts
- Implements ARP scanning for local network discovery
- Records response times and packet loss
- Presents results in a user-friendly format

### 3. Port Scanner
Create a script (`port_scanner.py`) that:
- Scans a target host for open TCP/UDP ports
- Allows specifying port ranges or common service ports
- Implements different scanning techniques (SYN, connect, etc.)
- Detects and identifies common services (HTTP, SSH, etc.)
- Handles timeouts and rate limiting to avoid overwhelming the network

### 4. Service Identification
Create a script (`service_detector.py`) that:
- Connects to open ports to gather service banners
- Identifies service versions from responses
- Detects operating system information when possible
- Reports potential security vulnerabilities
- Presents findings in an organized report

## Example Usage

```
# Scan a network range for live hosts
python host_discovery.py --network 192.168.1.0/24

# Scan ports on a specific host
python port_scanner.py --target 192.168.1.1 --port-range 1-1000

# Identify services on open ports
python service_detector.py --target 192.168.1.1 --ports 22,80,443
```

## Tips
- Use the `scapy` library for low-level packet creation and handling
- Consider using `nmap-python` for higher-level scanning functionality
- Be mindful of network security and only scan networks you have permission to test
- Use proper socket timeouts to handle unresponsive hosts
- Implement rate limiting to avoid flooding the network
- Consider parallel scanning for efficiency, but be careful with resource usage

## Expected Outcome
You should have a functional network scanner that can discover hosts, identify open ports, and detect running services. This tool will give you insight into network structure and security.

## Bonus Challenges
1. Implement a vulnerability scanner that checks for common security issues
2. Create a graphical network map from scan results
3. Add OS fingerprinting capabilities
4. Create a stealth scanning mode that's harder to detect 