# =================================
#   IF STATEMENTS
# =================================

cars = ['audi', 'bmw', 'suburu', 'benz']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

interested_cars = ['bmw', 'outback']

for car in interested_cars:
    if car in cars:
        print("We have some {}'s on the lot!".format(car))
    else:
        print("Sorry we don't have any {}'s on the lot".format(car))

user_age = input("What is your age?")


# =================================
#   HELLO ADMIN
# =================================

current_users = ['Admin', 'XCaperton', 'Chenaujr', 'HWpace', 'Locaperton']

if current_users:
    for user in current_users:
        if user.lower() == 'admin':
            print("Hello {}, would you like to see a status report?".format(user))
        else:
            print("Hello {}, welcome back!".format(user))
else:
    print("We need to find some users!")

del current_users[:]


new_users = ['xcaperton', 'otherboi', 'schuleb']

for user in new_users:
    if user.lower() in [v.lower() for v in current_users]:
        print("The username {} is not available. Please select another".format(user))
    else:
        print("The userame {} is available!".format(user))

# Numbers and printing
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        st = 'st'
    elif number == 2:
        st = 'nd'
    elif number == 3:
        st = 'rd'
    else:
        st = 'th'

    print("{}{}".format(str(number), st))

