import math


def split_check(bill_total, number_of_people):
    return math.ceil(bill_total / number_of_people)


try:
    total_due = float(input("What is the total?  "))
    numPeople = int(input("How many people?  "))

except ValueError:
    print("That is not a valid value. Please try again...")

else:
    amount_due = split_check(total_due, numPeople)
    print("Each person owes ${}".format(amount_due))
