# Exercise 6: URL Shortener Service

In this exercise, you'll build a simple URL shortener service similar to bit.ly or tinyurl.com. This project will help you practice web application development, database interactions, and HTTP redirects.

## Objectives
- Create a web service with Flask
- Implement URL shortening algorithm
- Store and retrieve URLs from a database
- Handle HTTP redirects
- Create a simple web frontend

## Tasks

### 1. URL Shortening Algorithm
Create a module (`shortener.py`) that:
- Implements a URL shortening algorithm (e.g., base62 encoding, hash)
- Ensures short URLs are unique
- Validates incoming URLs
- Generates short, readable URL identifiers

### 2. Database Backend
Create a module (`database.py`) that:
- Implements storage for URL mappings
- Provides functions to save and retrieve URLs
- Handles collisions in short URL generation
- Supports optional URL expiration
- Tracks basic usage statistics (clicks, etc.)

### 3. Web Application
Create a Flask application (`app.py`) that:
- Provides an API endpoint to shorten URLs
- Handles redirects from short URLs to original URLs
- Implements rate limiting to prevent abuse
- Includes basic error handling
- Returns appropriate HTTP status codes

### 4. Frontend Interface
Create HTML templates that:
- Provide a user interface for URL shortening
- Display the shortened URL to the user
- Show basic statistics for a short URL
- Include a simple, responsive design

## Example Usage

```
# Start the Flask application
python app.py

# Access in a browser: http://localhost:5000
# Enter a URL to shorten: https://www.example.com/very/long/path/to/something
# Get back: http://localhost:5000/abc123
```

## Tips
- Use SQLite for simple storage without external database dependencies
- Consider using Flask-SQLAlchemy for database interactions
- Implement proper URL validation (not all strings are valid URLs)
- Think about how to handle malicious URLs
- Use a simple, non-predictable algorithm for URL generation
- Remember to handle edge cases (e.g., what if the short URL doesn't exist?)

## Expected Outcome
You should have a functional URL shortener service that can take long URLs, create short aliases, and redirect users from the short URL to the original URL.

## Bonus Challenges
1. Add user accounts to track and manage shortened URLs
2. Implement custom short URLs (allow users to choose their short URL)
3. Add URL expiration functionality
4. Create an API key system for programmatic access to the service 