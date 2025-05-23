# Assignment 1: Create an inventory management - Use loops to display or update list of stock items

# This program allows the user to manage an inventory list.
# The user can view the current inventory, add new items, or remove existing items.
# The program uses a loop to repeatedly display options until the user chooses to exit.
# It demonstrates the use of lists, loops, and conditional statements in Python.

inventory = ["Apples", "Bananas", "Oranges"]

while True:
    print("\nCurrent Inventory:")
    for idx, item in enumerate(inventory, 1):
        print(f"{idx}. {item}")
    print("\nOptions:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        new_item = input("Enter item to add: ")
        inventory.append(new_item)
        print(f"{new_item} added to inventory.")
    elif choice == "2":
        remove_item = input("Enter item to remove: ")
        if remove_item in inventory:
            inventory.remove(remove_item)
            print(f"{remove_item} removed from inventory.")
        else:
            print("Item not found in inventory.")
    elif choice == "3":
        print("Exiting inventory management.")
        break
    else:
        print("Invalid choice. Please try again.")