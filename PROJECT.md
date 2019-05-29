## [Project](https://github.com/Bobrinik/humble_bundle_books)

- It's monotonous to download Humble Bundle books manually so I wrote a python script to do it for me instead.

## Project Difficulties

- Finding out what are the end points for downloading books and what parameters are needed to access it.

## Solution

- At first, I was thinking about using Selenium automation script to go an imitate user actions to download each book. However, it would introduce a dependency for a Selenium framework and it might not work the same way  across different computers.
- Second, I thought it's possible to grab  URLS for download by getting HTML page and then querying HTML with xPath to get them. However, it turned out that the links are in an IFrame that is loaded after the main page is loaded.
- Third, I fired up developer tools and checked network tab to see if there is an endpoint that is returning JSON.  It turned out that there was an endpoint, so I used this for implementing the downloading part in python.

## Technology used

- Python
- Developer tools