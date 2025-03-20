#!/usr/bin/env python3
"""
Socket-Based HTTP Server - Web Server Exercise

This script demonstrates how to create a basic HTTP server using Python's socket library.
"""

import socket
import sys
import os
import datetime
import threading
import signal

# Server configuration
HOST = '127.0.0.1'
PORT = 8000
BUFFER_SIZE = 1024
DEFAULT_RESPONSE = b"""
<!DOCTYPE html>
<html>
<head>
    <title>Python Socket Server</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
        h1 { color: #333; }
    </style>
</head>
<body>
    <h1>Hello from Python Socket Server!</h1>
    <p>This page is being served by a basic HTTP server implemented using Python sockets.</p>
    <p>Current time: {time}</p>
</body>
</html>
"""

def parse_http_request(request_data):
    """
    Parse the HTTP request.
    
    Args:
        request_data (bytes): The raw HTTP request data
        
    Returns:
        dict: Parsed HTTP request with method, path, headers
    """
    # TODO: Implement HTTP request parsing
    # Parse the request line (GET /path HTTP/1.1)
    # Parse the headers
    # Return a dictionary with the request components
    
    # Sample structure:
    request = {
        'method': '',
        'path': '',
        'version': '',
        'headers': {}
    }
    
    return request

def create_http_response(status_code, status_text, headers, body):
    """
    Create an HTTP response.
    
    Args:
        status_code (int): HTTP status code
        status_text (str): HTTP status text
        headers (dict): HTTP headers
        body (bytes): Response body
        
    Returns:
        bytes: The complete HTTP response
    """
    # TODO: Implement HTTP response creation
    # Format: HTTP/1.1 {status_code} {status_text}\r\n{headers}\r\n\r\n{body}
    
    response = b""
    return response

def handle_client(client_socket, client_address):
    """
    Handle a client connection.
    
    Args:
        client_socket (socket): The client socket
        client_address (tuple): The client address
    """
    try:
        # TODO: Receive the HTTP request
        pass
        
        # TODO: Parse the HTTP request
        
        # TODO: Handle the request (for now, just return a default response)
        
        # TODO: Create and send the HTTP response
        
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        # Close the client socket
        client_socket.close()

def run_server():
    """Run the HTTP server."""
    # TODO: Create a TCP/IP socket
    
    # TODO: Bind the socket to the address and port
    
    # TODO: Listen for incoming connections
    
    print(f"Server started on http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop the server...")
    
    try:
        while True:
            # TODO: Accept a client connection
            pass
            
            # TODO: Handle the client in a separate thread
            
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        # TODO: Clean up the socket
        pass
        
    print("Server shutdown complete")

if __name__ == "__main__":
    run_server() 