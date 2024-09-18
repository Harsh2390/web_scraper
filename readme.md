# Yahoo Finance Scraper
This project is a web scraping script that extracts important financial data from Yahoo Finance. Specifically, the script retrieves four types of data:

## **Table of Contents**

- [**Project Overview**](#project-overview)
- [**Features**](#features)
- [**Prerequisites**](#prerequisites)
- [**Installation**](#installation)
- [**Usage**](#usage)
- [**Code Explanation**](#code-explanation)


1. Top Losers - Stocks that have lost the most value in the market.
2. Top Gainers - Stocks that have gained the most value in the market.
3. 52-Week Losers - Stocks that have lost the most value over a 52-week period.
4. 52-Week Gainers - Stocks that have gained the most value over a 52-week period.
This data is crucial for financial analysis and can assist in developing trading strategies. It can be linked to other projects that involve financial analysis or even automated trading systems. The project leverages several Python packages: requests, BeautifulSoup, pandas, and lxml to achieve the task.

## Project Overview
The script scrapes Yahoo Finance using Python's BeautifulSoup library to extract HTML tables containing stock data. It processes the tables into a structured format using the Pandas library, which allows for easy manipulation and analysis. The four datasets (top losers, top gainers, 52-week losers, and 52-week gainers) are printed to the console, and they can also be further used or saved for different analytical purposes.

## Features
Web Scraping: Extracts stock market data from Yahoo Finance.
Data Structuring: Converts the scraped data into a Pandas DataFrame for easier manipulation and analysis.
Four Data Tables: Provides four important stock-related datasets:
- Top Losers
- Top Gainers
- 52-Week Losers
- 52-Week Gainers

## Prerequisites
Before running the script, ensure that the following Python packages are installed:

> requests: For sending HTTP requests to Yahoo Finance and fetching the web pages.
> beautifulsoup4: For parsing and scraping the HTML content of the Yahoo Finance pages.
> xml: Parser required by BeautifulSoup to handle the web pages.
> pandas: For storing and manipulating the extracted stock market data in a DataFrame.

## Installation
1. Clone the repository or download the script.
2. Install the required Python packages by running:
`pip install -r requirements.txt`

## Usage
To use the script, simply run it in a Python environment:
`python3 main.py`

Once the script is executed, it will scrape Yahoo Finance for the four datasets and display the results in the terminal.

## Code Explanation
### Libraries Used
+ requests: This library is used to make HTTP requests to the Yahoo Finance website and fetch the HTML content of the pages.
+ BeautifulSoup: Used for parsing the HTML content fetched from Yahoo Finance. It helps locate and extract the desired tables from the webpage.
+ pandas: Pandas is used to create and manipulate the structured data from the HTML tables into a tabular format (DataFrame).
+ lxml: A parser used by BeautifulSoup to handle and process the HTML content.

## Scrape Function
The function scrape_detail_page(url) takes in a URL as input and returns a Pandas DataFrame with the scraped data.

Steps:

1. Fetching the page: The function makes an HTTP request to the given URL and fetches the webpage content.
2. Parsing HTML: Using BeautifulSoup, it parses the HTML content and locates the specific table containing stock market data.
3. Extracting table headers: The headers of the table (such as stock name, price, change, etc.) are collected and set as column names in the DataFrame.
4. Extracting table rows: The rows of the table are iterated over, and the cell data is collected and inserted into the DataFrame.
5. Returning Data: The final DataFrame, without the last two unnecessary columns, is returned.




