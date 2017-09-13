# Generating Data

import os
ppath = "/Users/johncaperton/Projects/sandbox/0_topics/12_data/data.py"
ret = ppath[:ppath.rfind('/', 0)]
os.chdir(ret)

import matplotlib
import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Simple plot
input_values = range(1, 6)
squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=15)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()


# Plot Scatters
plt.close()
x_vals = range(1, 1001)
y_vals = [x**3 for x in x_vals]
plt.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Blues, s=40)
plt.show()

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()


while True:
    # Make a random walk and plot the points
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
