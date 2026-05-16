import streamlit as st
import requests
import time

st.title("📚 Book Search App (Google Books API)")

# INPUT FROM USER (Streamlit way)
topic = st.text_input("Enter a topic to search books")

maxResults = 7
orderBy = "relevance"
filter_type = "ebooks"
printType = "books"

# GET API KEY FROM STREAMLIT SECRETS
Api_key = st.secrets["Api_key"]

if topic:
    # BUILD URL
    url = f"https://www.googleapis.com/books/v1/volumes?q={topic}&orderBy={orderBy}&filter={filter_type}&printType={printType}&maxResults={maxResults}&key={Api_key}"

    # REQUEST
    response = requests.get(url)
    time.sleep(1)

    if response.status_code == 200:
        st.success("Books loaded successfully 🎉")
        books_data = response.json()

        items = books_data.get("items")

        if items:
            for book in items:
                volume_info = book.get("volumeInfo", {})
                access_info = book.get("accessInfo", {})
                sale_info = book.get("saleInfo", {})

                title = volume_info.get("title", "No title")
                authors = volume_info.get("authors")
                rating = volume_info.get("averageRating", "No Rating")
                ratings_count = volume_info.get("ratingsCount", 0)

                if not authors:
                    continue

                pdf = access_info.get("pdf", {}).get("isAvailable")
                saleability = sale_info.get("saleability", "NOT_FOR_SALE")
                price = sale_info.get("retailPrice", {}).get("amount", "Not Available")
                preview_link = volume_info.get("previewLink")

                st.subheader(title)
                st.write("👨Author:", authors)
                st.write("⭐ Rating:", rating)
                st.write("📊 Ratings Count:", ratings_count)
                st.write("💰 Price:", price)
                st.write("📄 PDF Available:", pdf)
                st.write("🔗 Preview:", preview_link)
                st.markdown("---")

    else:
        st.error("Server is temporarily busy. Try again later.")

        