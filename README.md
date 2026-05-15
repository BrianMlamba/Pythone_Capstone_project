# Pythone_Capstone_project 
NAME: BRIAN MLAMBA SOLOMON

Title:BOOK SEARCH TOOL USING PYTHON AND GOOGLE BOOKS API

Project Overview
The Book Search TOOL is a Python tool that uses the Google Books API to find ebooks based on a user’s topic Of interest input . It shows book details like title, author, and rating, helping users quickly find relevant books online.

THE PROBLEM STATEMENT
Students, researchers, and readers often face difficulties finding relevant ebooks online due to information overload and irrelevant search results. This process can be time-consuming and frustrating. To solve this problem, a Python-based Book Search Application was developed to help users quickly find relevant ebooks by simply entering a topic of interest.

TOOLS USED
1) Python programming language
2) Libraries used  requests
                   time
                   dot.env
                   os
3) Google BOOKS API
4) JSON Handling
5) VS Code / Jupyter Notebook

Methodology
1) Importing libraires
-import requests- It is used to send request to Google Books API
-import time-It is used to pause the application for a few seconds
-import os-It helps access environmental variables in the system
-from dotenv import load_dotenv- it imports load_dotenv from the python-dotenv package
-load_dotenv()-loads the API key and at the same time remain private
2) User-input
topic = input("Enter topic: ")- prompts user to enter topic of interest e.g ecology the value is stored in variable topic
3) Search Parameters-retrieved from Google books APi documentation
a) maxResults-sets the number of books to return from Api,it will display 7 books
b) orderBy-sort by relevance will display books related to the topic input first
c) filter_type-filters to show only ebooks
d) PrintType-only books will be displayed and not magazines
4) Api_key retrived
 - os.getenv("Api_key")- It retrieves the API key from the .env file while the "os.getenv()" reads environment variables securely.
5) Building the API URL 
- build the API request URL using an f-string by inserting the parameters above  q= is the user input.

6) Sending Request 
- response = requests.get(url)-Sends a GET request to Google books API 
7) Converting API response to JSON
books_data = response.json()-Converts the API response into Python dictionary format (json) for python to read easily
8) checking the request status
- response.status_code -prints the HTTP response status if its 200 -data retrieved successfully if not print try again later if it returns a status of 503
- time.sleep-it pauses the program for 3 seconds to avoid sending too many requests too quickly.
9) Retrieving Book items
- Retrieves the list of books from the API response.
items = books_data.get("items")
- Checks whether books were found -"if items"
10) Looping through the books
- for book in items: -it loops through each book returned by API
11) Extraction of Book details
-  volume_info = book.get("volumeInfo", {})- it retrieves general book details. title,author and ratings
- access_info = book.get("accessInfo", {})-reveals if pdf is available
- sale_info = book.get("saleInfo", {})-revaeals saleability and price
12) Getting individual books 
- title = volume_info.get("title", "no title")-Retrieves the book title.
-  author = volume_info.get("authors")-shows the authors
-  rating = volume_info.get("averageRating", "No Rating")- displays rating
- ratings_count = volume_info.get("ratingsCount", 0)- displays number of rating if none it inputs zero
13)  Jump/ignore Books Without Authors
-  if not author:
            continue
Checks if author information exists and skips books missing author data
14) Printing (Book Found )
-   print("\nBook found")- it prints the message book found then the details of book in another line
15) PDF available
-  pdf = access_info.get("pdf", {}).get("isAvailable")
16) saleability 
-  saleability = sale_info.get("saleability", "NOT_FOR_SALE")
17) Price details
-  price_info = sale_info.get("retailPrice",{})
18) Amount -actual price of the book
- price = price_info.get("amount","NOT Available")
19) Preview link of book
- it gets for you  Google Books preview URL and the user will be able  to preview the book online.
20) Result output displayed 

Key Insights
- Using .env files and python-dotenv showed the importance of protecting sensitive information such as API keys from the public
- Utilization of API to extract and process data

Conclusion
The Python Book Search tool successfully showed how APIs can be integrated into applications to extract and process data.
        
Resources/ References
1) Google API documentation
