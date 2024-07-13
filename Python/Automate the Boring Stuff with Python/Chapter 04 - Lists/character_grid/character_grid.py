'''
character_grid.py: prints a grid denoted by a list of lists of string characters

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 4. Practice Project - Character Picture Grid
- Task Description: see README.md
'''

def print_grid(grid_list):
    '''
    Args:
    - grid_list(list of lists of str.): the 'grid' of characters to print
        Note:
        - inner lists denote individual columns
        - nth members of each inner list share the same row

    Prints:
    - the character grid denoted by the grid_list arg.
    '''
    for y in range(len(grid_list[0])):         # Iterates over the height of the grid
        for x in range(len(grid_list)):        # Iterates over the width of the grid
            print(grid_list[x][y], end = '')   # Prints the character at each 'coordinate'
        print()                                # Starts a fresh line once a row is printed in full


# Function test:

heart = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']]

print_grid(heart)
