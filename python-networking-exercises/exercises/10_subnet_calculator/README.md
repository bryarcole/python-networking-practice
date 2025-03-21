# Exercise 10: Subnet Calculator

In this exercise, you'll create a subnet calculator that performs various subnet calculations and manages IP addressing. This will help you understand subnet mathematics, CIDR notation, and network planning.

## Objectives
- Master IP addressing concepts and binary operations
- Implement subnet calculations
- Work with CIDR notation
- Create subnet planning tools
- Visualize network addressing schemes

## Tasks

### 1. Basic Subnet Calculator
Create a script (`subnet_calc.py`) that:
- Calculates network and broadcast addresses from an IP and subnet mask
- Determines the number of available hosts in a subnet
- Converts between subnet masks and CIDR prefix lengths
- Validates IP addresses and subnet masks
- Shows binary representations of addresses

### 2. Subnet Divider
Create a script (`subnet_divider.py`) that:
- Divides a network into multiple subnets
- Calculates optimal subnet sizes based on host requirements
- Ensures no IP address space is wasted
- Provides details for each subnet (network address, broadcast address, IP range)
- Handles both equal and variable-sized subnetting

### 3. VLSM Calculator
Create a script (`vlsm_calculator.py`) that:
- Implements Variable Length Subnet Masking (VLSM)
- Takes a list of networks with host requirements
- Allocates address space efficiently
- Creates a hierarchical IP addressing plan
- Prevents subnet overlaps

### 4. Subnet Visualizer
Create a script (`subnet_visualizer.py`) that:
- Visualizes network address spaces
- Shows subnet hierarchy
- Displays utilization of address space
- Identifies potential conflicts or overlaps
- Exports visualizations to files (text, HTML, or graphical formats)

## Example Usage

```
# Calculate subnet information
python subnet_calc.py --ip 192.168.1.0 --mask 255.255.255.0

# Divide network into equal subnets
python subnet_divider.py --network 10.0.0.0/16 --subnets 4

# Calculate VLSM for multiple networks
python vlsm_calculator.py --network 172.16.0.0/16 --requirements "500,100,50,25,10"

# Visualize subnet hierarchy
python subnet_visualizer.py --network 192.168.0.0/16 --output subnet_map.html
```

## Tips
- Always consider edge cases like broadcast/network addresses
- Remember that usable hosts = total hosts - 2 (for IPv4)
- Pay attention to the binary math involved in subnetting
- Use libraries like `ipaddress` but also implement manual calculations to understand the process
- Test your calculator against known good examples
- Consider the special cases of /31 and /32 subnets

## Expected Outcome
You should have a functional subnet calculator that can perform various subnet calculations, divide networks efficiently, and visualize subnet hierarchies. This tool should help you understand and manage IP addressing schemes.

## Bonus Challenges
1. Add IPv6 support to all calculator functions
2. Implement supernetting/route summarization
3. Create a network design tool that optimizes address space
4. Add network scenario simulations (e.g., branch offices, VLANs) 