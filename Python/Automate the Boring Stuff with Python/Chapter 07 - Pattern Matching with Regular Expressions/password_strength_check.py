'''
password_strength_check.py: uses a set of regular expressions in order to test the strength of a password

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 7. Practice Project - Strong Password Detection
- Task Description: see password_strength_check.md
'''

def check_strength(password):

    import re
                                                                                    # Checks that the password contains at least:
    eight_characters = re.compile(r'.{8,}')                                             # 8 characters
    contains_uppercase = re.compile(r'.*[A-Z].*')                                       # 1 uppercase letter              
    contains_lowercase = re.compile(r'.*[a-z].*')                                       # 1 lowercase letter
    contains_digit = re.compile(r'.*\d.*')                                              # 1 digit
    contains_special = re.compile(r'''.*[.\-_,:;/\?!@#$%^&*()+=|'"{}\[\]].*''')          # 1 special character
    
    # Lists the RegEx obj. created
    checks = [eight_characters, contains_uppercase, contains_lowercase,
              contains_digit, contains_special]
    
    # Stores 'PASS'/'FAIL' values for each strength check 
    check_results = {eight_characters:'FAIL', contains_uppercase:'FAIL',
                     contains_lowercase:'FAIL', contains_digit:'FAIL',
                     contains_special: 'FAIL'}
    
    # Stores the number of strength checks passed
    tally = 0

    # Loops over each of the 5 strength checks created
    for check in checks:

        if check.search(password) != None:      # Evaluates to True if the password matches the given strength check's RegEx obj.     
            check_results[check] = 'PASS'           # Assigns 'PASS' to the check_results dict.
            tally += 1                              # Increments the tally by 1

    if 'FAIL' not in check_results.values():
        print('\nYour password is strong. It passes all checks.\n')   # Prints if all strength checks are assigned 'PASS'

    else:
        print()
        if tally < 2:
            print('Your password is very weak.', end = '')          # Prints if 0 or 1 strength checks are assigned 'PASS'
        if tally == 2:
            print('Your password is weak.', end = '')               # Prints if 2 strength checks are assigned 'PASS'
        if tally == 3:
            print('Your password is of moderate strength.', end = '')
        if tally == 4:
            print('Your password could be stronger.', end = '')     # Prints if 4 strength checks are assigned 'PASS'
        
        # Provides the user information on how to improve their password's strength
        print(' It should contain at least:')
        if 'FAIL' in check_results[eight_characters]:
            print(' - 8 characters')
        if 'FAIL' in check_results[contains_uppercase]:
            print(' - 1 uppercase letter')
        if 'FAIL' in check_results[contains_lowercase]:
            print(' - 1 lowercase letter')
        if 'FAIL' in check_results[contains_digit]:
            print(' - 1 digit')
        if 'FAIL' in check_results[contains_special]:
            print(' - 1 special character')

# Function tests:
check_strength('marbled')
check_strength('marbledspinefoot')
check_strength('marbledSpinefoot')
check_strength('marbledSpinef00t')
check_strength('marb1edSpinef00+')

