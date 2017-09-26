#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''

You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived 
ten minutes too early to an appointment, so you decided to take the opportunity to go for a 
short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime 
you press the button it sends you an array of one-letter strings representing directions to 
walk (eg. ['n', 's', 'w', 'e']). You know it takes you one minute to traverse one city block, 
so create a function that will return true if the walk the app gives you will take you exactly 
ten minutes (you don't want to be early or late!) and will, of course, return you to your starting 
point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction 
letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a 
walk, that's standing still!).

'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

direction_xy = {'n': [0, 1], 's': [0, -1], 'e': [1, 0], 'w': [-1, 0]}

position = [0, 0]


def isValidWalk(walk):

    if len(walk) != 10:
        return False

    for direction in walk:
        move = direction_xy[direction]
        position[0] += move[0]
        position[1] += move[1]

    if position == [0, 0]:
        return True
    else:
        return False

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


'''
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

a being 1, b being 2, etc.

As an example:

alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" as a string.
'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def alphabet_position(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    nums = [str(letters.find(char) + 1) for char in text.lower() if letters.find(char) >= 0]
    return ' '.join(nums)


test = "The sunset sets at twelve o' clock."
print(alphabet_position(test))


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def find_it(seq):
    unique = set(seq)
    not_found = True
    while not_found:
        for x in unique:
            if seq.count(x) % 2 != 0:
                return x
                not_found = False


test = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]

print(find_it(test))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
