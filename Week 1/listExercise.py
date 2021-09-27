from collections import Counter

# Initial inventory 
inventory = {
    'sword': 2,
    'axe': 1,
    'cold milk': 10,
    'stormwind pie': 2,
    'bow': 1,
    'helmet': 4,
    'bags': 6,
    'shirt': 2
}

# Items we want to add to the initial inventory
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'dagger', 'gold coin', 'ruby']

# Function that displays the content of the inventory
# and counts the total amount of items inside it
def displayInventory(inventory):
    print('Inventory:')
    amountOfItems = 0
    for key, value in inventory.items():
        print(key, value)
        amountOfItems += value
    
    print('Total amount of items: ' + str(amountOfItems))


# Function that adds items to a dictionary based on the contents of a list
def addToInventory(updatedInventory, addedItems):
    items = Counter(addedItems)
    for key, value in items.items():
        updatedInventory.setdefault(key, value)

    displayInventory(updatedInventory)

    return updatedInventory
        
        
addToInventory(inventory, dragonLoot)

# Output:
    # Inventory:
    # sword 2
    # axe 1
    # cold milk 10
    # stormwind pie 2
    # bow 1
    # helmet 4
    # bags 6
    # shirt 2
    # gold coin 3
    # dagger 2
    # ruby 1
    # Total amount of items: 34