#!/usr/bin/env python3
"""
Echo Client - Basic Socket Programming Exercise

This is a template for implementing a simple echo client using Python sockets.
"""

import socket
import sys

# Define constants
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8888         # The port used by the server

def main():
    """Main function to run the echo client."""
    # TODO: Create a TCP/IP socket
    
    try:
        # TODO: Connect the socket to the server
        
        print(f"Connected to server at {HOST}:{PORT}")
        
        # TODO: Implement the basic client that sends a single message
        # and receives the echoed response
        
        # TODO: Extend to handle multiple messages until the user types "quit"
        
    except ConnectionRefusedError:
        print(f"Connection to {HOST}:{PORT} refused. Is the server running?")
    except KeyboardInterrupt:
        print("\nClient shutting down...")
    finally:
        # TODO: Clean up the socket
        pass
        
    print("Client shutdown complete")

if __name__ == "__main__":
    main() 