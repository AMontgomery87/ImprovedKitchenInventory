from collections import Counter
from Recipes import*


inventory_file = open("Inventory", "a")

def whatcooking():
    cookingwhat=input("What are we cooking? ")
    if "ribeye" in cookingwhat:
        contents = "\n".join(ribeye)
        inventory_file.writelines(contents)



whatcooking()



inventory_fileR = open("Inventory", "r")

with open("Inventory") as f:
    inventoryList = f.read().splitlines()
    inventory_counter = Counter(inventoryList)

print(inventoryList)
print(inventory_counter)

inventory_file.close()