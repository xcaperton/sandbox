from bokeh.io import export_png, export_svgs, save
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot, row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs
from random import randint
from numpy import pi
import numpy as np

# Generate Mock Data
skills = ['speed', 'power', 'pass', 'shot', 'defense', 'stamina']
skill_rating = [randint(30, 100) / 100 for x in range(len(skills))]
skill_rating_perfect = [1, 1, 1, 1, 1, 1]
skill_rating75 = [.75, .75, .75, .75, .75, .75]

# Get angles to be used
angles = get_angles(skills)
points = equal_points_on_circle(skill_rating, angles, center=[2, 2])
points_perfect = equal_points_on_circle(skill_rating_perfect, angles, center=[2, 2])
points_75 = equal_points_on_circle(skill_rating75, angles, center=[2, 2])

# Plot Figure
output_file('test.html', mode='inline')

p = figure(plot_width=600, plot_height=600, x_range=(0, 4), y_range=(0, 4), title='Skills Radial')
#p.circle(2, 2, radius=1, alpha=.2)
p.patch(points_perfect[0], points_perfect[1], alpha=.2, color='grey')
p.patch(points_75[0], points_75[1], alpha=.2, color='grey')
p.patch(points[0], points[1], alpha=.5, color='firebrick')
p.circle([2], [2], size=5, color='black', alpha=.5)
show(p)

#--------------------------------------
#   GENERATE PLOT DATA FUNCTIONS BELOW
#--------------------------------------


def get_angles(skills):
    angle = 0
    angles = []
    for x in range(len(skills)):
        angle += (pi / (len(skills) / 2))
        angles.append(angle)

    return angles


def equal_points_on_circle(skills, angles, center=[0, 0]):
    points = []
    for x in range(len(skills)):
        points.append(xy_point_on_circle(angles[x], center=center, radius=skills[x]))
        point_list = [list(xy) for xy in zip(*points)]

    return point_list


def xy_point_on_circle(angle, center=[0, 0], radius=1):
    '''
        Finding the x,y coordinates on circle, based on given angle
    '''
    from math import cos, sin, pi
    # center of circle, angle in degree and radius of circle
    x = center[0] + (radius * cos(angle))
    y = center[1] + (radius * sin(angle))

    return x, y
