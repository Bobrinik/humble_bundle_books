#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `humble_get` package."""

import pytest
import json

from humble_get import get_books_to_download, download_a_book
from itertools import chain


@pytest.fixture
def data():
    with open("pretty_results.json", mode="r", encoding="utf8") as fp:
        return json.load(fp)


def test_parsing(data):
    assert list(chain.from_iterable(get_books_to_download(data))) == [
        {'book_name': 'threat_modeling_designing_for_security',
         'file_format': 'EPUB',
         'url_download': 'some_url'},
        {'book_name': 'threat_modeling_designing_for_security',
         'file_format': 'PDF',
         'url_download': ''}]


def test_download_a_book():
    book = {
        "book_name": "test_book_name",
        "file_format": "epub",
        "url_download": "https:"
    }
    download_a_book(".", book)
    assert False
