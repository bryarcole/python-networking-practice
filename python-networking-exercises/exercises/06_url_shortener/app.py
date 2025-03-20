#!/usr/bin/env python3
"""
URL Shortener Web Application - URL Shortener Exercise

This script implements a simple URL shortener service using Flask.
"""

from flask import Flask, render_template, request, redirect, url_for, flash, abort, jsonify
import os
import time
from datetime import datetime

# Import the URL shortener module and database module
# You'll need to implement these modules
# from shortener import generate_short_id, validate_url
# from database import save_url, get_original_url, update_stats

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # For flash messages

# Configuration
HOST = '127.0.0.1'
PORT = 5000
BASE_URL = f'http://{HOST}:{PORT}'

@app.route('/')
def index():
    """Render the home page with the URL submission form."""
    # TODO: Implement the index route
    # Should render a template with a form for URL submission
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Create a shortened URL from the submitted URL."""
    # TODO: Implement URL shortening
    # 1. Get the URL from the form
    # 2. Validate the URL
    # 3. Generate a short URL identifier
    # 4. Save the mapping to the database
    # 5. Return the shortened URL to the user
    
    # Example implementation:
    original_url = request.form.get('url', '')
    
    # For now, just return a dummy response
    short_id = "abc123"  # Replace with actual implementation
    short_url = f"{BASE_URL}/{short_id}"
    
    return render_template('shortened.html', original_url=original_url, short_url=short_url)

@app.route('/<short_id>')
def redirect_to_url(short_id):
    """Redirect the user to the original URL based on the short ID."""
    # TODO: Implement URL redirection
    # 1. Look up the original URL from the database
    # 2. If found, update click statistics and redirect the user
    # 3. If not found, show a 404 error
    
    # Example implementation:
    original_url = None  # Replace with database lookup
    
    if original_url:
        # Update statistics
        return redirect(original_url)
    else:
        abort(404)

@app.route('/stats/<short_id>')
def url_stats(short_id):
    """Show statistics for a shortened URL."""
    # TODO: Implement statistics view
    # 1. Look up the URL and stats from the database
    # 2. Render a template with the statistics
    
    # Example implementation:
    url_data = None  # Replace with database lookup
    
    if url_data:
        return render_template('stats.html', url_data=url_data)
    else:
        abort(404)

@app.route('/api/shorten', methods=['POST'])
def api_shorten_url():
    """API endpoint for URL shortening."""
    # TODO: Implement API endpoint
    # 1. Get the URL from the JSON request
    # 2. Validate the URL
    # 3. Generate a short URL
    # 4. Return JSON response with the short URL
    
    # Example implementation:
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'Missing URL parameter'}), 400
    
    original_url = data['url']
    
    # For now, just return a dummy response
    short_id = "abc123"  # Replace with actual implementation
    short_url = f"{BASE_URL}/{short_id}"
    
    return jsonify({
        'original_url': original_url,
        'short_url': short_url,
        'short_id': short_id,
        'created_at': datetime.now().isoformat()
    })

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

def main():
    """Main function to run the Flask application."""
    app.run(host=HOST, port=PORT, debug=True)

if __name__ == "__main__":
    main() 