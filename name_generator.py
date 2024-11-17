import random
import sys
import time

import name_variations

print("This is Name Generator")
print("")

#  ----- To do list ----- #
#  user can select options
#  show total number of names
#  add a new name to the file
#  select a random name from the file
#  exit
#  clean up code


def name_options():
    print("Please select an option: ")
    print("1. Show total number of names")
    print("2. Add a new name to the file")
    print("3.  Select a random name from the file")
    print("4. Exit")

    user_input = int(input("Enter your choice (1-4): "))

    input_options(user_input)


def input_options(num_selection):
    match num_selection:
        case 1:
            name_variations.view_name_count()
        case 2:
            name_variations.create_name()
        case 3:
            name_variations.random_name_view()
        case 4:
            # exit
            print("Thank you for using name generator")
            sys.exit()


while True:
    name_options()
