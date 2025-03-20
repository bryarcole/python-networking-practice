# Exercise 5: Simple Web Server

In this exercise, you'll learn how to create a basic HTTP web server using Python. You'll implement both a low-level socket-based server and a higher-level Flask-based server.

## Objectives
- Understand HTTP request/response cycle
- Implement a web server using raw sockets
- Create a web application using Flask
- Handle different HTTP methods (GET, POST)
- Serve static files and dynamic content

## Tasks

### 1. Socket-Based HTTP Server
Create a script (`socket_server.py`) that:
- Uses the socket library to create a basic HTTP server
- Listens on localhost port 8000
- Handles basic GET requests
- Serves HTML content
- Parses HTTP headers
- Handles multiple requests in sequence

### 2. Static File Server
Create a script (`file_server.py`) that:
- Enhances the socket server to serve static files
- Serves different content types (HTML, CSS, JavaScript, images)
- Sets appropriate Content-Type headers
- Handles 404 errors for missing files
- Implements basic directory listing

### 3. Flask Web Application
Create a script (`flask_app.py`) that:
- Uses Flask to create a web application
- Implements multiple routes
- Creates a basic web form
- Handles form submissions
- Uses templates for rendering HTML
- Implements session handling

### 4. RESTful API Server
Create a script (`api_server.py`) that:
- Implements a simple RESTful API with Flask
- Supports CRUD operations on a resource
- Returns JSON responses
- Implements proper HTTP status codes
- Includes basic input validation

## Example Usage

```
# Start the socket-based server
python socket_server.py

# Access in a browser: http://localhost:8000

# For the Flask server
python flask_app.py

# Access in a browser: http://localhost:5000
```

## Tips
- For the socket server, you'll need to manually parse HTTP requests
- Study the HTTP protocol specification to understand requests and responses
- Flask has excellent documentation at https://flask.palletsprojects.com/
- Use the developer tools in your browser to inspect requests and responses
- Test your servers with different browsers to ensure compatibility

## Expected Outcome
You should have a working web server that can serve both static and dynamic content, and handle basic HTTP requests and responses.

## Bonus Challenge
Implement WebSocket support in your server for real-time communication between the client and server. 