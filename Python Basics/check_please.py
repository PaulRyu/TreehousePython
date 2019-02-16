import math


def split_check(bill_total, number_of_people):

    if number_of_people <= 1:
        raise ValueError("More than one person is required to split the check.")
    return math.ceil(bill_total / number_of_people)


try:
    total_due = float(input("What is the total?  "))
    numPeople = int(input("How many people?  "))
    amount_due = split_check(total_due, numPeople)

except ValueError as err:
    print("That is not a valid value. Please try again...")
    print("({})".format(err))

else:
    print("Each person owes ${}".format(amount_due))
