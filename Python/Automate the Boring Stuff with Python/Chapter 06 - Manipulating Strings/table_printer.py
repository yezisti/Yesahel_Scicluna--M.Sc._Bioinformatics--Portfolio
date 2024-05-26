'''
table_printer.py: tabulates the contents of a list obj. and adds padding to the columns

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 6. Practice Project - Table Printer
- Task Description: see table_printer.md
'''

def print_table(table_data):
    '''
    Args:
    - table_data(list of lists of str.): the data to tabulate
        - Note: 
            - inner lists represent individual columns
            - nth members of each inner list will share the same row
            - inner lists must be of equal length
    Prints:
    - the data in tabular format, with each column right-justified
    '''

    import copy

    # Creates a separate copy of the list arg.
    table_copy = copy.deepcopy(table_data)

    # Creates a list that is as long as there are inner lists in the list arg.
    col_widths = [0] * len(table_data)


    for x in range(len(table_data)):                    # Iterates over the length of the list arg.
        for y in range(len(table_data[0])):             # Iterates over the length of each inner list in the list arg. 
            table_copy[x][y] = len(table_data[x][y])    # Stores the length of each string

        # Finds and stores the length of the longest string in each inner list
        table_copy[x].sort()                            
        col_widths[x] = table_copy[x][-1]

    # Prints the list arg. in tabular format
    for y in range(len(table_data[0])):  
        for x in range(len(table_data)):
            print(table_data[x][y].rjust(col_widths[x]), end = ' ')     # rjust() uses the stored data in order to add appropriate padding to each column
        print()     # Starts a fresh line for each row of the table

        
# Function test:

table = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]

print_table(table)                               
    
