#------------------------------
#   Examples of MatPlotLib
#------------------------------


import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

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
#   Make multiple Random Walks
#------------------------------


while True:
    # Make a random walk and plot the points
    rw = RandomWalk(50000)
    rw.fill_walk()
    plot_rw(rw)

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
