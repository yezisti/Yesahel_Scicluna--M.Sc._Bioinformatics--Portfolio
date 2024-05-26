# inventory.py - Task Description

### _From Automate the Boring Stuff with Python. Chapter 5. Practice Project - Fantasy Game Inventory:_

You are creating a fantasy video game. The data structure to model the player's inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, this dictionary value means the player has 1 rope, 6 torches, 42 gold coins, and so on:

`{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}`

Write a function named `displayInventory()` that would take any possible "inventory" and display it like the following:

`Inventory:`<br>
`12 arrow`<br>
`42 gold coin`<br>
`1 rope`<br>
`6 torch`<br>
`1 dagger`<br>
`Total number of items: 62`

### _From Automate the Boring Stuff with Python. Chapter 5. Practice Project - List to Dictionary Function for Fantasy Game Inventory:_

Imagine that a vanquished dragon's loot is represented as a list of strings like this:

`dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']`

Write a function named `addToInventory(inventory, addedItems)`, where the `inventory` parameter is a dictionary representing the player's inventory (like in the previous project) and the `addedItems` parameter is a list like `dragonLoot`. The `addToInventory()` function should return a dictionary that represents the updated inventory. Note that the `addedItems` list can contain multiples of the same item.

The previous program (with your `displayInventory()` function from the previous project) would output the following:

`Inventory:`<br>
`45 gold coin`<br>
`1 rope`<br>
`1 ruby`<br>
`1 dagger`<br>
`Total number of items: 48`