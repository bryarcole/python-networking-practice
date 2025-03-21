# Exercise 12: DNS Client Implementation

In this exercise, you'll implement your own DNS client that can perform various DNS lookups and operations. This will help you understand the DNS protocol, how domain names are resolved, and the structure of DNS records.

## Objectives
- Understand the DNS protocol structure and message format
- Implement DNS query and response handling
- Work with different DNS record types
- Interpret and display DNS records
- Handle DNS protocol errors and timeouts

## Tasks

### 1. Basic DNS Client
Create a script (`dns_client.py`) that:
- Sends DNS queries for different record types (A, AAAA, MX, TXT, etc.)
- Parses DNS responses
- Displays formatted results
- Handles DNS errors and timeouts
- Allows specifying a DNS server to query

### 2. DNS Record Explorer
Create a script (`dns_explorer.py`) that:
- Performs comprehensive DNS lookups for a domain
- Retrieves and displays all common record types
- Follows CNAME records automatically
- Shows TTL values for all records
- Creates a summary of DNS configuration

### 3. DNS Zone Transfer
Create a script (`dns_zone_transfer.py`) that:
- Implements the AXFR protocol for zone transfers
- Attempts zone transfers from DNS servers
- Formats and displays the complete zone data
- Identifies security issues in DNS configuration
- Exports zone data to different formats

### 4. DNS Lookup Tool
Create a script (`dns_lookup_tool.py`) that:
- Provides a command-line interface for DNS operations
- Supports reverse DNS lookups
- Implements DNS tracing to show the resolution process
- Validates DNS configurations
- Checks for DNS security extensions (DNSSEC)

## Example Usage

```
# Perform basic DNS lookup
python dns_client.py --domain example.com --type A

# Explore all DNS records
python dns_explorer.py --domain example.com --output example_dns.json

# Attempt zone transfer
python dns_zone_transfer.py --domain example.com --server ns1.example.com

# Trace DNS resolution
python dns_lookup_tool.py --trace --domain www.example.com
```

## Tips
- Study RFC 1035 for DNS message format details
- Use raw sockets for precise control or higher-level libraries for convenience
- Remember that DNS primarily uses UDP on port 53, but may fall back to TCP
- Test with domains you control to avoid potential issues
- Be aware of recursive vs. iterative queries
- Implement proper error handling for malformed responses
- Consider rate limiting to avoid overwhelming DNS servers

## Expected Outcome
You should have a functional DNS client that can perform various DNS lookups, interpret the results, and provide useful information about domain name configurations.

## Bonus Challenges
1. Implement DNSSEC validation
2. Create a DNS cache with proper TTL handling
3. Add support for newer DNS protocols like DNS over HTTPS (DoH) or DNS over TLS (DoT)
4. Implement a simple authoritative DNS server 