'''
coin_toss_debug.py: presents a debugged version of a simple guessing game program

Authors: Yesahel Scicluna, Al Sweigart

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 10. Practice Project - Debugging Coin Toss

Task Description: see coin_toss_debug.md
'''

# Original code:

'''
(1) import random
(2) guess = ''
(3) while guess not in ('heads', 'tails'):
(4)     print('Guess the coin toss! Enter heads or tails:')
(5)     guess = input()
(6) toss = random.randint(0, 1) # 0 is tails, 1 is heads
(7) if toss == guess:
(8)     print('You got it!')
(9) else:
(10)    print('Nope! Guess again!')
(11)    guesss = input()
(12)    if toss == guess:
(13)        print('You got it!')
(14)    else:
(15)        print('Nope. You are really bad at this game.')
'''

# Debugged code:

import random

print('\nGuess the coin toss!')
guess = ''                                             

while (guess != 'heads') and (guess != 'tails'): # Amendment to original line (3) 
    print('\nEnter heads or tails:')
    guess = input()
    
toss = random.randint(0, 1) # 0 is tails, 1 is heads

# Insertion between original lines (6) and (7):
if toss == 0:
    toss = 'tails' # Assigns 'tails' to toss if toss == 0
if toss == 1:
    toss = 'heads' # Assigns 'heads' to toss if toss == 1
    
if toss == guess:
    print('\nYou got it!')

else:
    print('\nNope! Guess again!')
 
    # Insertion between original lines (10) and (11):
    # Reinstates the input validation used by the first while loop
    guess = ''
    while (guess != 'heads') and (guess != 'tails'):
        print('\nEnter heads or tails:')        

        guess = input() # Amendment to original line (11)
        
    if toss == guess:
        print('\nYou got it!')
    else:
        print('\nNope. You are really bad at this game.')
