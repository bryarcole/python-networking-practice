# Exercise 7: Chat Application

In this exercise, you'll build a simple chat application with a server and client. This project will help you understand socket-based communication, threading, and real-time data exchange.

## Objectives
- Implement a multi-client chat server
- Create a client application to connect to the server
- Handle concurrent connections using threading
- Implement a simple chat protocol
- Create a basic user interface for the client

## Tasks

### 1. Chat Server
Create a script (`chat_server.py`) that:
- Sets up a socket server that accepts multiple client connections
- Handles client messages and broadcasts them to all connected clients
- Manages client connections and disconnections gracefully
- Implements basic commands (e.g., /help, /list, /quit)
- Tracks connected users and their activity

### 2. Command-Line Chat Client
Create a script (`chat_client.py`) that:
- Connects to the chat server
- Handles user input from the console
- Displays incoming messages from the server
- Processes commands (e.g., /help, /quit)
- Handles server disconnections gracefully

### 3. Enhanced Chat Client
Create an enhanced version (`enhanced_chat_client.py`) that:
- Adds a simple graphical user interface (GUI) using Tkinter
- Displays messages in a scrollable text area
- Provides an input field for typing messages
- Shows a list of connected users
- Includes a status bar with connection information

### 4. Chat Protocol Extensions
Extend the chat application to support:
- Private messaging between users
- User nicknames and status messages
- Message history (show recent messages when a user connects)
- Simple file sharing between users

## Example Usage

```
# Start the server
python chat_server.py

# In another terminal, start a client
python chat_client.py

# Enter a username when prompted
# Type messages to chat
# Use /help to see available commands
```

## Tips
- Use threading to handle multiple connections
- Create a clear protocol for messages between client and server
- Handle exceptions and disconnections gracefully
- Use queues for thread-safe communication
- Structure your code with classes for better organization
- Remember to close sockets when connections end

## Expected Outcome
You should have a functional chat application where multiple clients can connect to a server and exchange messages in real-time.

## Bonus Challenges
1. Implement message encryption for secure chat
2. Add chat rooms so users can join different conversations
3. Create a web-based client using Flask and WebSockets
4. Implement user authentication and persistent accounts 