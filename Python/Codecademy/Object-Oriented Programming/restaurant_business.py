'''
restaurant_business.py: defines a number of related classes, assigns them a number of attributes and methods,
and creates a number of instances of them.

Author: Yesahel Scicluna 

Source: Codecademy. Python 3. Practice Project - Basta Fazoolin'

Task Description: see restaurant_business.md
'''

import datetime as dt


# DEFINING CLASSES:

class Menu:

  def __init__(self, name, items, start_time, end_time):
    '''
    Args:
    - name(str.):  name of the menu
    - items(dict.):  keys(str.): food/drink items on the menu; values(floats): their prices
    - start_time(datetime): time when the menu is first served
    - end_time(datetime): time when the menu is last served
    '''
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return '{} | Served {} to {}'.format(self.name, self.start_time, self.end_time)

  def calculate_bill(self, purchased_items):
    '''
    Args:
    - purchased_items(list of str.): names of any items in the menu to calculate the sum price of
    '''
    bill = 0
    for purchased_item in purchased_items:
      bill += self.items[purchased_item.lower()]
    return bill

class Franchise:

  def __init__(self, address, menus):
    '''
    Args:
    - address(str.): address of the franchise
    - menus(list of Menu obj.): menus served by the franchise
    '''
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address

  def available_menus(self, time):
    '''
    Args:
    - time(datetime): time of the day to check for the franchise's available menus 
    '''
    available_menus = []
    for menu in self.menus:
      if (time >= menu.start_time) and (time <= menu.end_time):
        available_menus.append(menu)
    return available_menus

class Business:

  def __init__(self, name, franchises):
    '''
    Args:
    - name(str.): name of the business
    - franchises(list of Franchise obj.): franchises opened by the business
    '''
    self.name = name
    self.franchises = franchises


# INSTANTIATING CLASSES:

## Creating Menu objects:

brunch_items = {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50}
brunch = Menu('Brunch Menu', brunch_items, dt.time(11), dt.time(16))

early_bird_items = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00}
early_bird = Menu('Early Bird Menu', early_bird_items, dt.time(15), dt.time(18))

dinner_items = {
  'crostini with eggplant caponata': 13.00, 
  'caesar salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00}
dinner = Menu('Dinner Menu', dinner_items, dt.time(17), dt.time(23))

kids_items = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00}
kids = Menu('Kids Menu', kids_items, dt.time(11), dt.time(21))

arepas_items = {
  'arepa pabellon': 7.00,
  'pernil arepa': 8.50, 
  'guayanes arepa': 8.00, 
  'jamon arepa': 7.50}
arepas = Menu('Arepas Menu', arepas_items, dt.time(10), dt.time(20))

## Creating Franchise objects:

menu_list = [brunch, early_bird, dinner, kids]
flagship_store  = Franchise('1232 West End Road', menu_list)
new_installment = Franchise('12 East Mulberry Street', menu_list)
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas])

## Creating Business objects:

franchise_list = [flagship_store, new_installment]
first_business = Business('Basta Fazoolin\' with my Heart', franchise_list)
second_business = Business('Take a\' Arepa', [arepas_place])


# TESTING METHODS:

## Class Menu string representation tests:

print(brunch, early_bird, dinner, kids, arepas, sep = '\n', end = '\n\n')

## Class Franchise string representation tests:

print(flagship_store, new_installment, arepas_place, sep = '\n', end = '\n\n')

## Menu.calculate_bill tests:

brunch_order_1 = ['pancakes', 'home fries', 'coffee']
early_bird_order_1 = ['salumeria plate', 'mushroom ravioli (vegan)']

brunch_order_1_bill = brunch.calculate_bill(brunch_order_1)
early_bird_order_1_bill = early_bird.calculate_bill(early_bird_order_1)

print(brunch_order_1_bill, early_bird_order_1_bill, sep = '\n', end = '\n\n')

## Franchise.available_menus tests:

print(flagship_store.available_menus(dt.time(12)))
print(flagship_store.available_menus(dt.time(17,59)))