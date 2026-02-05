"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = dict([])

    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory
print("Q1:")
print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))



def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory
print("Q2:")
print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))



def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
        else:
            inventory.setdefault(item, 0)
    return inventory
print("Q3:")
print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))
print(decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))



def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory and inventory[item] > 0:
        inventory.pop(item)
    return inventory

print("Q4:")
print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))
print(remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))



def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inventory_list = []

    for item in inventory:
        if inventory[item] > 0:
            inventory_list.append((item, inventory[item]))
    return inventory_list

print("Q5:")
print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))