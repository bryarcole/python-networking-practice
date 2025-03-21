#!/usr/bin/env python3
"""
Subnet Calculator - Subnet Calculator Exercise

This script performs subnet calculations based on an IP address and subnet mask.
"""

import argparse
import sys
import ipaddress

def ip_to_binary(ip_address):
    """
    Convert an IP address to its binary representation.
    
    Args:
        ip_address (str): The IP address to convert
        
    Returns:
        str: Binary representation with dots between octets
    """
    # TODO: Implement conversion to binary
    # Convert each octet to binary representation
    pass

def mask_to_cidr(subnet_mask):
    """
    Convert a subnet mask to CIDR prefix length.
    
    Args:
        subnet_mask (str): The subnet mask (e.g., 255.255.255.0)
        
    Returns:
        int: The CIDR prefix length
    """
    # TODO: Implement mask to CIDR conversion
    # Count the number of 1's in the binary representation
    pass

def cidr_to_mask(prefix_length):
    """
    Convert a CIDR prefix length to subnet mask.
    
    Args:
        prefix_length (int): The CIDR prefix length
        
    Returns:
        str: The subnet mask
    """
    # TODO: Implement CIDR to mask conversion
    # Create a mask with the specified number of 1's followed by 0's
    pass

def calculate_network_address(ip_address, subnet_mask):
    """
    Calculate the network address from an IP and subnet mask.
    
    Args:
        ip_address (str): The IP address
        subnet_mask (str): The subnet mask
        
    Returns:
        str: The network address
    """
    # TODO: Implement network address calculation
    # Perform a bitwise AND between the IP and mask
    pass

def calculate_broadcast_address(ip_address, subnet_mask):
    """
    Calculate the broadcast address from an IP and subnet mask.
    
    Args:
        ip_address (str): The IP address
        subnet_mask (str): The subnet mask
        
    Returns:
        str: The broadcast address
    """
    # TODO: Implement broadcast address calculation
    # Invert the subnet mask and OR with the network address
    pass

def calculate_host_range(network_address, broadcast_address):
    """
    Calculate the range of usable host addresses.
    
    Args:
        network_address (str): The network address
        broadcast_address (str): The broadcast address
        
    Returns:
        tuple: (first_usable_ip, last_usable_ip)
    """
    # TODO: Implement host range calculation
    # First usable IP is network address + 1
    # Last usable IP is broadcast address - 1
    pass

def calculate_hosts(prefix_length):
    """
    Calculate the number of usable hosts in a subnet.
    
    Args:
        prefix_length (int): The CIDR prefix length
        
    Returns:
        int: Number of usable hosts
    """
    # TODO: Implement host calculation
    # 2^(32-prefix_length) - 2 (subtract network and broadcast addresses)
    # Handle special cases of /31 and /32
    pass

def display_subnet_info(ip_address, subnet_mask):
    """
    Display subnet information for the given IP and mask.
    
    Args:
        ip_address (str): The IP address
        subnet_mask (str): The subnet mask
    """
    # TODO: Implement display function
    # Calculate and display all subnet information
    pass

def main():
    """Main function to run the subnet calculator."""
    parser = argparse.ArgumentParser(description='Subnet Calculator')
    
    # Add IP address argument (required)
    parser.add_argument('--ip', required=True,
                        help='IP address (e.g., 192.168.1.0)')
    
    # Add subnet mask argument (required)
    mask_group = parser.add_mutually_exclusive_group(required=True)
    mask_group.add_argument('--mask',
                           help='Subnet mask (e.g., 255.255.255.0)')
    mask_group.add_argument('--cidr', type=int,
                           help='CIDR prefix length (e.g., 24)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Validate IP address
    try:
        ipaddress.IPv4Address(args.ip)
    except ValueError:
        print(f"Error: '{args.ip}' is not a valid IPv4 address.")
        return 1
    
    # Determine subnet mask from arguments
    if args.mask:
        try:
            ipaddress.IPv4Address(args.mask)
            subnet_mask = args.mask
        except ValueError:
            print(f"Error: '{args.mask}' is not a valid subnet mask.")
            return 1
    else:  # args.cidr is provided
        if args.cidr < 0 or args.cidr > 32:
            print(f"Error: CIDR prefix '{args.cidr}' is out of range (0-32).")
            return 1
        subnet_mask = cidr_to_mask(args.cidr)
    
    # Display subnet information
    try:
        display_subnet_info(args.ip, subnet_mask)
    except Exception as e:
        print(f"Error calculating subnet information: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 