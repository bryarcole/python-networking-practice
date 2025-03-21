#!/usr/bin/env python3
"""
Basic HTTP GET Request - HTTP Client Exercise

This script demonstrates how to make a basic HTTP GET request using the requests library.
"""

import requests
import sys
import json
from requests.exceptions import RequestException, Timeout, ConnectionError

def main():
    """Main function to demonstrate HTTP GET requests."""
    # The URL to send the GET request to
    url = "https://httpbin.org/get"
    
    # TODO: Add query parameters to the request (optional)
    
    try:
        # TODO: Make a GET request to the specified URL
        pass
        
        # TODO: Check if the request was successful (status code 200)
        
        # TODO: Print the response status code
        
        # TODO: Print the response headers
        
        # TODO: Print the response content (JSON in this case)
        
    except ConnectionError:
        print(f"Error: Could not connect to {url}. Please check your internet connection.")
        return 1
    except Timeout:
        print(f"Error: The request to {url} timed out.")
        return 1
    except RequestException as e:
        print(f"Error: An error occurred while making the request: {e}")
        return 1
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    sys.exit(main()) 