# Exercise 3: RESTful API Interaction

In this exercise, you'll learn how to interact with RESTful APIs by building a client for the JSONPlaceholder API, a fake online REST API for testing and prototyping.

## Objectives
- Understand RESTful API principles and conventions
- Interact with all CRUD operations (Create, Read, Update, Delete)
- Parse and process JSON data
- Handle API pagination and filtering
- Create a reusable API client class

## Tasks

### 1. API Client Framework
Create a reusable API client class (`api_client.py`) that:
- Handles base URL configuration
- Provides methods for all HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Handles error responses consistently
- Implements request retries with backoff for failed requests
- Manages session cookies and headers

### 2. Resource Managers
Create resource-specific manager classes for different JSONPlaceholder endpoints:
- `PostManager` for /posts
- `CommentManager` for /comments
- `UserManager` for /users

Each manager should implement appropriate CRUD methods for its resource.

### 3. Command-Line Interface
Create a command-line interface (`jsonplaceholder_cli.py`) that:
- Allows users to interact with all resources
- Supports all CRUD operations with appropriate arguments
- Formats output in a readable way
- Provides help and usage information

## Example Usage

```
# Get all posts
python jsonplaceholder_cli.py posts list

# Get a specific post
python jsonplaceholder_cli.py posts get 1

# Create a new post
python jsonplaceholder_cli.py posts create --title "New Post" --body "This is a new post" --userId 1

# Update a post
python jsonplaceholder_cli.py posts update 1 --title "Updated Title"

# Delete a post
python jsonplaceholder_cli.py posts delete 1
```

## API Reference
Use the JSONPlaceholder API for this exercise:
- Base URL: https://jsonplaceholder.typicode.com
- Resources: /posts, /comments, /albums, /photos, /todos, /users

## Tips
- Read the API documentation at https://jsonplaceholder.typicode.com/guide/
- Use the requests library for all HTTP operations
- Use argparse for command-line argument parsing
- Remember that JSONPlaceholder doesn't actually persist changes
- Implement proper error handling and user feedback

## Expected Outcome
You should have a fully functional command-line client for interacting with the JSONPlaceholder API that demonstrates your understanding of RESTful principles and API interaction patterns.

## Bonus Challenge
Add support for nested resources (e.g., /posts/1/comments) and implement filtering options for the list operations. 