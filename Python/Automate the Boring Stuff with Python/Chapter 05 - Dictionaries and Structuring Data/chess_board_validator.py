'''
chess_board_validator.py: defines two functions that look into the validity of dictionary objects intended to represent chess boards

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 5. Practice Project - Chess Dictionary Validator
- Task Description: see chess_board_validator.md
'''

def check_board(chess_board_dict):
    '''
    Usage:
    - Checks the validity of a dictionary object in representing a chess board of example notation:
      {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
    
    Args:
    - chess_board_dict (dict.) : chess board object to validate
    
    Returns:
    - True if dictionary object represents a valid chess board
    - False if dictionary object represents an invalid chess board

    Prints:
    - None
    '''

    import re

    # Creates lists to house each player's pieces
    w_piece_list = []
    b_piece_list = []

    # Returns False if dict. values do not start with 'w' or 'b'
    # Otherwise stores values in the appropriate list
    for value in chess_board_dict.values():
        if value[0] == 'w':
            w_piece_list.append(value)
        elif value[0] == 'b':
            b_piece_list.append(value)
        else:
            return False

    # Returns False if any player has more than 16 pieces
    if len(w_piece_list) > 16 or len(b_piece_list) > 16:
        return False

    # Returns False if either king not in dict. 
    if 'wking' not in w_piece_list or 'bking' not in b_piece_list:
        return False

    # Returns False if either player has more than 8 pawns
    if w_piece_list.count('wpawn') > 8 or b_piece_list.count('bpawn') > 8:
        return False

    # Creates RegEx objects to check notation against
    white_re = re.compile('^w(pawn|knight|bishop|rook|queen|king)$')        
    black_re = re.compile('^b(pawn|knight|bishop|rook|queen|king)$')
    space_re = re.compile('^[12345678][abcdefgh]$')


    # Returns False if value notation does not match either RegEx object
    for piece in w_piece_list:
        if white_re.search(piece) == None:
            return False
    for piece in b_piece_list:
         if black_re.search(piece) == None:
            return False

    # Returns False if key notation does not match RegEx object
    for key in chess_board_dict.keys():
        if space_re.search(key) == None:
            return False
    
    # Returns True if all the above conditions are met
    return True


def check_board_help(chess_board_dict):
    '''
    Usage:
    - Explains the result obtained from check_board()
 
    Args:
    - chess_board_dict (dict.) : chess board object on which user requires information
    
    Returns:
    - None

    Prints:
    - Notes on valid notation
    - Indications towards source of dictionary invalidity
    '''

    import re
    
    # Creates lists to house each player's pieces
    w_piece_list = []
    b_piece_list = []

    # Prints info if dict. values do not start with 'w' or 'b'
    # Otherwise stores values in appropriate list
    for value in chess_board_dict.values():
        if value[0] == 'w':
            w_piece_list.append(value)
        elif value[0] == 'b':
            b_piece_list.append(value)
        else:
            print("Piece (dict. value) notation must be prefixed with 'w' for white or 'b' for black (case-sensitive).")
            return

    # Prints info if any player has more than 16 pieces
    if len(w_piece_list) > 16:
        print('White has more than 16 pieces on the board.')
        return
    if len(b_piece_list) > 16:
        print('Black has more than 16 pieces on the board.')
        return

    # Prints info if either king not in dict. 
    if 'wking' not in w_piece_list:
        print('White king not on board.')
        return
    if 'bking' not in b_piece_list:
        print('Black king not on board.')
        return

    # Prints info if either player has more than 8 pawns
    if w_piece_list.count('wpawn') > 8:
        print('White cannot have more than 8 pawns.')
        return
    if b_piece_list.count('bpawn') > 8:
        print('Black cannot have more than 8 pawns.')
        return

    # Creates RegEx objects to check notation against
    white_re = re.compile('^w(pawn|knight|bishop|rook|queen|king)$')        
    black_re = re.compile('^b(pawn|knight|bishop|rook|queen|king)$')
    space_re = re.compile('^[12345678][abcdefgh]$')


    # Prints info if value notation does not match either RegEx object
    for piece in w_piece_list:
        if white_re.search(piece) == None:
            print("White piece notation (case-sensitive): 'wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking'.")
            return
    for piece in b_piece_list:
         if black_re.search(piece) == None:
            print("Black piece notation (case-sensitive): 'bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking'.")
            return

    # Prints info if key notation does not match RegEx object
    for key in chess_board_dict.keys():
        if space_re.search(key) == None:
            print("Board space (dict. key) notation (case-sensitive): no. from 1 to 8, letter from a to h. Eg: '1a', '2a', '3b', '3c'.")
            return

    # Prints info if all the above conditions are met
    print('Board valid.\n', chess_board_dict)

'''
Deficiencies:
- Functions are unable to detect instances where the user assigns multiple pieces (values) to the same spaces (keys).
    - If all else valid, check_board() will return True.
    - Recommendation: print dictionary or use check_board_help() to check dictionary for missing pieces.
'''