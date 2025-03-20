#!/usr/bin/env python3
"""
HTML Parser - Web Scraping Exercise

This script demonstrates how to parse HTML content using BeautifulSoup.
"""

import requests
import sys
import argparse
from bs4 import BeautifulSoup
from collections import Counter
from requests.exceptions import RequestException

def fetch_webpage(url):
    """
    Fetch a webpage and return its content.
    
    Args:
        url (str): The URL to fetch
        
    Returns:
        str: The HTML content of the page
        
    Raises:
        RequestException: If the request fails
    """
    # TODO: Implement webpage fetching
    pass

def parse_html(html_content):
    """
    Parse HTML content using BeautifulSoup.
    
    Args:
        html_content (str): HTML content to parse
        
    Returns:
        BeautifulSoup: Parsed HTML
    """
    # TODO: Implement HTML parsing
    pass

def extract_elements(soup):
    """
    Extract and display various elements from parsed HTML.
    
    Args:
        soup (BeautifulSoup): Parsed HTML
        
    Returns:
        dict: Dictionary containing extracted elements
    """
    # TODO: Extract headings (h1, h2, h3)
    
    # TODO: Extract paragraphs
    
    # TODO: Extract links
    
    # TODO: Extract images
    
    # Create a dictionary with the extracted elements
    elements = {
        'headings': [],
        'paragraphs': [],
        'links': [],
        'images': []
    }
    
    return elements

def count_tags(soup):
    """
    Count the occurrence of different HTML tags.
    
    Args:
        soup (BeautifulSoup): Parsed HTML
        
    Returns:
        Counter: Counter object with tag counts
    """
    # TODO: Implement tag counting
    pass

def display_results(elements, tag_counts):
    """
    Display the extracted elements and tag counts.
    
    Args:
        elements (dict): Dictionary containing extracted elements
        tag_counts (Counter): Counter object with tag counts
    """
    # TODO: Implement results display
    pass

def main():
    """Main function to demonstrate HTML parsing."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Parse HTML content from a webpage')
    parser.add_argument('--url', default='https://example.com',
                        help='URL to fetch and parse (default: https://example.com)')
    args = parser.parse_args()
    
    try:
        # Fetch the webpage
        html_content = fetch_webpage(args.url)
        
        # Parse the HTML
        soup = parse_html(html_content)
        
        # Extract elements
        elements = extract_elements(soup)
        
        # Count tags
        tag_counts = count_tags(soup)
        
        # Display results
        display_results(elements, tag_counts)
        
    except RequestException as e:
        print(f"Error: Failed to fetch the webpage: {e}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    sys.exit(main()) 