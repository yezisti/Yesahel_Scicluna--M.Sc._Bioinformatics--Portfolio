'''
game_inventory.py: displays the contents of dict. and list objects; updates dict. obj. with list obj.

Author: Yesahel Scicluna

Source: Al Sweigart, Automate the Boring Stuff with Python. Chapter 5. Practice Projects - Fantasy Game Inventory,
                                                                                           List to Dictionary Function for Fantasy Game Inventory
- Task Description: see game_inventory.md
'''

# Displays inventory contents
def display_inventory(inventory):
    '''
    Args:
    - inventory(dict.): key(str.): inventory item name; value(int.): inventory item quantity
    '''
    item_total = 0
    for k, v in inventory.items():

        # Stylises the output
        qt = '*' + str(v) 
        print(qt.rjust(4) + ' ' + k)
        
        item_total += v
    print('Total number of items: ' + str(item_total) + '\n')

# Displays loot contents
def display_loot(loot):
    '''
    Args:
    - loot(list of str.): names of each single item in loot
    '''
    # Creates a dict. obj. from the list arg. 
    loot_dict = {}
    item_total = 0
    for item in loot:
        loot_dict.setdefault(item, 0)
        loot_dict[item] += 1
    
    # Prints the loot contents by accessing the dict. items
    for k, v in loot_dict.items():

        # Stylises the output
        qt = '*' + str(v)
        print(qt.rjust(4) + ' ' + k)
        
        item_total += v
    print('Total number of items: ' + str(item_total) + '\n')

# Adds loot contents to inventory
def add_to_inventory(inventory, loot):
    '''
    Args:
    - inventory(dict.): key(str.): inventory item name; value(int.): inventory item quantity
    - loot(list of str.): names of each single item in loot
    '''
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory
    

# Function tests:

player1_inventory  = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'gold coin']

print('\nThis is your inventory at the start of the game:')
display_inventory(player1_inventory)

print('You slayed a dragon and obtained its loot:')
display_loot(dragon_loot)

player1_inventory = add_to_inventory(player1_inventory, dragon_loot)
print('This is what your inventory looks like now:')
display_inventory(player1_inventory)
