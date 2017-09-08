# =================================
#   STORING DATA
# =================================

import json

# Use JSON to store and read data

# WRITE to JSON
numbers = [2, 3, 5, 7, 12]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# READ from JSON
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)


# Prompt for username then remember upon returnk
username = input("What is your name? ")
filename = 'username.JSON'

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)

    print("We will remember you when you come back, {}".format(username))

with open(filename) as f_obj:
    username = json.load(f_obj)

    print("Welcome back, {}".format(username))


# =================================
#   REMEMBER ME EXERCISE
# =================================


def greet_user():
    """Greet user by name"""
    filename = 'username.json'
    try:
        with open(filename) as f_obJ:
            username = json.load(f_obJ)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
    else:
        print("Welcome back, {}.".format(username))


greet_user()

# REFACTORING


def get_stored_username():
    """return stored username"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Request new username"""
    filename = 'username.json'
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

    return username


def greet_user():
    """greeet a user"""
    username = get_stored_username()
    if username:
        print("Welcome back, {}".format(username))
    else:
        username = get_new_username()
        print("We will remember you next time, {}.".format(username))


def greet_user2():
    """greeet a user"""
    username = get_stored_username()
    if username:
        correct_name = input("Is {} your username? (y/n)".format(username))
        if correct_name == 'n':
            username = get_new_username()
            print("We will remember you next time, {}".format(username))
        else:
            print("Welcome back, {}".format(username))
    else:
        username = get_new_username()
        print("We will remember you next time, {}.".format(username))


greet_user()
greet_user2()
