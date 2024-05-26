'''
close_name_gaps.py: goes through files in a specified folder and closes any gaps in the numbering of those files' names

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 9. Practice Project - Filling in the Gaps
- Task Description: see close_name_gaps.md
'''

def close_gaps(folder, prefix, file_ext, places):
    '''
    Args:
    - folder(str.): the path of the folder containing the files to process
    - prefix(str.): the name of the files (excluding numbering) to process
    - file_ext(str.): the extension of the files to process (e.g. '.pdf', '.txt', '.csv', etc.)
    - places(int.): the number of places in the files' numbering (e.g. 1 if 0-9, 2 if 00-99, 3 if 000-999, etc.)

    Output:
    - searches the specified folder for the files with the specified prefix and file extension and
      locates any gaps in their numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt); 
      renames the files as necessary in order to close said gaps
    '''

    import os, shutil
    
    # Gets the absolute path of the specified folder
    folder = os.path.abspath(folder)

    # Creates a new folder within 'Documents' in which to move the processed files
    new_folder_name = os.path.basename(folder + ' (gaps closed)')
    home_dir = os.path.expanduser('~')
    new_dir = os.path.join(home_dir, 'Documents', new_folder_name)
    os.mkdir(new_dir)

    # Lists the file contents of the specified folder
    fol_contents = os.listdir(folder)

    # Ignores filenames not of the specified prefix and extension 
    for filename in fol_contents:
        if not filename.startswith(prefix):
            fol_contents.remove(filename)
        if not filename.endswith(file_ext.lower()):
            fol_contents.remove(filename)            

    # Tracks the file numbering within the next for-loop
    count = 1

    # Loops over each of the specified files within the specified folder
    for filename in fol_contents:
        
        # Gets the absolute path of the current file
        abs_file_path = os.path.join(folder, filename)
        
        # Gets the correct filename of the current file
        count_form = str(count).rjust(places, '0')  # Uses the same number of places as the files' original numbering
        base_start = prefix + count_form
        
        # Moves files with the correct numbering to the new folder
        if filename.startswith(base_start):
            new_abs_file_path = os.path.join(new_dir, filename)
            shutil.move(abs_file_path, new_abs_file_path)
            count += 1
            
        # Renames files with the correct numbering, then moves them to the new folder
        elif not filename.startswith(base_start):
            new_file_name = base_start + file_ext.lower()
            new_abs_file_path = os.path.join(new_dir, new_file_name)
            shutil.move(abs_file_path, new_abs_file_path)
            count += 1

    # Directs the user to the folder of the function's output
    print('Done. Find your processed files in:\n%s'
          %(new_dir))