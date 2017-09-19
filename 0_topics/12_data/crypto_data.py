import poloniex
import json
import pygal
import bokeh
from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show
from numpy import pi

# Polo Calls

polo = poloniex.Poloniex('5I7ELFOI-CL9RLWHL-M6Y1WTBH-BW37S4OO', 'cef5ce2ce783f33f9d9bb881044080f9297c685fee8b893cf317cb71338c80a30af0d469c37597a8d4115365b652172a2ce99c84a938c826291617c510075d1d')

#------------------------------
#   Polo Daily % Change
#------------------------------

daily_tickers = polo.returnTicker()
tickers = dict(daily_tickers)

pair, pchange = [], []
for k in tickers:
    if k[:4] == 'USDT':
        pair.append(k)
        pchange.append(tickers[k]['percentChange'])

# Abbreviate ticker names
pair_abb = [t[t.find('_') + 1:] for t in pair]

# Create Chart
output_file("dailyticker.html")

p1 = figure(title='24hr Percent Change', x_range=pair_abb, plot_width=800, plot_height=400, y_range=(0, max(pchange) + max(pchange) * .1), tools='hover')
p1.vbar(x=pair_abb, top=pchange, width=.5, color="firebrick", alpha=.8)
p1.add_tools(HoverTool(show_arrow=False,
                       line_policy='nearest',
                       tooltips=None))
# Rotate Axis
p1.xaxis.major_label_orientation = pi / 4

show(p1)
