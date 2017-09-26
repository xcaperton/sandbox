#------------------------------
#   Surfline API and Charting with Bokeh
#------------------------------

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

bob sam Bob

import csv
import urllib.request
import json
from bokeh.plotting import figure, output_file, show
from datetime import datetime
import numpy as np
from bokeh.models import HoverTool, CrosshairTool
from bokeh.models import Legend
from random import randint
from bokeh.palettes import Category20c
from bokeh.models import ColumnDataSource

#------------------------------
#   Functions for grabbing surfline info
#------------------------------


def get_dates(location_dict):
    temp = []
    for day in location_dict['Surf']['dateStamp']:
        for times in day:
            temp.append(datetime.strptime(times, '%B %d, %Y %H:%M:%S'))

    return temp


def get_surf_height(location_dict, height_type):
    temp = []
    for items in location_dict['Surf'][height_type]:
        for item in items:
            temp.append(item)

    return temp

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Pull Request from Surfline
surf = urllib.request.urlopen("http://api.surfline.com/v1/forecasts/5252?resources=surf,analysis&days=12&getAllSpots=True&units=e&interpolate=false&showOptimal=false")
surfj = surf.read()
all_spots = json.loads(surfj)

# Create a list of dicts with relevant info
spots_list = []
for spot in all_spots:
    spot_temp = {}
    spot_temp['dates'] = get_dates(spot)
    spot_temp['surf_min'] = get_surf_height(spot, 'surf_min')
    spot_temp['surf_max'] = get_surf_height(spot, 'surf_max')
    spot_temp['name'] = spot['name']

    spots_list.append(spot_temp)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#------------------------------
#   BUILD BOKEH PLOT
#------------------------------


output_file('test.html', mode='inline')

x = 0
p1 = figure(x_axis_type='datetime', plot_width=800, plot_height=600, title='Surf Heights')
p1.grid.grid_line_alpha = .4
p1.x_range.range_padding = 0
for spot in spots_list:
    x += 1
    l_color = "#{}34a77".format(x)
    band_x = np.append(spot['dates'], spot['dates'][::-1])
    band_y = np.append(spot['surf_min'], spot['surf_max'][::-1])
    p1.patch(band_x, band_y, color=l_color, fill_alpha=.4, legend=spot['name'], muted_color=l_color, muted_alpha=0.1)
p1.legend.location = "top_right"
p1.legend.click_policy = "mute"


show(p1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#------------------------------
#   Build Single Plot for one spot
#------------------------------


output_file('test.html')

# Configure Data
spot = spots_list[0]
spot_dict = spot.copy()
del spot_dict['name']

band_x = np.append(spot['dates'], spot['dates'][::-1])
band_y = np.append(spot['surf_min'], spot['surf_max'][::-1])

source1 = ColumnDataSource(spot_dict)

# Gen Figure attributes
p1 = figure(tools='crosshair', x_axis_type='datetime', plot_width=800, plot_height=600, title='Surf Heights')
p1.grid.grid_line_alpha = .6
p1.ygrid.grid_line_dash = [6, 4]
p1.xgrid.grid_line_color = None
p1.x_range.range_padding = 0
l_color = "#134a77".format(x)

# Renderers
p1.patch(band_x, band_y, color=l_color, fill_alpha=.4, legend=spot['name'], muted_color=l_color, muted_alpha=0.1)
# p1.scatter("dates", "surf_max", source=source1, name='surf_max', line_color=l_color, size=5, fill_color='white',hover_alpha=.6, alpha=0)
p1.line("dates", "surf_min", source=source1, name='surf_min', line_color=l_color)

# Legen
p1.legend.location = "top_right"
p1.legend.click_policy = "mute"

# Crosshair
crosshair = p1.select(dict(type=CrosshairTool))
crosshair.line_alpha = .3
crosshair.line_color = 'grey'

# Other hover
cr = p1.circle("dates", "surf_max", source=source1, size=10,
               fill_color="grey", hover_fill_color="white",
               fill_alpha=0.00, hover_alpha=.95,
               line_color=None, hover_line_color=l_color)

p1.add_tools(HoverTool(tooltips="""
        <HTML>
        <HEAD>
        <style>
        .bk-tooltip {
            background-color: white !important;
            box-shadow: rgba(0, 0, 0, 0.3) 0 2px 10px;
            border-radius: 0px;
            border: 2px solid #3ddb93;
            font-weight: 300;
            font-size: 12px;
            position: absolute;
            padding: 5px;
            pointer-events: none;
            opacity: 0.95;
            }
        .bk-tooltip>div:not(:first-child) {display:none;}
        </style>
        </HEAD>
        <BODY>
        <div style="font-family: verdana; padding: 10px">
        <span style="font-size: 15px;">Surf Heights<br></span>
        <span align="center" style="font-size: 12px; color: #3ddb93;">
        <p>Max Height: @surf_max</p>
        <p>Min Height: @surf_min</p>

        </span>
        </div>
        """,
                       renderers=[cr], mode='vline', show_arrow=False))


show(p1)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#------------------------------
#   Test charting
#------------------------------


def generate_y_data(size=50):
    max = [randint(0, 20) for x in range(1, size + 1)]
    min = [x * (randint(1, 100) / 100) for x in max]

    return min, max, np.append(min, max[::-1])


output_file('test2.html', mode='inline')

# Generate all data
x_rg = list(range(1, 51))
x_data = np.append(x_rg, x_rg[::-1])

data = generate_y_data()

# Add data to dicts
data_patch, data_std = {}, {}

# Patch values
data_patch['y_values'] = data[2]
data_patch['x_values'] = x_data

# Scatter Values
data_std['x_values'] = x_rg
data_std['surf_min'] = data[0]
data_std['surf_max'] = data[1]

source1 = ColumnDataSource(data_patch)
source2 = ColumnDataSource(data_std)

p1 = figure(tools='hover', title='Testing Random Patches', plot_width=800, plot_height=600, x_axis_type='datetime')
p1.x_range.range_padding = 0
p1.patch('x_values', 'y_values', source=source1,
         fill_color='#134a77',
         fill_alpha=.5,
         legend='Random Patch1',
         muted_alpha=.1,
         muted_color='#134a77')
p1.line('x_values', 'surf_max', source=source2, hover_alpha=1)
p1.line('x_values', 'surf_min', source=source2, hover_alpha=1)
p1.legend.click_policy = "mute"

hover = p1.select(dict(type=HoverTool))
hover.tooltips = """
        <HTML>
        <HEAD>
        <style>
        .bk-tooltip {
            background-color: white !important;
            box-shadow: rgba(0, 0, 0, 0.3) 0 2px 10px;
            border-radius: 0px;
            border: 2px solid #3ddb93;
            font-weight: 300;
            font-size: 12px;
            position: absolute;
            padding: 5px;
            pointer-events: none;
            opacity: 0.95;
            }
        </style>
        </HEAD>
        <BODY>
<div style="font-family: verdana; padding: 10px">
<span style="font-size: 15px;">Surf Heights<br></span>
<span align="center" style="font-size: 12px; color: #3ddb93;">
<p>Max Height: h@surf_max</p>
<p>Min Height: @surf_min</p>

</span>
</div>
"""


"""
<div style="font-family: verdana; width : 550px; position: fixed; left: 950px; top: 80px; border: 2px solid @color; background: #f5f5f5; padding: 10px">
 <span style="font-size: 15px;">Title</span>
<span style="font-size: 12px; color: #696;">@title</span>
</div>
"""


# hover.tooltips = [
#    ("Surf Max (ft)", "@surf_max"),
#    ("Surf Min (ft)", "@surf_min")]
hover.mode = 'mouse'

show(p1)
