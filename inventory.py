# Krzysztof Dzioba

import csv
import os

inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}


def import_inventory(inventory, filename="import_inventory.csv"):
    """Importing inventory from file. Notice this function is vulnerable whether\
 file import_inventory.csv exists."""

    if filename:
        try:
            with open(filename, 'r') as inv_file:
                for l in inv_file:  # l - line of file
                    l = l.split(",")  # putting line from csv file to list
                    item = l[0]  # each item is now a different variable
                    value = l[1]  # it's str
                    if value == "count":
                        continue
                    if item == "item_name":
                        continue
                    value_length = len(value) - 1
                    value = value[0:value_length]  # no \n in str "count"
                    dictionary = {}
                    value = int(value)
                    dictionary[item] = value  # Temporary dictionary
                    for item in dictionary:  # Adding to main inventory
                        if item not in inventory:
                            inventory[item] = value
                        else:
                            inventory[item] += value
        except:
            print(
                "\nNo such file. If \"import_inventory.csv\" file exist, \
inventory has been imported from it. \n")
            file_exist = os.path.isfile("import_inventory.csv")
            if file_exist:
                with open("import_inventory.csv", 'r') as inv_file:
                    for l in inv_file:  # l - line of file
                        l = l.split(",")  # putting line from csv file to list
                        item = l[0]  # each item is now a different variable
                        value = l[1]  # it's str
                        if value == "count":
                            continue
                        if item == "item_name":
                            continue
                        value_length = len(value) - 1
                        value = value[0:value_length]  # no \n in str "count"
                        dictionary = {}
                        value = int(value)
                        dictionary[item] = value  # Temporary dictionary
                        for item in dictionary:  # Adding to main inventory
                            if item not in inventory:
                                inventory[item] = value
                            else:
                                inventory[item] += value
            else:
                print("File import_inventory.csv doesn't exist. Inventory has\
 not been imported. \n ")


def export_inventory(inventory, filename=None):
    """Exporting inventory to a file"""
    if filename == "":
        with open('export_inventory.csv', 'w') as z:
            writer = csv.writer(z)
            for row in inventory.items():
                writer.writerow(row)

    else:
        if ".csv" in filename:
            with open(filename, 'w') as z:
                writer = csv.writer(z)
                for row in inventory.items():
                    writer.writerow(row)
        else:
            filename = filename + ".csv"
            with open(filename, 'w') as z:
                writer = csv.writer(z)
                for row in inventory.items():
                    writer.writerow(row)


def display_inventory(inventory):
"""Display inventory, no order"""
    print("Inventory:")
    for i in inventory:
        print(inventory[i], i)
    z = 0
    for k in inventory:
        z = z + inventory[k]
    print("Total number of items: ", z, "\n")


def add_to_inventory(inventory, items):
    """Adding loot to the inventory"""
    for i in loot:
        if i not in inventory:
            inventory[i] = 0
        if i in inventory:
            inventory[i] += 1
    return inventory


def print_table(inventory, order=None):
    """Printing inventory in a table with specific order."""
    list_of_items = []  # list of number of items held
    for l in inventory:
        z = inventory[l]
        list_of_items.append(z)
        # print(list_of_items)
    m = max(list_of_items)
    o = str(m)
    t = list(o)
    r = len(t)  # last 4 lines checks how many digits are in number of items
    #  with biggest value. It's just in case the amount of loot
    #  of the same type is very, very big.
    list_of_items = []
    for key in inventory:
        list_of_items.append(key)

    q = 0  # q is max lenght of name of item
    for l in (list_of_items):
        k = len(l)
        if k > q:
            q = k

    e = list_of_items

    n = len("count")
    # g - variable which defines how strong it will justify to the right in
    # table.
    if r > n:  # checks how justifying should works.
        g = r  # number of digits are bigger
    else:
        g = n  # "count is bigger"

    e = g + len("item name:")  # "e" used in printing below
    w = e + len("Item_name")  # "w" used in printing dash_list below

    x = sum(inventory.values())

    if order == "count,desc":

        print(("count").rjust(g + 3), "Item name:".rjust(g + q))
        dash_list = ["-"] * (g + q + g + 4)
        print (''.join(dash_list).rjust(g + 3 + q))

        for key, value in sorted(
                inventory.items(), key=lambda x: x[1], reverse=True):
            print(str(value).rjust(g + 3), str(key).rjust(g + q))
        print (''.join(dash_list))

        print("Total numbers of items: ", x)

    elif order == "count,asc":
        print(("count").rjust(g + 3), "Item name:".rjust(g + q))
        dash_list = ["-"] * (g + q + g + 4)
        print (''.join(dash_list).rjust(g + 3 + q))

        for key, value in sorted(
                inventory.items(), key=lambda x: x[1], reverse=False):
            print(str(value).rjust(g + 3), str(key).rjust(g + q))
        print (''.join(dash_list))

        print("Total numbers of items: ", x)

    else:
        print(("count").rjust(g + 3), "Item name:".rjust(g + q))
        dash_list = ["-"] * (g + q + g + 4)
        print (''.join(dash_list).rjust(g + 3 + q))
        # print(dash_list, end=" ")
        for key in inventory:
            print(str(inventory[key]).rjust(g + 3), str(key).rjust(g + q))
        print (''.join(dash_list))

        print("Total number of items: ", x, "\n")

loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

display_inventory(inventory)

filename = input("Write a file name to import inventory or leave empty if file \
doesn't exist.\n")

import_inventory(inventory, filename)

display_inventory(inventory)

add_to_inventory(inventory, loot)

print("Adding loot. \n")

order = input(
    "Showing inventory. Select order: count,desc count,asc or leave empty\n")

print_table(inventory, order)

filename = input(
    "Type a filename to export your inventory. You can just press enter. \n")

export_inventory(inventory, filename)

print_table(inventory)
