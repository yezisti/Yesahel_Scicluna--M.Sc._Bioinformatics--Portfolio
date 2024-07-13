'''
collatz.py: performs the Collatz sequence of operations on a number input

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 3. Practice Projects - The Collatz Sequence, Input Validation
- Task Description: see README.md
'''

def collatz(number):
    if number % 2 == 0: # Evaluates to True if arg. is even
        print(number // 2) # Displays half the number
        return(number // 2) # Returns half the number
    elif number % 2 == 1: # Evaluates to True if arg. is odd
        print(3 * number + 1) # Displays triple the number plus one
        return(3 * number + 1) # Returns triple the number plus one

# Provides context to the user.
print(
    '\nThe Collatz conjecture is one of the most famous unsolved problems in mathematics.', \
    'It asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.', \
    'It concerns sequences of integers in which each term is obtained from the previous term as follows:', \
    ' - If the previous term is even, the next term is one half of the previous term.', \
    ' - If the previous term is odd, the next term is 3 times the previous term plus 1.', \
    'The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence.', \
    'The conjecture has been shown to hold for all positive integers up to 2.95 x 10^20, but no general proof has been found.', \
    '\nInput a positive integer to learn about its Collatz sequence.\n', \
    sep = '\n')

while True:
    print('Input your number here:')
    try:
        number_input = int(input())
        print()
        if number_input > 0:
            print('The collatz sequence for ' + str(number_input) + ' is:')
            print(number_input)
            count = 0

            # Loop applies the collatz() function to the inputted number until it is reduced to 1
            while number_input != 1:
                    number_input = collatz(number_input)
                    count = count + 1
            else:
                print('\nNumber of operations to 1:\n' + str(count)) # Displays the size of the inputted number's Collatz sequence

        elif number_input == 0:
            print('0 can never be transformed into 1 when operated on in this manner.')  # Prevents user from entering 0
        elif number_input < 0:
            print('Negative integers can never be transformed into 1 when operated on in this manner.') # Prevents user from entering a negative integer
        print()

    except ValueError:
        print('\nInput must be an integer.\n') # Prevents user from entering anything other than an integer
