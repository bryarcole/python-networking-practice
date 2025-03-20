#!/usr/bin/env python3
"""
Echo Server - Basic Socket Programming Exercise

This is a template for implementing a simple echo server using Python sockets.
"""

import socket
import sys

# Define constants
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8888         # Port to listen on (non-privileged ports are > 1023)

def main():
    """Main function to run the echo server."""
    # TODO: Create a TCP/IP socket
    
    # TODO: Bind the socket to the address and port
    
    # TODO: Listen for incoming connections (make the socket a listening socket)
    
    print(f"Server started on {HOST}:{PORT}")
    print("Waiting for a connection...")
    
    try:
        while True:
            # TODO: Wait for a connection
            
            # TODO: Print connection information
            
            try:
                # TODO: Receive and echo data in a loop
                pass
                
            finally:
                # TODO: Clean up the connection
                pass
                
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        # TODO: Clean up the socket
        pass
        
    print("Server shutdown complete")

if __name__ == "__main__":
    main() 