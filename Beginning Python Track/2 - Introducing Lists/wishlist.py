books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]


def display_wishlist(title, lists):
    copied_list = lists.copy()
    print(title + ":")
    popped_value = copied_list.pop(0)
    print("Popped value = " + popped_value)
    for obj in copied_list:
        print("- " + obj)


display_wishlist("Books", books)
print()
display_wishlist("Video Games", video_games)

# IMPORTANT CONCEPT
# If you want to remove everything from a list, just saying:
# for item in inventory:
#     inventory.remove(item)
# will not work because the indices will be corrupted when manipulating the actual list.
# ----
# If doing:
# for item in inventory.copy()
#     inventory.remove(item)
# The list will become successfully empty because the indices are not corrupted while deletion occurs.
