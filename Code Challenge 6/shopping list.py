# Written by piyush kumar
# Shopping list app

# To import color
import colorama
# List to hold items
item_list = []

# Instructions for how to use app
print("---------------Welcome to Shopping list App----------------".center(20))
print(colorama.Fore.RED+("Enter HELP to know about various commands"))
print(colorama.Fore.BLACK+"Enter items you want to add to the list")


# To add item at specific index
def add_at():
    index_1 = int(input("Enter the index at which you want to add the item:"))
    item = input("Enter the item you want to add at the specified index:")
    item_list.insert((index_1-1), item)


# To remove items
def remove_items():
    items_remove = input("Enter item name to be removed:")
    item_list.remove(items_remove)


# Function to show items associated with SHOW commands
def show():
    print("------------------------------------------------------------------")
    for i in item_list:
        print(i)


# To show about special commands
def helps():
    print(f'{1}.SHOW-to show shopping list items')
    print(f'{2}.ADD-to add items at a specific Index in the shopping list')
    print(f'{3}.REMOVE-to remove items from the shopping list')
    print(f'{4}.DONE-to stop adding items and to quit from the app')


# To accept item
def add_item():
    while True:
        item_accept = input(">")
        if item_accept == "DONE":
            break
        elif item_accept == "SHOW":
            show()
        elif item_accept == "HELP":
            helps()
        elif item_accept == "ADD":
            add_at()
        elif item_accept == "REMOVE":
            remove_items()
        else:
            item_list2 = item_accept.split(",")
            item_list.extend(item_list2)


# To call the function for adding items in the shopping list
add_item()
