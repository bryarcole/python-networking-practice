# Exercise 1: Basic Socket Programming

In this exercise, you'll learn the fundamentals of socket programming in Python by creating a simple client-server application.

## Objectives
- Understand the basics of the TCP/IP protocol
- Create a server that listens for connections
- Create a client that connects to the server
- Send and receive data between client and server

## Tasks

### 1. Echo Server
Create a simple echo server (`echo_server.py`) that:
- Listens on localhost port 8888
- Accepts connections from clients
- Receives data from the client
- Echoes the received data back to the client
- Handles multiple client connections (one at a time)
- Gracefully handles client disconnections

### 2. Echo Client
Create a client (`echo_client.py`) that:
- Connects to the echo server
- Sends a message to the server
- Receives and displays the echoed message
- Gracefully closes the connection

### 3. Multi-message Client
Extend your client to:
- Send multiple messages to the server
- Continue until the user enters "quit"
- Display all responses from the server

## Example Usage

1. Start the server in one terminal:
```
python echo_server.py
```

2. Start the client in another terminal:
```
python echo_client.py
```

3. Type messages in the client terminal and see them echoed back.

## Tips
- Use the `socket` module in Python
- Remember to close sockets when done
- Handle exceptions appropriately
- For the server, use `bind()`, `listen()`, and `accept()`
- For the client, use `connect()`
- Use `recv()` and `send()` for data transfer

## Expected Outcome
You should be able to send messages from the client to the server and see them echoed back. The server should handle client connections and disconnections gracefully.

## Bonus Challenge
Make the server handle multiple clients simultaneously using threading or select. 