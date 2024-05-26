'''
link_finder.py: searches copied text for website links and copies them back onto the clipboard

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 7 - Pattern Matching with Regular Expressions
- Task: Use regular expressions to automate the task of finding website links.
'''

import pyperclip, re

# RegEx obj. matches links starting with 'http://', 'https://', or 'www.'
# Links must be separated by whitespace in order to be detected
link_regex = re.compile(r'((https?://|www\.)\S+)')

# Stores the contents of the clipboard
text = pyperclip.paste()

matches = []

count = 1

for groups in link_regex.findall(text):                 # Iterates over each match obj.
    link_line = '(' + str(count) + ') ' + groups[0]     # Numbers the match obj.
    matches.append(link_line)                           # Stores the numbered match obj.
    count += 1                                          # Increments the match obj. numbering by 1
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))                  # Copies the list of match obj. onto the clipboard
    print('Copied to clipboard:')
    print('\n'.join(matches))                           # Prints the list of match obj.
else:
    print('No links found.')                            # Handles scenarios where no match is found
