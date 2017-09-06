
# =================================
#   LISTS
# =================================

# Generate a list
test = ['a', 'b', 'c', 'd']


test[2]  # Access item
test[-1]  # Access last item in list
print(test[0:3])  # Split the list
print(test[1:3])
print(test[:2])  # Return everything before index 2
print(test[2:])  # Return index 2 and beyond
print(test[-2])  # Return 2nd to last item in list
print(test[-2:])  # Return last 2 items in a list
print(test[-2:])  # Return last 2 items in a list
print(test[:-2])  # Return all but last 2 items in a list


test[2] = 'cc'  # Modify item

test.append('e')  # Add item

test.insert(1, 'aa')  # Insert item

del test[1]  # Remove item by index
test.remove('b')  # Remove item by value -> only removes first instance so if multiple need a loop

test_popped = test.pop()  # Remove last item in a list and pass it to the variable name
test_popped = test.pop(0)  # Pop 1st item in list -- can define by indexes

test.sort(reverse=True)  # Sort a list alphabetically permanatenly
sorted(test)  # Temporarily sort a list
test.reverse()  # Reverse the order of a list


# =================================
#   ITERATING LISTS
# =================================

for i in range(0, len(test)):  # Print index
    print(i)

for v in test:  # Print Value
    print(v)

for i, v in enumerate(test):  # Print index and value
    print(i, v)

for v in reversed(test):  # Iterate in reverse
    print(v)

for i, v in reversed(list(enumerate(test))):  # Reverse over index and values
    print(i, v)

for i in range(len(test) - 1, -1, -1):  # Reverse index
    print(i)

# =================================
#   WORKING WITH RANGES
# =================================

# Notes: When working with ranges remember lists will exclude the last name of the range when iterrating

for v in range(0, 5):
    print(v)

numbers = list(range(0, 5))  # Use "list" to convert a range to a list
even_numbers = list(range(2, 11, 2))  # Return only even numbers

list = []
for v in range(1, 11):
    list.append(v**2)

print(list)
print(min(list), max(list), sum(list))

# =================================
#   LIST COMPREHENSIONS
# =================================

# This will automatically iterate over a range and build a list for you

# Build a list of squares

# something = [action_on_value for value in range]
# OR better yet: [ACTION then for statement]
list = [value**2 for value in range(1, 11)]
[print(v) for v in list]


# =================================
#   TUPLES
# =================================

# A Tuple looks just like a list but you use() and not brackets. It is the same but cannot change ever


# =================================
#   PRACTICE EXERCISES
# =================================


# ------------------------------
# Practice: Dinner with friends
# ------------------------------

# Generate a list of friends to invite
dinner_invites = ['J Cole', 'Hannah', 'Dan Angster']

for i in reversed(range(len(dinner_invites))):
    print(i)

for friends in dinner_invites:
    print("{}, I hope you can make it to dinner".format(friends))

print("Unfortunately, {} cannot make it to the dinner party".format(dinner_invites[2]))

# Replace Dan with Caleb and resend messages
dinner_invites[2] = 'Caleb Jones'

for friends in dinner_invites:
    print("{}, I hope you can make it to dinner".format(friends))

# Send a message that we got a bigger table and add people to the list
for friends in dinner_invites:
    print("{}, We found a bigger table and will be inviting more friends!".format(friends))

dinner_invites.insert(0, 'Julie')  # Add to beginning of list
dinner_invites.insert(len(dinner_invites) // 2, 'Sarah')  # Add to middle of list
dinner_invites.append('Britt Parnell')  # Add to end of list

for friends in dinner_invites:
    print("{}, I hope you can make it to dinner.".format(friends))

print('Y2ou can only invite 2 people for dinner')

'''
for x in reversed(dinner_invites):
    if len(dinner_invites) > 2:
        uninvited = dinner_invites.pop(dinner_invites.index(x))
        print("Sorry {}, you can't come to my dinner anymore".format(uninvited))
    else:
        print("{}, you can come to my party!".format(x))
        dinner_invites.remove(x)
'''

# OR
for i, v in reversed(list(enumerate(dinner_invites))):
    if i > 1:
        uninvited = dinner_invites.pop(i)
        print("Sorry {}, you aren't invited anymore".format(uninvited))
    else:
        print("{}, You can come to my party!".format(v))
        del dinner_invites[i]

print(dinner_invites)


# ------------------------------
# Practice: Places in the World
# ------------------------------

places = ['Mexico',
          'Colombia',
          'Ecuador',
          'France',
          'Brazil']

print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))


# ------------------------------
# Practice: Iterate Lists
# ------------------------------

pizzas = ['Pepperoni', 'Hawaiian', 'Cheese']

for pizza in pizzas:
    print("I like {} pizza!".format(pizza))

print("I am a really big fan of pizza. \nIt is one of my favs. \nYep I love it!")

for value in range(1, 5):
    print(value)


for value in range(1, 21):
    print(value)

numbers = list(range(1, 21))
print(min(numbers), max(numbers))

numbers = list(range(1, 20, 2))
for v in numbers:
    print(v)

numbers = [value * 3 for value in range(3, 31, 3)]

numbers = [value**3 for value in range(1, 11)]
for value in numbers:
    print(value)


# ------------------------------
# WORKING WITH SLICES
# ------------------------------

# Use places
print(places)

print("The first 3 items in the list are: {}".format(places[:3]))
print("3 Items from the middle of the list are: {}".format(places[2:5]))
print("The last 3 items in the list are: {}".format(places[-3:]))

# Use pizzas
print(pizzas)
friends_pizzas = pizzas[:]
friends_pizzas.append('Meat Lovers')

print("My favorite pizzas are:")
[print("\t{}".format(x)) for x in pizzas]
print("Calebs favorite pizzas are:")
[print("\t{}".format(x)) for x in friends_pizzas]
