# ------ Project Requirement 1 ------
# Create a new empty list named shopping_list.
shopping_list = []


# Create a function named add_to_list that declares a parameter named item
# Add the item to the list
def add_to_list(item):
    shopping_list.append(item)
    print("Added! List has {} items.".format(len(shopping_list)))


# ------ Project Requirement 1 ------
# Define a function named show_list that prints all the items in the list
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    ENTER 'SHOW' to see your current list.
    """)


show_help()
while True:
    new_item = input("> ")

    if new_item == "DONE":
        break

    elif new_item == "HELP":
        show_help()
        continue

    elif new_item == "SHOW":
        show_list()
        continue

    # Call add_to_list with new_item as an argument
    add_to_list(new_item)
