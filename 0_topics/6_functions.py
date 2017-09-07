# =================================
#   FUNCTIONS
# =================================


# Clearly can build standard returns of values but can also return dictionaries

def build_person(first_name, last_name):
    """return info about a person"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('xan', 'caperton')


# Build get some names
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at anytime to quit")
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    print("\nHello {} {}".format(f_name.title(), l_name.title()))


def make_album(name, artist, tracks=''):

    album = {'name': name, 'artist': artist}
    if tracks:
        album['tracks'] = tracks

    return album


j_cole = make_album('Cole World', 'J Cole')
jay_z = make_album('Black Album', 'Jay-z')
beyonce = make_album('Fruits', 'Beyonce', 10)

albums = [j_cole, jay_z, beyonce]

while True:
    print("Add an album to your list:")
    artist = input("Artist name: ")

    if artist == 'q':
        break

    album = input("Album name: ")
    if album == 'q':
        break

    tracks = int(input("Number of tracks (optional): "))
    if tracks == 'q':
        break

    albums.append(make_album(album, artist, tracks))
    print(albums)
    print("\nThis is the stuff".format(other))


# NOTE: A list passed to a function can be altered and changes are permanent
# However you can pass a copy of the list like so list[:]

unprinted = ['tshirt', 'pants', 'hat']
printed = []


def print_items(unprinted_designs, completed_models):
    while unprinted_designs:
        t = unprinted_designs.pop()

        print("Printing {}".format(t))
        completed_models.append(t)


def show_printed(completed_models):
    print("The following designs have been printed:")
    for f in completed_models:
        print(f)


print_items(unprinted_designs, printed)
show_printed(printed)

# OR

print_items(unprinted_designs[:], printed)  # will maintain original list


def function_name(*toppings):  # will allow user to pass any amount of args as a tuple


def function_name(size, *toppings):


def build_profile(first, last, **user_info):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')


def make_sammy(*fixings):
    print("Making your sandwich with:")
    for fixing in fixings:
        print("\n{}".format(fixing))
