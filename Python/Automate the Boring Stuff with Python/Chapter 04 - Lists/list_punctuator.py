'''
list_punctuator.py: Punctuates a list of inputted items with commas, conjuctions, and full stops. 

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 4. Practice Project - Comma Code
- Task Description: see list_punctuator.md
'''

def punctuate(anylist):
   if len(anylist) > 1:
      print(anylist[0].capitalize(), end = ', ')     # Capitalises the first obj. and inserts a comma after it
      
      if len(anylist) > 2:                         
         for i in range(1, len(anylist)-2):
             print(anylist[i].lower(), end = ', ')   # Inserts commas after obj. in the middle of the list

         print(anylist[-2].lower(), end = ', and ')  # Inserts a comma and an 'and' after the penultimate obj.
         print(anylist[-1].lower(), end = '.')       # Inserts a full stop after the final list obj. 

      else:
         print('and ' + anylist[1].lower() + '.', end = '')    # Handles lists containing 2 obj.
         
   else:
      print('You must have more than one item in your list.')  # Rejects lists containing only 1 obj.
   
while True:
    print('\nEnter a list of items you wish this program to punctuate for you.', 
          '\nEnter a blank when your list is done.\n')

    itemlist = []

   # Stores the user-inputted strings in the itemlist list obj.
   # Stops appending strings when the user presses enter on a blank input
    while True:
        items = input()
        if items == '':
            break                 
        itemlist.append(items)     

    # Calls the defined function and passes it itemlist as arg.
    punctuate(itemlist)

    # Allows the user to either continue with a new list or quit the program
    print("\n\nContinue with a new list? Enter 'yes' or 'no'.")
    while True:
        userselection = input().lower()
        if userselection == 'yes':
            break
        elif userselection == 'no':
            break
        else:
            print("\nInput unrecognised. Type 'yes' or 'no'.")
            continue
    if userselection == 'yes':
        continue
    elif userselection == 'no':
        break

