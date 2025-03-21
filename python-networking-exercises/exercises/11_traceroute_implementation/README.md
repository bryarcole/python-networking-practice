# Exercise 11: Traceroute Implementation

In this exercise, you'll implement your own version of the traceroute utility, which traces the route that packets take through a network from source to destination. This will help you understand network routing, ICMP protocols, and packet time-to-live (TTL) mechanics.

## Objectives
- Understand how traceroute works
- Implement TTL-based path discovery
- Work with ICMP protocol messages
- Analyze network latency and routing
- Handle different network responses

## Tasks

### 1. Basic Traceroute
Create a script (`simple_traceroute.py`) that:
- Traces the route to a destination host
- Uses ICMP Echo Request messages with increasing TTL values
- Displays the IP address of each hop
- Shows response time for each hop
- Handles timeouts and unreachable destinations

### 2. Enhanced Traceroute
Create a script (`enhanced_traceroute.py`) that:
- Extends the basic traceroute with additional features
- Performs parallel probing for faster results
- Resolves hostnames for each hop
- Uses multiple probe packets per hop for more accurate timing
- Supports different probe methods (ICMP, UDP, TCP)

### 3. Traceroute Analyzer
Create a script (`traceroute_analyzer.py`) that:
- Analyzes the results of traceroute operations
- Identifies high-latency hops
- Detects routing loops
- Calculates jitter between consecutive probes
- Creates a visual representation of the path

### 4. Path Comparison Tool
Create a script (`path_compare.py`) that:
- Runs traceroute to a destination at different times
- Compares the routes to detect path changes
- Highlights differences in paths
- Tracks latency changes over time
- Generates reports on routing stability

## Example Usage

```
# Run a basic traceroute
sudo python simple_traceroute.py --destination www.example.com

# Run an enhanced traceroute with TCP probes
sudo python enhanced_traceroute.py --destination 8.8.8.8 --method tcp --port 443

# Analyze a traceroute output
python traceroute_analyzer.py --input traceroute_output.txt

# Compare paths at different times
python path_compare.py --destination www.google.com --interval 1h --duration 24h
```

## Tips
- Use raw sockets for sending custom packets (requires root/admin privileges)
- Understand the difference between ICMP "Time Exceeded" and "Destination Unreachable" messages
- Be aware that some routers may not respond to traceroute probes
- Set appropriate timeouts for responses
- Remember that network paths may be asymmetric (forward and return paths can differ)
- Consider using the scapy library for packet manipulation
- Be mindful of rate limiting to avoid overwhelming network devices

## Expected Outcome
You should have a functional traceroute utility that can discover and display the path packets take through a network, with timing information for each hop.

## Bonus Challenges
1. Implement MTU discovery along the path
2. Add support for IPv6 traceroute
3. Create a graphical representation of the network path
4. Integrate geolocation to show the geographical path 