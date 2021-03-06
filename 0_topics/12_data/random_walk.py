# Random walk
import matplotlib.pyplot as plt
from random import choice


class RandomWalk():
    """A random walk similator"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in the direction
            x_direction = choice([-1,1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere:
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


def plot_rw(rw):
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)

    # Emphasize first and last points
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    # Remove axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.figure(figsize=(10, 6))

    plt.show()
