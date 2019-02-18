import os

# ------ Project Requirement 1 ------
# Create a new empty list named shopping_list.
shopping_list = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Create a function named add_to_list that declares a parameter named item
# Add the item to the list
def add_to_list(item):
    shopping_list.append(item)
    print("Added! List has {} items.".format(len(shopping_list)))
    show_list()


# ------ Project Requirement 1 ------
# Define a function named show_list that prints all the items in the list
def show_list():
    clear_screen()
    print("Here's your list:")
    for item in shopping_list:
        print(item)


def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    ENTER 'SHOW' to see your current list.
    """)


show_help()
while True:
    new_item = input("> ")

    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        break

    elif new_item.upper() == "HELP":
        show_help()
        continue

    elif new_item.upper() == "SHOW":
        show_list()
        continue
    else:
        add_to_list(new_item)
