import random
import time

print("This is Name Generator")
print("")

#  user can select options
#  show total number of names
#  add a new name to the file
#  select a random name from the file
#  exit


def name_options():
    print("Please select an option: ")
    print("1. Show total number of names")
    print("2. Add a new name to the file")
    print("3.  Select a random name from the file")
    print("4. Exit")

    user_input = int(input("Enter your choice (1-4): "))


while True:
    name_options()
