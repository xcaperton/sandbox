# =================================
#   DICTIONARIES
# =================================

# When looping you can use .keys() [default], .values() or .items()
# Use set(dictionary) to return the list without duplicates


alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned {} points".format(new_points))

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

# =================================
#   EXAMPLES
# =================================

caleb = {
    "first_name": "Caleb",
    "last_name": "Jones",
    "age": 30,
    "city": "Richmond"
}

for x in caleb.keys():
    print(caleb[x])

fav_numbers = {
    "Hannah": 10,
    "Xan": 13,
    "CT": 21,
}

for x in fav_numbers:
    print(x, fav_numbers[x])


glossary = {
    "Print": "Prints a string",
    "Print2": "Prints a string",
    "Lower": "Turns the string lower case",
    "Upper": "Make the string all upper case",
    "Title": "Capitalizes the first letters in a string",
}

for key, value in glossary.items():
    print("{}: {}\n".format(key, value))

for func, definit in glossary.items():
    print("{}: {}\n".format(func, definit))

for names in glossary.keys():
    print(names)

for names in sorted(glossary):
    print(names)

for names in (glossary.values()):
    print(names)

for names, defs in sorted(glossary.items()):
    print("{}: {}".format(names, defs))

for names in set(glossary.values()):
    print(names)


# =================================
#   NESTING
# =================================

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


aliens = []

for v in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("There are a total of {} aliens in the list".format(len(aliens)))


for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

friend_1 = {'first_name': 'hannah', 'last_name': 'pace', 'location': 'cville'}
friend_2 = {'first_name': 'caleb', 'last_name': 'jones', 'location': 'richmond'}
friend_3 = {'first_name': 'xan', 'last_name': 'caperton', 'location': 'beach'}

friends = [friend_1, friend_2, friend_3]

for friend in friends:
    print("\n")
    for k, v in friend.items():
        print("{}: {}".format(k, v))

scout = {'name': 'scout', 'type': 'cat'}
hoover = {'name': 'hoover', 'type': 'dog'}
beau = {'name': 'beau', 'type': 'dog'}

pets = [scout, hoover, beau]

print("\n")
for pet in pets:
    print("\n")
    for k, v in pet.items():
        print("{}: {}".format(k, v))

favorite_places = {
    "caleb": ['Richmond', 'OBX', 'Pluto'],
    "hannah": ['Africa', 'South America', 'Greece'],
    "xan": ['Surfing', 'OBX', 'Florida'],
}

for friend, places in favorite_places.items():
    print("{}'s favorite places are:".format(friend))
    for place in places:
        print("\t{}".format(place))

friend_1['favorite_numbers'] = [5, 7, 9]
friend_2['favorite_numbers'] = [2]
friend_3['favorite_numbers'] = [11, 77]

for friend in friends:
    print("{}'s fav numbers are:".format(friend['first_name'].title()))
    for number in friend['favorite_numbers']:
        print("\t{}".format(number))

cities = {
    'Richmond': {
        'country': 'USA',
        'population': 100000,
        'fact': 'This is the best city ever',
    },
    'Cartagena': {
        'country': 'Colombia',
        'population': 800000,
        'fact': 'This city is super hot',
    },
    'Athens': {
        'country': 'Greece',
        'population': 120600,
        'fact': 'We want to volunteer here',
    },
}

for city, city_stats in cities.items():
    print("{}:".format(city))
    for city_stat, city_stat_desc in city_stats.items():
        print("\t{}: {}".format(city_stat, city_stat_desc))


cities['Quito'] = {
    'country': 'Ecuador',
    'population': 1902390,
    'fact': 'This is city was tough on us',
}
