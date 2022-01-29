# -*- coding: utf-8 -*-

"""Main module."""
import requests
import json
from os import path
from enum import Enum

HUMBLE_URL = "https://www.humblebundle.com/api/v1/order/{}?wallet_data=true"


class BookFormat(Enum):
    PDF = "pdf"
    EPUB = "epub"
    MOBI = "mobi"
    PRC = "prc"
    ALL = "all"


def select_format(books, format: BookFormat):
    for book in books:
        for download in book:
            file_format = download["file_format"]
            if file_format == format.value or format == BookFormat.ALL:
                yield download


def get_page(key):
    raw_json = requests.get(HUMBLE_URL.format(key)).content
    data = json.loads(raw_json)
    return data


def get_downloads(book_name, download):
    download_struct = download["download_struct"]
    for link in download_struct:
        yield {
            "book_name": book_name,
            "file_format": link["name"].lower(),
            "url_download": link["url"]["web"]
        }


def get_books_to_download(data):
    products = data["subproducts"]
    for book in products:
        for download in book["downloads"]:
            yield get_downloads(book["machine_name"], download)


def download_a_book(root_folder, book):
    url_to_download_from = book["url_download"]
    book_title = book["book_name"]
    file_format = book["file_format"]
    book_filename = f"{book_title}.{file_format}"

    book_data = requests.get(url_to_download_from)

    with open(path.join(root_folder, book_filename), 'wb') as myBook:
        size = book_data.headers['Content-Length']
        if size == 0:
            print("Could not download:" + book_title + "." + file_format.lower())
        for chunk in book_data.iter_content():
            myBook.write(chunk)
