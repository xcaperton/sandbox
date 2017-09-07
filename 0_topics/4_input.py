# =================================
#   USER INPUTER
# =================================


message = input("Tell me something about you:")
print(message)

# Writing a longer prompts
prompt = """We want to learn some more info from you:

Please tell us your father:"""
print(input(prompt))


# Make sure to convert strings to integers if needed
height = input("How tall are you, in inches?")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# Determine even or odd
number = input("Enter a number and I'll tell you if it is even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number {} is even.".format(number))
else:
    print("\nThe number {} is odd.".format(number))


car = input("What kind of car are you looking for? ")
print("Let me see if I can find you a {}.".format(car))

people = int(input("How many people are you expecting? "))
if people > 8:
    print("\nI'm sorry you'll have to wait for a table.".format(people))
else:
    print("\nYou're table is ready")

number = int(input("Give me a number: "))
if number % 10 == 0:
    print("\nThe number is divisble by 10!")
else:
    print("\nThe number isn't divisble by 10, sorry")

# =================================
#   WHY LOOPS
# =================================

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Program
prompt = """
Tell me something and I will repeat it back.

> Type 'quit' to exit
"""

active = True
while active:
    message = input(prompt)

    if message.lower() != 'quit':
        print(message)
    else:
        active = False

# Loops can also be set with 'while TRUE:' to run forever
#   until a 'break' is called

while True:
    city = input('Tell me a city you like:')

    if city == 'quit':
        break
    else:
        print("\nI am glad you think that {} is great.".format(city))


# Using continue is a bit weird however it does the following:
# When a loop comes to continue it will skip rest of code and go to
# the top of the loop

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2:
        continue

    print(current_number)

# Movie program!
total_people = int(input("How many people are in your party?"))

people = 1
total = 0
while people <= total_people:
    people += 1
    age = int(input("How old is the movie goer? "))

    if age < 4:
        cost = 0
    elif age < 16:
        cost = 10
    else:
        cost = 15

    total += cost
    print("\nThe ticket will cost {}".format(str(cost)))

print("\nThat'll be a total of ${}".format(total))

# One way to guess numbers
active = True
while active:
    if int(input("Guess a number:")) == 7:
        active = False
        print("You got it!")

print("End")

# Another way to guess numbers
while True:
    if int(input("Guess a number:")) == 7:
        print("You got it!")
        break

# Don't modify things in a for loop but instead us a while loop

unconfirmed_users = ['Xan', 'Hannah', 'Caleb']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: {}".format(current_user.title()))
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())

# Remove all instances from a list

pets = ['dog', 'cat', 'dog', 'parrot', 'dog', 'other']
print(pets)

while 'dog' in pets:
    pets.remove('dog')

print(pets)


# Storing data to dictionaries

responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for person's name and responses
    name = input("What is your name? ")
    response = input("Do you like D Trump? ")

    # Store responses
    responses[name] = response
    repeat = input("Would you like someone else to response? (yes/no)")

    if repeat == 'no':
        polling_active = False

# Polling complete
print("\n --- POLL RESULTS ---")
for name, response in responses.items():
    print("{}: {}".format(name, response))


# LAST EXAMPLES

sandwich_orders = ['PBJ', 'Ham and Cheese', 'Peperroni', 'Pastrami', 'Pastrami']
completed = []

while sandwich_orders:
    sammy = sandwich_orders.pop()

    print("Making this sammy: {}".format(sammy))

    completed.append(sammy)

print("We've only got {} Pastrami's left".format(sandwich_orders.count('Pastrami')))
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print("We are all out of pastrami, see:")
print(sandwich_orders)
print("All the sandwiches are done son")

[print(x) for x in range(0, 5)]
