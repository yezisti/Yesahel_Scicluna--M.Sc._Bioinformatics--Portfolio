'''
clip.py: uses shelve files to extend the functionality of the clipboard from the command line; can be used as a secure password manager

Authors: Al Sweigart (base code), Yesahel Scicluna (function expansion)

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 8. Practice Project - Extending the Multiclipboard
- Task Description: see clip.md
'''

user_guide = '''
clip.py - Saves and loads pieces of text to the clipboard

Usage: py.exe clip.py save <keyword> - Saves the current clipboard to the specified keyword
       py.exe clip.py <keyword> - Loads the keyword-associated text to the clipboard
       py.exe clip.py list - Lists all the keywords in use
       py.exe clip.py delete <keyword> - Deletes the text associated with the specified keyword
       py.exe clip.py wipe - Deletes every text associated with every keyword in use'''

import shelve, pyperclip, sys

if len(sys.argv) == 1:  # Evaluates True if no additional command-line arguments are passed 
    print(user_guide)   # Prints a guide on program use 

clip_shelf = shelve.open('clip')    # Creates a shelve file obj. by opening or creating the specified shelve file

if len(sys.argv) == 3:
    
    if sys.argv[1].lower() == 'save':                                                  # Evaluates True if 3 cla are passed, of which the 2nd is <save>                            
        clip_shelf[sys.argv[2]] = pyperclip.paste()                                    # Saves the current clipboard to the keyword specified by the 3rd cla
        print('\nSaved under <' + sys.argv[2] + '>:\n' + clip_shelf[sys.argv[2]])      # Indicates what text has been saved in association with what keyword  
    
    elif sys.argv[1].lower() == 'delete':                                              # Evaluates True if 3 cla are passed, of which the 2nd is <delete>
        print('\nDeleted from <' + sys.argv[2] + '>:\n' + clip_shelf[sys.argv[2]])     # Indicates what keyword and associated text have been deleted
        del clip_shelf[sys.argv[2]]                                                    # Deletes the text associated with the keyword specified by the 3rd cla

elif len(sys.argv) == 2:
     
    if sys.argv[1].lower() == 'list':                                       # Evaluates True if the last of 2 cla passed is <list>
        if len(clip_shelf) > 0:                                             
            print('\nKeys:\n' + '\n'.join(list(clip_shelf.keys())))         # Lists the keywords in use, if any
        else:
            print('\nNo keys in use')                                       # Handles scenarios where no keywords are in use
         
    elif sys.argv[1].lower() == 'wipe':                                     # Evaluates True if the last of 2 cla passed is <wipe>
        for key in clip_shelf.keys():                                       # Iterates over every keyword in use
           del clip_shelf[key]                                              # Deletes the text associated with the current keyword
        print('\nClipboard wiped')                                          # Indicates loop termination
        
    elif sys.argv[1].lower() in clip_shelf:                                 # Evaluates True if the last of 2 cla passed is a keyword in use
        pyperclip.copy(clip_shelf[sys.argv[1]])                             # Loads the text associated with the specified keyword onto the clipboard
        print('\nLoaded to clipboard:\n' + clip_shelf[sys.argv[1]])         # Indicates what text has been loaded onto the clipboard

clip_shelf.close() # Closes the shelve file, saving every piece of clipboard text that has been associated with a keyword to the hard drive
