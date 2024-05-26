'''
lucky.py: uses a search term supplied to the command-line in order to open several of the top Google search results

Author: Al Sweigart
- Editor: Yesahel Scicluna (selector in line 22)
    - Justification: The '.r a' selector originally suggested by Al Sweigart is no longer functional

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 11. Project - "I'm Feeling Lucky" Google Search
'''

import requests, sys, webbrowser, bs4

# Displays text while the Google page is being downloaded
print('\nGoogling...')

# Downloads the page containing the links Google provides upon searching with the term supplied to the command-line
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))  # Creates a response object that gets the web page with the search results
res.raise_for_status()  # Raises an expection if there is a problem with the download of the page

# Retrieves the top (<=5) search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')  # Creates a soup object from the response object's text attribute
link_elems = soup.select('div#main > div > div > div > a') # Parses the soup object using the provided selector
num_open = min(5, len(link_elems)) # Stores the number of links to open (5 or less if <5 links are provided by Google)

# Opens a browser tab for each of the top search results
for i in range(num_open):
    webbrowser.open('https://google.com' + link_elems[i].get('href')) # Gets the link's 'href' attribute to use in constructing the working URL
