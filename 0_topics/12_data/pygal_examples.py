#------------------------------
#   Plotting with Pygal
#------------------------------

from die import Die
import matplotlib.pyplot as plt
import pygal
import webbrowser
from random_walk import RandomWalk

die = Die()

# Make some rolls and store as a list
results = []
[results.append(die.roll()) for x in range(1000)]

# Analyze Results
x_values = list(range(1, die.num_sides + 1))
frequencies = [results.count(x) for x in x_values]

print(frequencies)

plt.close()
plt.bar(x_values, frequencies)
plt.show()

hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Results'
hist.y_title = 'Frequency of Results'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

# Use xc helper to open in browser OR
xc.open_in_browser('die_visual.svg')

# Render in browser from pygal directly
hist.render_in_browser()

#------------------------------
#   Rolling 2 die
#------------------------------

die_1 = Die()
die_2 = Die()

# Roll the dice a bunch of times
results = []
[results.append(die_1.roll() + die_2.roll()) for x in range(25000)]

# Analyze results
max_results = die_1.num_sides + die_2.num_sides
frequencies = [results.count(x) for x in range(2, max_results + 1)]

# For x labels
str_list = []
str_list = [str(x) for x in range(2, max_results + 1)]

hist = pygal.Bar()

hist.title = "Results of two die rollings"
hist.x_labels = str_list
hist.x_title = 'Results'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_in_browser()


#------------------------------
#   Try Random Walk with PyGal
#------------------------------

rw = RandomWalk()
rw.fill_walk()

chart = pygal.XY(stroke=False)
chart.add('test', list(zip(rw.x_values, rw.y_values)))
chart.render_in_browser()

test = [rw.x_values, rw.y_values]
