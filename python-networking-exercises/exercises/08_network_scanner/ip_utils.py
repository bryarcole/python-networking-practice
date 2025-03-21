#!/usr/bin/env python3
"""
IP Address Utilities - Network Scanner Exercise

This module provides utilities for working with IP addresses and subnets.
"""

import ipaddress
import re
import socket
import struct

def is_valid_ip(ip_address):
    """
    Validates if a string is a valid IPv4 address.
    
    Args:
        ip_address (str): The IP address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # TODO: Implement IP validation
    # Hint: Use socket.inet_pton or ipaddress module
    pass

def is_valid_cidr(cidr_notation):
    """
    Validates if a string is a valid CIDR notation (e.g., 192.168.1.0/24).
    
    Args:
        cidr_notation (str): The CIDR notation to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # TODO: Implement CIDR validation
    # Check format and valid IP with subnet mask between 0-32
    pass

def ip_to_binary(ip_address):
    """
    Converts an IP address to its binary representation.
    
    Args:
        ip_address (str): The IP address to convert
        
    Returns:
        str: Binary representation of the IP
    """
    # TODO: Implement IP to binary conversion
    # Convert each octet to binary and concatenate
    pass

def binary_to_ip(binary):
    """
    Converts a binary representation back to an IP address.
    
    Args:
        binary (str): Binary representation of an IP (32 bits)
        
    Returns:
        str: The IP address
    """
    # TODO: Implement binary to IP conversion
    # Group binary into octets and convert to decimal
    pass

def get_ip_range(cidr_notation):
    """
    Generates a list of all IP addresses in a given CIDR range.
    
    Args:
        cidr_notation (str): The CIDR notation (e.g., 192.168.1.0/24)
        
    Returns:
        list: List of all IP addresses in the range
    """
    # TODO: Implement IP range generation
    # Use ipaddress module to generate all IPs in network
    pass

def is_ip_in_subnet(ip_address, subnet_cidr):
    """
    Determines if an IP address is within a specific subnet.
    
    Args:
        ip_address (str): The IP address to check
        subnet_cidr (str): The subnet in CIDR notation
        
    Returns:
        bool: True if the IP is in the subnet, False otherwise
    """
    # TODO: Implement subnet check
    # Use ipaddress module to check if IP is in network
    pass

def get_network_address(cidr_notation):
    """
    Gets the network address from a CIDR notation.
    
    Args:
        cidr_notation (str): The CIDR notation
        
    Returns:
        str: The network address
    """
    # TODO: Implement network address extraction
    # Use ipaddress module to get network address
    pass

def get_broadcast_address(cidr_notation):
    """
    Gets the broadcast address from a CIDR notation.
    
    Args:
        cidr_notation (str): The CIDR notation
        
    Returns:
        str: The broadcast address
    """
    # TODO: Implement broadcast address extraction
    # Use ipaddress module to get broadcast address
    pass

def get_subnet_mask(cidr_notation):
    """
    Gets the subnet mask from a CIDR notation.
    
    Args:
        cidr_notation (str): The CIDR notation
        
    Returns:
        str: The subnet mask in dotted decimal notation
    """
    # TODO: Implement subnet mask extraction
    # Extract prefix length and convert to subnet mask
    pass

def main():
    """Example usage of the IP utilities."""
    # Example IP and CIDR
    ip = "192.168.1.1"
    cidr = "192.168.1.0/24"
    
    # Validate IP and CIDR
    print(f"Is {ip} a valid IP? {is_valid_ip(ip)}")
    print(f"Is {cidr} a valid CIDR? {is_valid_cidr(cidr)}")
    
    # Convert IP to binary and back
    binary = ip_to_binary(ip)
    print(f"Binary representation of {ip}: {binary}")
    print(f"IP from binary: {binary_to_ip(binary)}")
    
    # Get network information
    print(f"Network address of {cidr}: {get_network_address(cidr)}")
    print(f"Broadcast address of {cidr}: {get_broadcast_address(cidr)}")
    print(f"Subnet mask of {cidr}: {get_subnet_mask(cidr)}")
    
    # Check if IP is in subnet
    print(f"Is {ip} in {cidr}? {is_ip_in_subnet(ip, cidr)}")
    
    # Generate first 5 IPs in range
    ip_range = get_ip_range(cidr)[:5]
    print(f"First 5 IPs in {cidr}: {ip_range}")

if __name__ == "__main__":
    main() 