'''
user_login.py: simulates a simple login screen

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 2 - Flow Control

Objective: Practice implementing flow control statements
'''

# Greets the user
print('Hello!')

# Asks the user to enter their first or full name
while True:
    print('What is your name?')
    username = str.lower(input()) # makes input validation case-insensitive
    if (username == 'yesahel') or (username == 'yesahel scicluna'): # Accepts the user's first name or full name
        break
    else:
        print('User not recognised.')    

# Gives the user 3 chances to input the correct password before granting or denying them access
print('Please enter your password.')
for i in range(3):
    password = input() # input validation is kept case-sensitive
    if password == 'marbledspinefoot': 
        break
    else:
        print('Incorrect. Guesses remaining: ' + str(2-i))
        i = i + 1
if i == 3:
    print('Access denied.')
elif i < 3:
    print('Access granted. Welcome, Yesahel.')
