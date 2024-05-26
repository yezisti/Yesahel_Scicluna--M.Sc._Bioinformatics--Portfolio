'''
socials.py: quickly launches one's social media from the command-line interface

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 11 - Web Scraping
 - Task: Simultaneously open several social network sites that you regularly check without directly opening the web browser
'''

import sys, webbrowser

usage = 'py.exe socials.py - launches your social media'

# Evaluates True if the user only enters 'py.exe socials.py' into the command-line interface
if len(sys.argv) == 1:

    # Launches Facebook, Messenger, Youtube, TikTok, Twitter, and LinkedIn
    webbrowser.open('https://www.facebook.com/')
    webbrowser.open('https://www.messenger.com/')   
    webbrowser.open('https://www.youtube.com/')
    webbrowser.open('https://www.tiktok.com/following?lang=en')
    webbrowser.open('https://twitter.com/?lang=en') 
    webbrowser.open('https://www.linkedin.com/feed/')

# Instructs the user to enter 'py.exe socials.py' if the above condition is not met
else:
    print(usage)
