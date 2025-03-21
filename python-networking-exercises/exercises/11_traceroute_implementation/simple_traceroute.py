#!/usr/bin/env python3
"""
Simple Traceroute - Traceroute Implementation Exercise

This script implements a basic traceroute utility using ICMP echo requests.
Note: This script requires administrative/root privileges to run.
"""

import argparse
import os
import sys
import socket
import struct
import time
import select
from scapy.all import IP, ICMP, sr1, conf

# Constants
DEFAULT_MAX_HOPS = 30
DEFAULT_TIMEOUT = 2  # seconds
DEFAULT_PROBES = 3


def create_socket():
    """
    Create a raw socket for sending/receiving ICMP packets.
    
    Returns:
        socket: Raw socket for ICMP
    """
    # TODO: Implement socket creation
    # Create a raw socket with ICMP protocol
    pass

def resolve_hostname(hostname):
    """
    Resolve a hostname to an IP address.
    
    Args:
        hostname (str): Hostname to resolve
        
    Returns:
        str: IP address
    """
    # TODO: Implement hostname resolution
    # Use socket.gethostbyname() to resolve the hostname
    pass

def send_probe(sock, destination, ttl, probe_id, timeout):
    """
    Send a single probe packet with the given TTL.
    
    Args:
        sock (socket): The socket to use
        destination (str): Destination IP address
        ttl (int): Time to live value
        probe_id (int): Probe identifier
        timeout (float): Timeout in seconds
        
    Returns:
        tuple: (responder_ip, rtt, icmp_type, icmp_code)
    """
    # TODO: Implement probe sending and receiving
    # Set socket TTL
    # Send ICMP echo request packet
    # Wait for response with timeout
    # Parse response and calculate RTT
    pass

def send_probes(destination, max_hops=DEFAULT_MAX_HOPS, timeout=DEFAULT_TIMEOUT, probes_per_hop=DEFAULT_PROBES):
    """
    Perform a traceroute to the destination.
    
    Args:
        destination (str): Destination hostname or IP address
        max_hops (int): Maximum number of hops to try
        timeout (float): Timeout in seconds for each probe
        probes_per_hop (int): Number of probes per hop
    """
    # TODO: Implement traceroute
    # Resolve the destination hostname
    # Create a raw socket
    # For each TTL from 1 to max_hops:
    #   Send probes_per_hop probes
    #   Display results for this hop
    #   If we've reached the destination, stop
    pass

def format_probe_result(ttl, probe_num, result):
    """
    Format the result of a single probe.
    
    Args:
        ttl (int): Time to live value
        probe_num (int): Probe number
        result (tuple): (responder_ip, rtt, icmp_type, icmp_code)
        
    Returns:
        str: Formatted result string
    """
    # TODO: Implement result formatting
    # Format the probe result for display
    pass

def main():
    """Main function to run the traceroute."""
    # Check if running with admin/root privileges
    if os.geteuid() != 0:
        print("Error: This script requires administrative privileges.")
        print("Please run with sudo or as root.")
        return 1
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Simple Traceroute Implementation')
    parser.add_argument('--destination', '-d', required=True,
                        help='Destination hostname or IP address')
    parser.add_argument('--max-hops', '-m', type=int, default=DEFAULT_MAX_HOPS,
                        help=f'Maximum number of hops (default: {DEFAULT_MAX_HOPS})')
    parser.add_argument('--timeout', '-t', type=float, default=DEFAULT_TIMEOUT,
                        help=f'Timeout in seconds for each probe (default: {DEFAULT_TIMEOUT})')
    parser.add_argument('--probes', '-p', type=int, default=DEFAULT_PROBES,
                        help=f'Number of probes per hop (default: {DEFAULT_PROBES})')
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        print(f"Traceroute to {args.destination}, {args.max_hops} hops max, {args.timeout}s timeout")
        print()
        
        # Perform traceroute
        send_probes(
            destination=args.destination,
            max_hops=args.max_hops,
            timeout=args.timeout,
            probes_per_hop=args.probes
        )
        
    except KeyboardInterrupt:
        print("\nTraceroute stopped by user.")
    except Exception as e:
        print(f"Error during traceroute: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 