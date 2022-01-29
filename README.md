# CLI for getting your Humble Bundle Books
Humble book bundles are hard to download from the order page.

![](https://raw.githubusercontent.com/Bobrinik/humble_bundle_books/master/resources/page.png)

If you are going to click on the download button you are going to end up with one popup window per book.
Which is a painfull UX to say the least.

So, I decided to implement a `command line app in Python` that would make it easier to download books from the order page
into a directory of my choosing.

## Installation
```bash
pip install humble-get
```

## How to use it?
In order to use this script, you would need to have a humble bundle `key`.

You can get it by checking the URL right after buying your bundle.
![](https://raw.githubusercontent.com/Bobrinik/humble_bundle_books/master/resources/img.png)

```bash
https://www.humblebundle.com/downloads?key=YOUR_KEY

humble_get -key YOUR_KEY -format epub -p ./my/books/directory
# OR
humble_get -key YOUR_KEY -format pdf -p ./my/books/directory
# OR
humble_get -key YOUR_KEY -format all -p ./my/books/directory
```
