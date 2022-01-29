# -*- coding: utf-8 -*-

"""Console script for humble_get."""
import sys
import click
from .humble_get import get_page, get_books_to_download, select_format, download_a_book, BookFormat
from tqdm import tqdm


@click.command()
@click.option("-key", "--humble-key", required=True, help="Key that you find in the URL of your Humble Bundle order")
@click.option("-p", "--target-path", type=click.Path(exists=True), help="Location where books will be saved")
@click.option("-format", "--book-format", type=click.Choice([b_format.value for b_format in BookFormat]), default="all",
              help="Specify format of the books to download")
@click.option("-dry-run", "--dry-run", default=False, help="If set to true, will only output file names to download")
def main(humble_key, target_path, book_format, dry_run):
    """Console script for humble_get."""
    book_format = BookFormat(book_format)

    data = get_page(humble_key)
    books = get_books_to_download(data)
    books_to_download = [b for b in select_format(books, book_format)]

    for book_to_download in tqdm(books_to_download):
        if dry_run:
            print(f"Book: {book_to_download['book_name']}.{book_to_download['file_format']}")
        else:
            download_a_book(target_path, book_to_download)
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise ValueError("Provide humble bundle key")
    sys.exit(main())  # pragma: no cover
