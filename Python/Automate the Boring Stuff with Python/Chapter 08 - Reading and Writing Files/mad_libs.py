'''
mad_libs.py: reads text files, replacing a set of placeholder text with user-supplied text

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 8. Practice Project - Mad Libs
- Task Description: see mad_libs.md

Required Files: madlibs_1.txt, ..., madlibs_5.txt
'''

import os, random, re

# Stores the absolute path of the folder containing the required text files (see 'Required Files')
ml_folder = 'C:\\Users\\yesah\\Documents\\mad_libs' # Modify the path as necessary

# Changes the current working directory to the folder specified above
os.chdir(ml_folder)

# Reads any one of the text files within the specified folder
random_form = open('.\\madlibs_%s.txt' %(random.randint(1, 5)))
mad_libs = random_form.read()
random_form.close()

# Inpsects the randomly selected text in chunks
for i in range(len(mad_libs)):
    window = mad_libs[i:i+13]

    # Prompts the user to supply a string that can appropriately replace the placeholder text encountered
    # Replaces the placeholder text with the user-supplied text
    if '[adjective]' in window:
        print('\nEnter an adjective:')
        adjective = input()
        mad_libs = mad_libs.replace('[adjective]', adjective, 1)

    if '[sing. noun]' in window:
        print('\nEnter a singular noun:')
        noun = input()
        mad_libs = mad_libs.replace('[sing. noun]', noun, 1) 
    
    if '[plural noun]' in window:
        print('\nEnter a plural noun:')
        noun_pl = input()
        mad_libs = mad_libs.replace('[plural noun]', noun_pl, 1)

    if '[verb, inf]' in window:
        print('\nEnter an infinitive verb:')
        verb_inf = input()
        mad_libs = mad_libs.replace('[verb, inf]', verb_inf, 1)

    if '[verb, pt]' in window:
        print('\nEnter a verb in the past tense:')
        verb_pt = input()
        mad_libs = mad_libs.replace('[verb, pt]', verb_pt, 1)

    if '[verb, -ing]' in window:
        print('\nEnter a verb ending with -ing:')
        verb_ing = input()
        mad_libs = mad_libs.replace('[verb, -ing]', verb_ing, 1) 

    if '[person name]' in window:
        print('\nEnter the name of a person:')
        name = input()
        mad_libs = mad_libs.replace('[person name]', name, 1)

    if '[silly name]' in window:
        print('\nEnter a silly name:')
        silly_name = input()
        mad_libs = mad_libs.replace('[silly name]', silly_name, 1)

    if '[place name]' in window:
        print('\nEnter a place name:')
        place = input()
        mad_libs = mad_libs.replace('[place name]', place, 1)

    if '[job name]' in window:
        print('\nEnter a job name:')
        job = input()
        mad_libs = mad_libs.replace('[job name]', job, 1)  

    if '[food name]' in window:
        print('\nEnter a type of food:')
        food = input()
        mad_libs = mad_libs.replace('[food name]', food, 1) 

    if '[drink name]' in window:
        print('\nEnter a type of drink:')
        drink = input()
        mad_libs = mad_libs.replace('[drink name]', drink, 1)

    if '[animal name]' in window:
        print('\nEnter a type of animal:')
        animal = input()
        mad_libs = mad_libs.replace('[animal name]', animal, 1)  

# Writes the completed 'form' in a new text file
complete_form = open('.\\madlibs_complete.txt', 'w')
complete_form.write(mad_libs)
complete_form.close()

# Directs the user to the location of their completed 'form'
print('\nRead your Mad Libs here:')
print(os.path.join(ml_folder, 'madlibs_complete.txt'))
