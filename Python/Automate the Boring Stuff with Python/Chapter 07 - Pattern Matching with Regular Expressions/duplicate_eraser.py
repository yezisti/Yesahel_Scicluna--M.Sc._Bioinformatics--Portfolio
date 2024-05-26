'''
duplicate_eraser.py: uses regular expressions to find and erase a number of common typos within a provided set of text

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 7 - Pattern Matching with Regular Expressions
 - Task: Find common typos such as multiple spaces between words, accidentally repeated words, multiple exclamation marks at the end of sentences, etc.
'''

import pyperclip, re # type: ignore

text = pyperclip.paste()                            # Stores the contents of the clipboard

multi_word = re.compile(r'(\w+)( \1)+', re.I)       # Matches duplicate words
multi_char = re.compile(r'''([ ,.:;?!'"])\1+''')    # Matches duplicate spaces and punctuation marks

text = multi_word.sub(r'\1', text)                  # Removes duplicates words from the text
text = multi_char.sub(r'\1', text)                  # Removes duplicate spaces and punctuation marks from the text    

pyperclip.copy(text)                                # Loads the processed text back onto the clipboard
print('Copied to clipboard:\n' + text)              # Prints the processed text
