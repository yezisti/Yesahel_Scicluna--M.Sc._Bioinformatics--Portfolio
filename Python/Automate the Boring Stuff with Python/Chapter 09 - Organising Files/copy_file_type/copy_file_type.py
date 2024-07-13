'''
copy_file_type.py: finds and makes copies of files of a specified file extension

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 9. Practice Project - Selective Copy
- Task Description: see README.md
'''

def copy_file_type(folder, file_ext):
    '''
    Args:
    - folder(str.): the path of the folder tree to search
    - file_ext(str.): the file extension (e.g. '.pdf', '.txt', '.csv', etc.) to use as a search filter

    Output:
    - creates a new folder containing a copy of each file of specified extension that is present within the specified folder tree
    '''

    import os, shutil
    
    # Gets the absolute path of the specified folder
    folder = os.path.abspath(folder)

    # Creates a new folder within 'Documents' in which to save the copied files
    home_dir = os.path.expanduser("~")
    copy_dir = os.path.join(home_dir, 'Documents', (file_ext.upper()[1:] + ' Copies'))
    os.mkdir(copy_dir)

    # Walks the specified folder tree
    for folder_name, subfolders, file_names in os.walk(folder):

        # Iterates over every file in the folder tree
        for file_name in file_names:

            # Evaluates True if the current file is of the specified extension and has not already been copied
            if file_name.endswith(file_ext.lower()) and not os.path.isfile(os.path.join(copy_dir, file_name)):

                # Informs the user of the function's progress
                print('Copying %s...' %(file_name))

                # Copies the current file to the new folder
                try:
                    shutil.copy(os.path.join(folder_name, file_name), copy_dir)
                except OSError:
                    continue

    # Directs the user to the folder of the function's output   
    print('\nDone. Copied %s files to:\n%s' %(file_ext.upper()[1:], copy_dir))
