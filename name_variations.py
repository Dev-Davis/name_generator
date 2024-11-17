import time
import random

def create_name():
    # add new name to the file
    new_name = input("Input a new name to add: ")
    file = open('names.txt', 'a')
    file.write(new_name + "\n")
    file.close()
    print(f"{new_name} was added")
    print("")
    time.sleep(1)


def view_name_count():
    # show total number of names
    file = open('names.txt', 'r')
    names = file.readlines()
    file.close()
    print(f"There are {len(names)} names in the file")
    print("")
    time.sleep(1)


def random_name_view():
    # select a random name
    file = open('names.txt', 'r')
    names = file.readlines()
    print(random.choice(names))
    print("")
    time.sleep(1)
