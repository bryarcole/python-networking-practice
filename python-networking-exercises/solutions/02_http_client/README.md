# Exercise 2: HTTP Client Operations

In this exercise, you'll learn how to interact with web servers using the `requests` library, a popular HTTP client library for Python.

## Objectives
- Understand HTTP methods (GET, POST, PUT, DELETE)
- Make HTTP requests using the `requests` library
- Handle response data in different formats (JSON, HTML)
- Work with HTTP headers and query parameters
- Handle authentication and cookies

## Tasks

### 1. Basic HTTP GET Request
Create a script (`basic_get.py`) that:
- Makes a GET request to a public API (like https://httpbin.org/get)
- Prints the response status code, headers, and content
- Handles possible exceptions

### 2. HTTP Methods Explorer
Create a script (`http_methods.py`) that:
- Makes GET, POST, PUT, and DELETE requests to https://httpbin.org/
- For POST and PUT requests, sends some data
- Prints the response from each request
- Compares the differences in responses

### 3. API Data Fetcher
Create a script (`api_data_fetcher.py`) that:
- Fetches data from a public API (like JSONPlaceholder or OpenWeatherMap)
- Parses the JSON response
- Formats and displays specific information from the response
- Allows passing query parameters to filter results

### 4. Web Page Analyzer
Create a script (`web_page_analyzer.py`) that:
- Fetches the content of a web page (like https://example.com)
- Extracts and counts HTML elements (e.g., how many links, images, etc.)
- Analyzes HTTP headers (e.g., server type, content type)
- Reports on response time

## Example Usage

```
python api_data_fetcher.py --limit 5
```

## Tips
- Use the `requests` library for all HTTP operations
- Handle exceptions like connection errors, timeouts, and invalid URLs
- Remember to check the status code of responses
- For JSON APIs, use the `.json()` method to parse responses
- Be respectful of APIs by not making too many requests too quickly

## Expected Outcome
You should be able to interact with various web services, handle different types of HTTP responses, and extract useful information from them.

## Bonus Challenge
Create a script that handles authentication with an API that requires it (like GitHub or Twitter). 