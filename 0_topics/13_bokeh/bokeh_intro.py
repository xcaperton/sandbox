#------------------------------
#   Bokeh start
#------------------------------
from bokeh.io import export_png, export_svgs, save
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot, row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Panel, Tabs
from random import choice
import pygal
import numpy as np
from math import pi

# map to inline for working OFFLINE
output_file("test.html", mode='inline')


p = figure()

x_vals = range(1, 6)
y_Vals = [x * 3 for x in x_vals]

p.line(x_vals, y_Vals, line_width=5)
show(p)

t = list(zip(x_vals, y_Vals))


class RandomWalk():
  """Randomwalk simulation"""

  def __init__(self, num_steps=500):
    self.num_steps = num_steps
    self.x_vals = [0]
    self.y_vals = [0]

  def get_x_step(self):
    """Calculate X step"""
    x_direction = choice([-1, 1])
    x_step = choice([1, 2, 3, 4, 5])
    x_move = x_direction * x_step

    return x_move

  def get_y_step(self):
    """Calculate y step"""
    y_direction = choice([-1, 1])
    y_step = choice([1, 2, 3, 4, 5])
    y_move = y_direction * y_step

    return y_move

  def fill_walk(self):
    for step in range(self.num_steps):
      self.x_vals.append(self.x_vals[-1] + self.get_x_step())
      self.y_vals.append(self.y_vals[-1] + self.get_y_step())


# Generate Random Walk
rw = RandomWalk()
rw.fill_walk()

# Plot basic scatter
p1 = figure(title='Random Walk', x_axis_label='X Vals', y_axis_label='Y Vals')
p1.scatter(rw.x_vals, rw.y_vals, line_width=5)
show(p1)


#------------------------------
#   More Advanced Plot
#------------------------------

# With Bokeh

# Prep some data
x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y0 = [i**2 for i in x]
y1 = [10**i for i in x]
y2 = [10**(i**2) for i in x]

p = figure(
    tools="pan,reset,box_zoom,save",
    y_axis_type="log", y_range=[.001, 10**11], title='Log Axis Example',
    x_axis_label='sections', y_axis_label='particles'
)

# Add some renderers
p.line(x, x, legend="x=x")
p.circle(x, x, legend="y=x", fill_color="white", size=8)
p.line(x, y0, legend="y=x^2", line_width=3)
p.line(x, y1, legend="y=10^x", line_color="red")
p.circle(x, y1, legend="y=10^x", fill_color="red", line_color="red", size=6)
p.line(x, y2, legend="y=10^x^2", line_color="orange", line_dash="4 4")

show(p)


# With Pygal

test = pygal.Line()
sets = list(zip(x, y1))
test.x_labels = [str(x) for x in x]
test.title = 'Stuff with PyGal'
test.x_title = 'X vals'
test.y_title = 'Y vals'
test.add('x', x)
test.add('y', y0)
test.add('y1', y1)

test.render_in_browser()

t = np.random.random(size=3) * 100

#------------------------------
#   More Examples with Bokeh
#------------------------------

# prepare some data
N = 4000

# Create arrays for X & Y and store N values of each
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5

# Somehow generate color codes
colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50 + 2 * x, 30 + 2 * y)
]
# output to static HTML file (with inline resources)
output_file("color_scatter.html", title="color_scatter.py example", mode="inline")

TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

# create a new plot with the tools above, and explicit ranges
p = figure(tools=TOOLS, x_range=(0, 100), y_range=(0, 100))

# add a circle renderer with vectorized colors and sizes
p.circle(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

# show the results
show(p)


#------------------------------
#   Bokeh: Linked Panning
#------------------------------


# prepare some data
N = 100
x = np.linspace(0, 4 * np.pi, N)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.sin(x) + np.cos(x)

# output to static HTML file
output_file("linked_panning.html", mode='inline')

# hover = HoverTool(tooltips=None,mode='vline')


# create a new plot
s1 = figure(width=250, plot_height=250, title=None)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)
# s1.add_tools(hover)

# NEW: create a new plot and share both ranges
s2 = figure(width=250, height=250, x_range=s1.x_range, y_range=s1.y_range, title=None)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

# NEW: create a new plot and share only one range
s3 = figure(width=250, height=250, x_range=s1.x_range, title=None)
s3.square(x, y2, size=10, color="olive", alpha=0.5)

# NEW: put the subplots in a gridplot
p = gridplot([[s1, s2, s3]], toolbar_location=None)
# show the results
show(p)

# Grid plot customs
l = gridplot([[s1, s2], [s3]])
show(l)

# Usings tabs
tab1 = Panel(child=s1, title='tab1')
tab2 = Panel(child=s2, title='tab2')
tab3 = Panel(child=s3, title='tab 3')
layout = Tabs(tabs=[tab1, tab2, tab3])
show(layout)


#------------------------------
#   Bokeh: Linked Brushing
#------------------------------

# Essentially linked through the source because X is common across both plots

output_file('linked_brushing', mode='inline')

source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))

TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

# Create a new plot and add a renderer
left = figure(tools=TOOLS, width=350, height=350, title=None)
left.circle('x', 'y0', source=source)

# Create another new plot and add a renderer
right = figure(tools=TOOLS, width=350, height=350, title=None)
right.circle('x', 'y1', source=source)

p = gridplot([[left, right]])

show(p)

#------------------------------
#   Simple Plottings
#------------------------------


# TIP: Create a dict of two arrays
test = dict(x=x, y0=y0)

# Draw Rectangles
p = figure(plot_width=400, plot_height=400)
p.quad(top=[2, 3, 4], bottom=[1, 2, 3], left=[1, 2, 3],
       right=[1.2, 2.5, 3.7], color="#B3DE69")
show(p)


# Vertical Bar Chart
p = figure(plot_width=400, plot_height=400)
p.vbar(x=[1, 2, 3], width=0.5, bottom=0,
       top=[1.2, 2.5, 3.7], color="firebrick")
show(p)


# Patch Chart
p = figure(plot_width=400, plot_height=400)
# add a patch renderer with an alpha an line width
p.patch([1, 2, 3, 4, 5], [6, 7, 8, 7, 3], alpha=0.5, line_width=2)
show(p)


# Multiline
p = figure(plot_width=400, plot_height=400)
p.multi_line([[1, 3, 2], [3, 4, 6, 6]], [[2, 1, 4], [4, 7, 8, 5]],
             color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=4)
show(p)

# Ovals
p = figure(plot_width=400, plot_height=400)
p.oval(x=[1, 2, 3], y=[1, 2, 3], width=0.2, height=40, color="#CAB2D6",
       angle=pi / 3, height_units="screen")
show(p)

# p = figure(plot_width=400, plot_height=400)
p.ellipse(x=[1, 2, 3], y=[1, 2, 3], width=[0.2, 0.3, 0.1], height=0.3,
          angle=pi / 3, color="#CAB2D6")
show(p)


# Line segments

p = figure(plot_width=400, plot_height=400)
p.segment(x0=[1, 2, 3], y0=[1, 2, 3], x1=[1.2, 2.4, 3.1],
          y1=[1.2, 2.5, 3.7], color="#F4A582", line_width=3)

show(p)

# Rays
p = figure(plot_width=400, plot_height=400)
p.ray(x=[1, 2, 3], y=[1, 2, 3], length=45, angle=[30, 45, 60],
      angle_units="deg", color="#FB8072", line_width=2)

show(p)

# Arcs
p = figure(plot_width=400, plot_height=400)
p.arc(x=[1, 2, 3], y=[1, 2, 3], radius=0.8, start_angle=0, end_angle=2, color="navy")

show(p)

# Wedge
p = figure(plot_width=400, plot_height=400)
p.wedge(x=[1, 2, 3], y=[1, 2, 3], radius=0.2, start_angle=0.4, end_angle=4.8,
        color="firebrick", alpha=0.6, direction="clock")
show(p)

# Annual Wedge ***
p = figure(plot_width=400, plot_height=400, x_range=(0, 2), y_range=(0, 2))
p.annular_wedge(x=[1], y=[1], inner_radius=0.3, outer_radius=0.5,
                start_angle=pi / 2, end_angle=3.14, color="green", alpha=0.6)
show(p)

# Annulus wedge
p = figure(plot_width=400, plot_height=400)
p.annulus(x=[1, 2, 3], y=[1, 2, 3], inner_radius=0.1, outer_radius=0.25,
          color="orange", alpha=0.6)

show(p)


#------------------------------
#   Plotting scales
#------------------------------


# Categorical

factors = ["a", "b", "c", "d", "e", "f", "g", "h"]
x = [50, 40, 65, 10, 25, 37, 80, 60]

output_file("categorical.html", mode='inline')
p = figure(y_range=factors)
p.circle(x, factors, size=15, fill_color="orange", line_color="green", line_width=3)
show(p)
