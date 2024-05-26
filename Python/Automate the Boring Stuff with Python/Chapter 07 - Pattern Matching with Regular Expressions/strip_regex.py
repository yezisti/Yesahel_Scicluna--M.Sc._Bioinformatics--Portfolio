'''
strip_regex.py: defines a function that works like the `strip()` method

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 7. Practice Project - Regex Version of strip()
- Task Description: see strip_regex.md
'''

import re

def strip_regex(text, char = '\s'):
    '''
    Args:
    - text(str.): the text to be stripped at its flanks
    - char(str.): the character or characters to strip off the flanks of the text (set to whitespace by default)

    Returns:
    - the text stripped off the specified flanking characters
    '''
    
    regex = re.compile(r'[' + char + ']*' +                                # Matches the characters to strip on the left flank
                        '([^' + char + ']' + '.*' + '[^' + char + '])' +   # Matches the text to be stripped at its flanks
                        '[' + char + ']*',                                 # Matches the characters to strip on the right flank
                        re.DOTALL | re.VERBOSE)              
    try:
        return regex.search(text).group(1)  # Returns the stripped text
    
    # Handles scenarios where text == char
    except AttributeError:
        return 'Error: Text cannot be stripped of itself.' 


# Function tests:
print(strip_regex('helloellohllohe', 'hello'))
print(strip_regex('helloellhelloworld!ohllohe', 'hello'))
print(strip_regex('hihihiHello world!ihihihih', 'hi'))
print(strip_regex('12345Hello world!54321', '12345'))
print(strip_regex('''
                    Hello world!
                                '''))

