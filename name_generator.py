import random
import time, sys

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

    input_options(user_input)


def input_options(num_selection):
    match num_selection:
            case 1:
                # show total number of names
                file = open('names.txt', 'r')
                names = file.readlines()
                file.close()
                print(f"There are {len(names)} names in the file")
                time.sleep(1)

                print("")
            case 2:
                # add new name to the file
                new_name = input("Input a new name to add: ")
                file = open('names.txt', 'a')
                file.write(new_name + "\n")
                print(f"{new_name} was added")
                file.close()

                # names.append(new_name)

                # file = open('names.txt',  'w')
                # file.writelines(names)
                # print(f"{new_name} was added")
                # file.close()
                time.sleep(1)
            case 3:
                # select a random name
                file = open('names.txt', 'r')
                names = file.readlines()
                # for name in names:
                print(random.choice(names))
                time.sleep(1)
            case 4:
                # exit
                print("Thank you for using name generator")
                sys.exit()


while True:
    name_options()
