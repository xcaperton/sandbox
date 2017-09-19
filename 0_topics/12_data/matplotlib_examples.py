# Generating Data

import os
ppath = "/Users/johncaperton/Projects/sandbox/0_topics/12_data/data.py"
ret = ppath[:ppath.rfind('/', 0)]
os.chdir(ret)

import matplotlib
import matplotlib.pyplot as plt
from random_walk import RandomWalk


#------------------------------
#   Simple plots
#------------------------------

input_values = range(1, 6)
squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)
plt.show()
plt.close()

# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=15)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show(block=False)

#------------------------------
#   Plot with Color Map
#------------------------------

# Plot Scatters
plt.close()
x_vals = range(1, 1001)
y_vals = [x**3 for x in x_vals]
plt.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Blues, s=40)
plt.show()


#------------------------------
#   Random Walk Plot
#------------------------------

rw = RandomWalk()
rw.fill_walk()

if plt:
    plt.close()

plt.figure(figsize=(10, 6))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)

# Emphasize first and last points
plt.scatter(0, 0, c='green', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

# Remove axes
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

#------------------------------
#   Random Walk plot 2
#------------------------------

rw = RandomWalk()
rw.fill_walk()

if plt:
    plt.close()

plt.figure(figsize=(10, 6))

point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, linewidth=3)

# Emphasize first and last points
#plt.plot(0, 0, c='green', s=100)
#plt.plot(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

# Remove axes
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
