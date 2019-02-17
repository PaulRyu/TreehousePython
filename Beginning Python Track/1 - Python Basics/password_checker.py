# While Loop Lesson
import sys

# Variables
MASTER_PASSWORD = "openSesame"
password = input("Please enter a password: ")
attempt_count = 1

# Loop to handle naive password code
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many attempts. Exiting.")
    password = input("Invalid password. Try again: ")
    attempt_count += 1
print("Password accepted.")
