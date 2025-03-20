# Exercise 4: Web Scraping

In this exercise, you'll learn how to extract data from websites using Python's web scraping tools. Web scraping is the process of automatically collecting information from websites.

## Objectives
- Understand the basics of HTML and CSS for web scraping
- Use the BeautifulSoup library to parse HTML
- Extract specific data from web pages
- Navigate through websites by following links
- Handle different page structures and layouts

## Tasks

### 1. HTML Parser
Create a script (`html_parser.py`) that:
- Fetches a web page (e.g., https://example.com)
- Parses the HTML content using BeautifulSoup
- Extracts and displays various elements (headings, paragraphs, links, images)
- Counts the occurrence of different HTML tags

### 2. Data Extractor
Create a script (`data_extractor.py`) that:
- Scrapes a structured website (e.g., a simple blog or news site)
- Extracts specific information (e.g., article titles, dates, authors)
- Formats and saves the data as JSON or CSV
- Includes error handling for missing elements

### 3. Pagination Handler
Create a script (`pagination_handler.py`) that:
- Scrapes multiple pages of a paginated website
- Extracts consistent data across all pages
- Implements rate limiting to be respectful to the server
- Combines all collected data into a single dataset

### 4. Website Crawler
Create a script (`website_crawler.py`) that:
- Starts from a root URL
- Follows links to discover other pages within the same domain
- Creates a site map of discovered pages
- Collects specified information from each page
- Implements depth limiting to prevent infinite crawling

## Example Usage

```
python data_extractor.py --url https://quotes.toscrape.com --output quotes.json
```

## Tips
- Always be respectful of websites' terms of service and robots.txt
- Implement rate limiting to avoid overwhelming servers
- Use CSS selectors and XPath for precise element selection
- Test your scrapers on small subsets before running them on entire sites
- Some websites may block scraping attempts, so be prepared to handle this
- Consider using a headless browser like Selenium for JavaScript-heavy sites

## Expected Outcome
You should be able to extract structured data from websites and store it in a usable format for further analysis or processing.

## Websites for Practice
- https://quotes.toscrape.com (designed for scraping practice)
- https://books.toscrape.com (designed for scraping practice)
- https://news.ycombinator.com (real-world example)
- https://old.reddit.com/r/programming (real-world example)

## Bonus Challenge
Create a script that monitors a website for changes and sends a notification when new content is detected. 