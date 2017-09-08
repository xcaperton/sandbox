# =================================
#   READING FILES
# =================================

# Basic Read
with open('docs/txt_file.txt') as file_object:
    contents = file_object.read()
    print(contents)

# Basic read and remove blanks at end
with open('docs/txt_file.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# Read and loop over lines
with open('docs/txt_file.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# Read and loop over lines using readlines()
with open('docs/txt_file.txt') as file_object:
    lines = file_object.readlines()

# create pi string
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(pi_string[:10])  # First 10 digis

# =================================
#   PRACTICE READING HTML FILE AND PARSING
# =================================


# Read HTML file
# Nice way to read file and strip lines

def valid_line(line):
    status = True

    if line[:4] != '<td>' and line[:4] != '<th>':
        status = False

    if len(line) <= 4:
        status = False

    return status


with open('docs/test.html') as file_object:
    lines = [line.strip() for line in file_object]

tds = []
for line in lines:
    if valid_line(line):
        tds.append(line[4:-5])

y = 0
splits = []
for x in range(0, len(tds), 10):
    #list_name = 'list' + str(y)
    splits.append(tds[x:(x + 9)])

print(splits)

# =================================
#   WRITING FILES
# =================================

''' You can open a file in:
 'r' - read mode
 'w' - write mode
 'a' - append mode
 'r+' - write and write to file
 '''

# Note: Write mode will erase all contents before passing the objects

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love Hannah.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love cheese.")

# =================================
#   PRACTICE WRITE FILES
# =================================

names = input("What is your name?: ")
filename = 'guests.txt'

with open(filename, 'a') as file_object:
    file_object.write("{}\n".format(names))

filename = 'whyprogram.txt'

while True:
    reason = input("Why do you like programming? \n(press 'q' to quit at anytime)")
    if reason != 'q':
        with open(filename, 'a') as file_object:
            file_object.write("\n{}".format(reason))
    else:
        print("Thanks!")
        break


# =================================
#   EXCEPTIONS
# =================================

while True:
    print("Give me two numbers and I'll divide them:\n")

    first = input("First Number: ")
    if first == 'q':
        break

    second = input("Second Number: ")
    if second == 'q':
        break

    try:
        result = int(first) / int(second)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("You must provide numbers.")
    else:
        print("The result is {}.".format(result))


with open('cats.txt', 'w') as f_obj:
    f_obj.write("Holly\nScout\nTurtle")

with open('dogs.txt', 'w') as f_obj:
    f_obj.write("Hoover\nJac\nBasil")


def open_and_print(filename):
    try:
        with open(filename, 'r') as f_obj:
            lines = [line.strip() for line in f_obj]
            for line in lines:
                print(line)
    except FileNotFoundError:
        print("Couldn't find the file {}.".format(filename))
        # pass -- use pass to fail silently
