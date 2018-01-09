import requests
import json
import os
import sys
HUMBLE_URL = "https://www.humblebundle.com/api/v1/order/{}?wallet_data=true"

def getPage(key):
    print(HUMBLE_URL.format(key))
    raw_json = requests.get(HUMBLE_URL.format(key)).content
    data = json.loads(raw_json)
    return data

def get_books(data):
    folder_name = data['product']['machine_name']
    print(folder_name)
    os.makedirs(folder_name, exist_ok=True)
    books = data['subproducts']
    books_number = len(data['subproducts'])
    for book in books:
        save_book(folder_name, book)
        print("Done: "+data['product']['machine_name'])
        books_number = books_number - 1
        print("Books left: "+str(books_number))

def save_book(folder_name, book):
    download_links = book["downloads"]
    for book_data in download_links:
        book_title = book_data["machine_name"]
        print("Downloading:"+book_title)
        for book_link in book_data["download_struct"]:
            file_format = book_link["name"]
            url_download = book_link['url']['web']

            book_data = requests.get(url_download)

            myBook = open(os.path.join(folder_name, os.path.basename(book_title+"."+file_format.lower())), 'wb')
            size = book_data.headers['Content-Length']
            if size == 0:
                print("Could not download:"+book_title+"."+file_format.lower())
            for chunk in book_data.iter_content():
                myBook.write(chunk)

if __name__ == '__main__':
    if len(sys.argv == 1):
        raise ValueError("Provide humble bundle key")
    key = sys.argv[1]
    data = getPage(key)
    data = get_books(data)
