'''
coin_flip_streaks.py: calculates the probability of 100 coin tosses producing at least one streak of 6 heads or tails

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 4. Practice Project - Coin Flip Streaks
- Task Description: see README.md
'''

import random

# Stores the number of experiments that result in at least one streak
streak_tally = 0

# Repeats the experiment 10,000 times
for experiment_number in range(10000):

    # Writes a random list of 100 'heads' or 'tails' values
    flip_outcomes = []
    for flip in range(100):
        flip_outcome = random.randint(0, 1) # Heads and tails represented by 1s and 0s
        flip_outcomes.append(flip_outcome)
        
    # Checks for the presence of at least one uninterrupted streak of 6 'heads' or 'tails'
    for i in range(len(flip_outcomes)-6):
        if flip_outcomes[i:i+6] == [0,0,0,0,0,0]:
            streak_tally += 1
            break
        elif flip_outcomes[i:i+6] == [1,1,1,1,1,1]:
            streak_tally += 1
            break

# Calculates the probability of a streak as a percentage (experimental size = 10,0000 iterations)
experiment_outcome = (streak_tally/10000.0)*100

print('\nProbability of 100 coin tosses producing a streak of 6 heads or tails:\n' + str(experiment_outcome) + '%')