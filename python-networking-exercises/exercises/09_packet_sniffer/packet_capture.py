#!/usr/bin/env python3
"""
Packet Capture - Packet Sniffer Exercise

This script demonstrates how to capture network packets using Python.
Note: This script requires administrative/root privileges to run.
"""

import argparse
import os
import sys
import time
import socket
import struct
import datetime
from scapy.all import sniff, wrpcap, conf

def get_interfaces():
    """
    Get a list of available network interfaces.
    
    Returns:
        list: List of interface names
    """
    # TODO: Implement interface discovery
    # Return a list of available network interfaces
    pass

def packet_callback(packet):
    """
    Callback function called for each captured packet.
    
    Args:
        packet: The captured packet
        
    Returns:
        bool: True to continue capturing, False to stop
    """
    # TODO: Implement packet processing
    # Display basic information about the captured packet
    pass

def capture_packets(interface, count=0, timeout=None, filter_str=None, output_file=None):
    """
    Capture packets from a network interface.
    
    Args:
        interface (str): Network interface to capture packets from
        count (int): Number of packets to capture (0 = infinite)
        timeout (int): Timeout in seconds (None = no timeout)
        filter_str (str): BPF filter string
        output_file (str): File to save captured packets to
    """
    # TODO: Implement packet capture
    # Use scapy.sniff to capture packets
    # Display progress information
    # Save captured packets to a file if specified
    pass

def print_packet_summary(packet):
    """
    Print a summary of a packet.
    
    Args:
        packet: The packet to summarize
    """
    # TODO: Implement packet summary printing
    # Extract and print relevant information from the packet
    pass

def main():
    """Main function to run the packet capture."""
    # Check if running with admin/root privileges
    if os.geteuid() != 0:
        print("Error: This script requires administrative privileges.")
        print("Please run with sudo or as root.")
        return 1
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Capture network packets')
    parser.add_argument('--interface', '-i', help='Network interface to capture from')
    parser.add_argument('--count', '-c', type=int, default=0, 
                        help='Number of packets to capture (0 = infinite)')
    parser.add_argument('--timeout', '-t', type=int, 
                        help='Timeout in seconds')
    parser.add_argument('--filter', '-f', 
                        help='BPF filter string (e.g. "tcp port 80")')
    parser.add_argument('--output', '-o', 
                        help='Output file to save captured packets (.pcap format)')
    parser.add_argument('--list-interfaces', '-l', action='store_true',
                        help='List available interfaces and exit')
    args = parser.parse_args()
    
    # List available interfaces if requested
    if args.list_interfaces:
        interfaces = get_interfaces()
        print("Available interfaces:")
        for interface in interfaces:
            print(f"  - {interface}")
        return 0
    
    # Check if interface is specified
    if not args.interface:
        print("Error: No interface specified.")
        print("Use --list-interfaces to see available interfaces.")
        print("Use --interface to specify an interface.")
        return 1
    
    try:
        print(f"Starting packet capture on {args.interface}...")
        if args.filter:
            print(f"Filter: {args.filter}")
        
        if args.count > 0:
            print(f"Capturing {args.count} packets...")
        else:
            print("Capturing packets (press Ctrl+C to stop)...")
        
        # Start packet capture
        capture_packets(
            interface=args.interface,
            count=args.count,
            timeout=args.timeout,
            filter_str=args.filter,
            output_file=args.output
        )
        
    except KeyboardInterrupt:
        print("\nCapture stopped by user.")
    except Exception as e:
        print(f"Error during packet capture: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 