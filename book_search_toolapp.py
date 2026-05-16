
import requests
import time
import os
from dotenv import  load_dotenv
load_dotenv()

# GOOGLE BOOKS API PARAMETERS
topic = input("Enter topic: ")
maxResults = 7
orderBy = "relevance"
filter_type = "ebooks"
printType = "books"
Api_key = os.getenv("Api_key")

#BUILDING URL
url = f"https://www.googleapis.com/books/v1/volumes?q={topic}&orderBy={orderBy}&filter={filter_type}&printType={printType}&maxResults={maxResults}&key={Api_key}"

#SENDING REQUEST
response = requests.get(url)
print(response)
time.sleep(3)
books_data = response.json()
if response.status_code == 200:
    print("success")
else:
     print("The Server is Temporarily busy try again later")
     
items = books_data.get("items")
if items:
    for book in items:
        volume_info = book.get("volumeInfo", {})
        access_info = book.get("accessInfo", {})
        sale_info = book.get("saleInfo", {})

        title = volume_info.get("title", "no title")
        author = volume_info.get("authors")
        rating = volume_info.get("averageRating", "No Rating")
        ratings_count = volume_info.get("ratingsCount", 0)
        #skip books without Authors
        if not author:
            continue

        print("\nBook found")

        pdf = access_info.get("pdf", {}).get("isAvailable")
        saleability = sale_info.get("saleability", "NOT_FOR_SALE")
        price_info = sale_info.get("retailPrice",{})
        price = price_info.get("amount","NOT Available")
        preview_link = volume_info.get("previewLink")
    

        print("Title:", title)
        print("Author:", author)
        print("Price:",price)
        print("pdf:",pdf)
        print("rating:",rating)
        print("ratings_count:",ratings_count)
        print("previewLink:",preview_link)
else:
     print("No books available")

        