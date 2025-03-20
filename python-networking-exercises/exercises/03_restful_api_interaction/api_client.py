#!/usr/bin/env python3
"""
RESTful API Client - API Interaction Exercise

This module provides a reusable API client for interacting with RESTful APIs.
"""

import requests
import time
import json
import logging
from urllib.parse import urljoin
from requests.exceptions import RequestException, Timeout, ConnectionError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class APIClient:
    """A reusable client for interacting with RESTful APIs."""
    
    def __init__(self, base_url, timeout=10, max_retries=3, backoff_factor=0.5):
        """
        Initialize the API client.
        
        Args:
            base_url (str): The base URL of the API.
            timeout (int): The timeout for requests in seconds.
            max_retries (int): Maximum number of retries for failed requests.
            backoff_factor (float): Backoff factor for retries.
        """
        # TODO: Initialize the class attributes
        
        # TODO: Create a requests session
        
    def _make_request(self, method, endpoint, **kwargs):
        """
        Make an HTTP request to the API.
        
        Args:
            method (str): The HTTP method to use.
            endpoint (str): The API endpoint to request.
            **kwargs: Additional arguments to pass to requests.
            
        Returns:
            dict: The JSON response data.
            
        Raises:
            Exception: If the request fails after all retries.
        """
        # TODO: Implement request with retry logic
        pass
    
    def get(self, endpoint, params=None):
        """Make a GET request to the API."""
        # TODO: Implement GET method
        pass
    
    def post(self, endpoint, data=None, json=None):
        """Make a POST request to the API."""
        # TODO: Implement POST method
        pass
    
    def put(self, endpoint, data=None, json=None):
        """Make a PUT request to the API."""
        # TODO: Implement PUT method
        pass
    
    def patch(self, endpoint, data=None, json=None):
        """Make a PATCH request to the API."""
        # TODO: Implement PATCH method
        pass
    
    def delete(self, endpoint):
        """Make a DELETE request to the API."""
        # TODO: Implement DELETE method
        pass

# Example resource manager class
class ResourceManager:
    """Base class for API resource managers."""
    
    def __init__(self, api_client, resource_path):
        """
        Initialize the resource manager.
        
        Args:
            api_client (APIClient): The API client to use.
            resource_path (str): The path to the resource.
        """
        # TODO: Initialize the resource manager
        pass
    
    def list(self, params=None):
        """Get a list of resources."""
        # TODO: Implement list method
        pass
    
    def get(self, resource_id):
        """Get a specific resource by ID."""
        # TODO: Implement get method
        pass
    
    def create(self, data):
        """Create a new resource."""
        # TODO: Implement create method
        pass
    
    def update(self, resource_id, data):
        """Update a resource."""
        # TODO: Implement update method
        pass
    
    def delete(self, resource_id):
        """Delete a resource."""
        # TODO: Implement delete method
        pass

# Example of how to use the client
def main():
    """Example usage of the API client."""
    # Base URL for JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Create an instance of the API client
    api_client = APIClient(base_url)
    
    # Example: Get all posts
    # TODO: Implement example usage
    
    # Example: Create a new post
    # TODO: Implement example usage
    
    # Example: Update a post
    # TODO: Implement example usage
    
    # Example: Delete a post
    # TODO: Implement example usage

if __name__ == "__main__":
    main() 