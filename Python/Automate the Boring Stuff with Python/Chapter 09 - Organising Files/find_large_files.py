'''
find_large_files.py: Searches the entirety of a specified folder for files larger than a specified size

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 9. Practice Project - Deleting Unneeded Files
- Task Description: see find_large_files.md
'''

def find_large_files(folder, size_in_MB):
    '''
    Args: 
    - folder(str.): the path of the folder tree to search
    - size_in_MB(int.): the minimum file size (in MB) to use as a search filter

    Prints:
    - the absolute path of the files contained within the specified folder tree that are larger than the specified file size
    '''
    
    import os

    # Gets the absolute path of the specified folder
    folder = os.path.abspath(folder)

    # Informs the user of the search parameters in use
    print('\nSearching %s for files larger than %s MB...\n'
          %(os.path.basename(folder), size_in_MB))

    count = 1
    
    # Walks the specified folder tree
    for folder_name, subfolders, file_names in os.walk(folder):
        
        # Iterates over every file in the folder tree
        for file_name in file_names:

            # Gets the absolute path of the current file
            abs_file_path = os.path.join(folder_name, file_name)

            # Prints the current file's absolute path if it is larger than the specified size
            if os.path.getsize(abs_file_path) > int(size_in_MB)*1000000:
                print('(%s) ' %(count) + abs_file_path)
                count += 1

    # Informs the user of the search's completion
    print('\nSearch complete.\n')
