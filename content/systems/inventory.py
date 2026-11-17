
# Inventory system for The Museum of Things That Never Happened


# List of items the player has collected
inventory = []


# Descriptions of the inventory items
item_descriptions = {
    "Sealed Letter": "A mysterious letter containing a secret about the Curator.",
    "Silver Key": "A small silver key that may unlock a hidden door.",
    "Missing City Map": "A map showing the location of a forgotten city.",
    "Broken Clock Hand": "A clock hand that may help solve the broken clock puzzle.",
    "Memory Photograph": "A photograph showing a memory connected to the museum."
}


# Add an item to the inventory
def add_item(item):

    if item in item_descriptions:
        if item not in inventory:
            inventory.append(item)
            print(item + " was added to your inventory.")
        else:
            print("You already have this item.")
    else:
        print("This item does not exist.")


# Remove an item from the inventory
def remove_item(item):

    if item in inventory:
        inventory.remove(item)
        print(item + " was removed from your inventory.")
    else:
        print("You do not have this item.")


# Display the player's inventory
def show_inventory():

    print("\n" + "=" * 30)
    print("YOUR INVENTORY")
    print("=" * 30)

    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for index, item in enumerate(inventory):
            print(str(index + 1) + ". " + item)

    print("=" * 30)


# Use an item from the inventory
def use_item(item):

    if item in inventory:
        print("\nYou use the " + item + ".")
        print(item_descriptions[item])
        return True
    else:
        print("You do not have this item.")
        return False

