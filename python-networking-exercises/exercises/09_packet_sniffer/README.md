# Exercise 9: Packet Sniffer

In this exercise, you'll build a packet sniffer that can capture and analyze network traffic. This will help you understand network protocols, packet structure, and data encapsulation.

## Objectives
- Understand network packet structure and headers
- Capture raw network packets using Python
- Parse and interpret different protocol headers (Ethernet, IP, TCP, UDP, etc.)
- Extract and analyze packet payloads
- Filter and process specific types of network traffic

## Tasks

### 1. Basic Packet Capture
Create a script (`packet_capture.py`) that:
- Captures packets from a network interface
- Displays basic information about each captured packet
- Saves captured packets to a file
- Handles keyboard interrupts to stop capturing gracefully

### 2. Protocol Header Parser
Create a module (`packet_parser.py`) that:
- Parses Ethernet frame headers
- Parses IP packet headers (v4 and v6)
- Parses TCP and UDP headers
- Parses ICMP messages
- Extracts header flags and options

### 3. Application Protocol Analyzer
Create a script (`protocol_analyzer.py`) that:
- Identifies common application protocols (HTTP, DNS, DHCP, etc.)
- Extracts and displays relevant information from application data
- Reconstructs data streams from TCP packets
- Detects and reports unusual or malformed packets

### 4. Traffic Monitor
Create a script (`traffic_monitor.py`) that:
- Displays real-time statistics on network traffic
- Groups packets by protocol, source, and destination
- Calculates bandwidth usage by host and protocol
- Creates summaries of traffic patterns
- Alerts on suspicious activity or threshold crossings

## Example Usage

```
# Capture packets on a specific interface
sudo python packet_capture.py --interface eth0 --count 100

# Analyze captured packets from a file
python protocol_analyzer.py --file captured_packets.pcap

# Monitor network traffic in real-time
sudo python traffic_monitor.py --interface eth0 --interval 5
```

## Tips
- Use the `scapy` library for advanced packet manipulation
- Use `libpcap` (through python bindings like `pypcap` or `pcapy`) for efficient packet capture
- Remember that packet sniffing usually requires administrative/root privileges
- Study RFC documents to understand protocol specifications
- Use wireshark as a reference tool for packet analysis
- Be mindful of privacy and legal considerations when capturing packets

## Expected Outcome
You should have a functional packet sniffer that can capture, parse, and analyze network traffic, providing insights into protocol behavior and network communication.

## Bonus Challenges
1. Implement protocol-specific dissectors (e.g., parse HTTP headers, DNS queries)
2. Add packet injection capabilities
3. Create visualizations of network traffic patterns
4. Implement anomaly detection for network security monitoring 