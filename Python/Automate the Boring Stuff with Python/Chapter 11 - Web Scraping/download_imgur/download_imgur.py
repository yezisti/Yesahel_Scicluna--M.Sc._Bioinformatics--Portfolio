'''
download_imgur.py: searches and downloads images from Imgur

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 11. Practice Project - Image Site Downloader
- Task Description: see README.md
'''

import sys, requests, os, bs4

# Derives a search term from the command-line arguments
search_term = ' '.join(sys.argv[1:])

# Creates a folder within 'Downloads' in which to store the downloaded images
home_dir = os.path.expanduser('~')
folder_path = os.path.join(home_dir, 'Downloads', search_term)
os.makedirs(folder_path, exist_ok=True)

# Downloads the web page that contains the search results
url = 'https://imgur.com/search?q=' + search_term
res = requests.get(url)
res.raise_for_status()

# Identfies the images within the downloaded web page
soup = bs4.BeautifulSoup(res.text, 'html.parser')
img_elems = soup.select('a.image-list-link > img')

# Decides the number of images to download
num_of_elems = min(10, len(img_elems)) # Evaluates to 10 or the number of images that result from the search, if less than 10 images result 

for i in range(num_of_elems):

    # Downloads the image
    source  = 'https:' + img_elems[i].get('src')
    res = requests.get(source)
    res.raise_for_status()

    # Saves the image
    image_file = open(os.path.join(folder_path, os.path.basename(source)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

# Directs the user to the location of the program's output
print('Done. Find your images in:\n' + folder_path)