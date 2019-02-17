import sys

# Global variables
TICKET_PRICE = 10
SERVICE_CHARGE = 2

# Class variables
tickets_remaining = 100
tickets_to_purchase = 0


def calculate_price(num_tickets):
    return (TICKET_PRICE * num_tickets) + SERVICE_CHARGE


while tickets_remaining != 0:
    # ----- Project Requirement: 1 -----
    # Output how many tickets are remaining using the tickets_remaining
    # variable

    # print("There are {} tickets remaining.".format(tickets_remaining))
    print("There are", tickets_remaining, "tickets available for purchase.")

    # ----- Project Requirement: 2 -----
    # Gather the user's name and assign it to a new variable
    name = input("Please enter your name: ")

    # ----- Project Requirement: 3 -----
    # Prompt the user by name and ask how many tickets they would like.
    # Calculate the price (number of tickets multiplied by the price) and
    # assign it to a variable.
    # Output the price to the screen.
    valid_purchase = False
    while not valid_purchase:
        try:
            tickets_to_purchase = int(input("How many tickets would you like, {}? ".format(name)))
            if tickets_remaining < tickets_to_purchase:
                raise ValueError("Insufficient tickets. There are {} tickets remaining.".format(tickets_remaining))
        except ValueError as err:
            print("Error: {}. Please try again. ".format(err))
        else:
            if tickets_to_purchase == 0:
                print("You must purchase at least one ticket.")
            else:
                total_tickets_price = calculate_price(tickets_to_purchase)
                print("Your total price for the tickets is: ${}".format(total_tickets_price))
                valid_purchase = True

    # ----- Project Requirement: 4 -----
    # Prompt user if they want to proceed. Y/N
    # If they want to proceed, print out to the screen "SOLD!" to confirm the purchase.
    # Decrement the number of tickets bought.
    # Otherwise, thank them by their name.
    customer_consent = input("Would you like to proceed? Y/N: ").upper()

    if customer_consent == 'Y':
        print("SOLD!")
        tickets_remaining -= tickets_to_purchase

    if customer_consent == 'N':
        print("No tickets purchased. Thank you and have a nice day.")

# ----- Project Requirement: 5 -----
# Notify user that the tickets are sold out.
sys.exit("Tickets are sold out. Goodbye.")
