import pandas as pd
import poloniex as poloniex
import datetime
import numpy as np
import webbrowser
import os
import bokeh
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file


def polo_tick(ticker2):
    if '_' in ticker2:
        ticker_temp = ticker2
    else:
        ticker_temp = 'USDT_' + ticker2

    return str.upper(ticker_temp)


def ppdf(df):
    '''
    Print df to webbrowser
    '''

    import webbrowser
    import os

    css_style = '''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            font-family: arial;
            font-size: 13px;
        }
        th, td {
            padding: 5px;
            text-align: left;
        }
        table#t01 {
            width: 100%;    
            background-color: #f1f1c1;
        }
        th {
            background-color: #254D68;
            color: white;
        }
        </style>
        </head>
    '''

    with open('/Users/johncaperton/Projects/sandbox/temp_html.html', 'w') as temp_file:
        temp_file.write(css_style + df.to_html())
        html_path = 'file://' + temp_file.name
        webbrowser.get('chrome').open_new(html_path)


holdings_static = {'btc': 1.81411,
                   'bch': 1.82789,
                   'eth': 23.6612,
                   'xrp': 14732,
                   'str': 4059}


def cc_holdings(ticks):
    '''
    List all holdings
    '''

    # Add something to remove ticker from the thing
    if '_' in ticks:
        ticks = ticks[ticks.find('_') + 1:]

    holdings = {'btc': 1.81411,
                'bch': 1.82789,
                'eth': 23.6612,
                'xrp': 14732,
                'str': 4059}

    return float(holdings[str.lower(ticks)])


def cc_snapshot(ticker, call_time=None):
    '''
    Return current snapshot of specified crypto handle to USD
    '''

    import pandas as pd
    import time

    # Create connection to poloniex api if one doesn't exist
    try:
        polo
    except NameError:
        import poloniex
        polo = poloniex.Poloniex('5I7ELFOI-CL9RLWHL-M6Y1WTBH-BW37S4OO',
                                 'cef5ce2ce783f33f9d9bb881044080f9297c685fee8b893cf317cb71338c80a30af0d469c37597a8d4115365b652172a2ce99c84a938c826291617c510075d1d')
    if call_time is None:
        call_time = pd.to_datetime(datetime.datetime.now())

    quant = cc_holdings(ticker)
    polo_tick_ret = polo_tick(ticker)

    polo_out = polo.returnTicker()[polo_tick_ret]

    #polo_out_trim = list({polo_out[x] for x in ('last', 'low24hr', 'high24hr', 'baseVolume')})

    cc_snap = {'ticker': ticker,
               'polo_ticker': polo_tick_ret,
               'call_date_time': call_time,
               'quantity': quant,
               'last': polo_out['last'],
               'low24hr': polo_out['low24hr'],
               'high24hr': polo_out['high24hr'],
               'baseVolume': polo_out['baseVolume']}

    return pd.DataFrame(cc_snap, index=[0])


def pull_portfolio():
    '''
    Pull current portfolio values
    '''

    r = 0
    call_t = pd.to_datetime(datetime.datetime.now())

    for x in holdings_static:

        if r == 0:
            temp_df = cc_snapshot(x, call_t)
        else:
            temp_df = pd.concat([temp_df, cc_snapshot(x, call_t)])
        r += 1

    temp_df['total'] = temp_df['last'] * temp_df['quantity']
    temp_df.loc['OVERALL'] = pd.Series(temp_df['total'].sum(), index=['total'])

    ppdf(temp_df)


def cc_historical(ticker, start_time=None, end_time=None, period=300, chart=False):
    '''
    Return current snapshot of specified crypto handle to USD
    '''

    import pandas as pd
    import time

    # Create connection to poloniex api if one doesn't exist
    try:
        polo
    except NameError:
        import poloniex
        polo = poloniex.Poloniex('5I7ELFOI-CL9RLWHL-M6Y1WTBH-BW37S4OO',
                                 'cef5ce2ce783f33f9d9bb881044080f9297c685fee8b893cf317cb71338c80a30af0d469c37597a8d4115365b652172a2ce99c84a938c826291617c510075d1d')
    if end_time is None:

        end_time = pd.to_datetime(datetime.datetime.now())
    if start_time is None:
        start_time = end_time - datetime.timedelta(days=1)

    polo_tick = 'USDT_' + str.upper(ticker)

    temp_df = polo.returnChartData(polo_tick, start=start_time, end=end_time, period=300)
    temp_df = pd.DataFrame(temp_df)
    temp_df['ticker'] = str.upper(ticker)

    if chart == True:
        cc_chart(temp_df, str(ticker))

    return temp_df


def cc_chart(df, ticker):

    from bokeh.layouts import gridplot
    from bokeh.plotting import figure, show, output_file

    p1 = figure(x_axis_type="datetime", title="Prices")
    p1.grid.grid_line_alpha = 0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'

    p1.line(df['date'], df['close'], color='#A6CEE3', legend=str.upper(ticker))

    show(gridplot([[p1]], plot_width=1000, plot_height=700))  # open a browser


# Bollinger Bands
def BBANDS(df, n):
    #MA = pd.Series(pd.rolling_mean(df['close'], n))
    #MSD = pd.Series(pd.rolling_std(df['close'], n))
    MA = df['close'].rolling(window=30, center=False).mean()
    MSD = df['close'].rolling(window=30, center=False).std()
    b1 = 4 * MSD / MA
    B1 = pd.Series(b1, name='BollingerB_' + str(n))
    df = df.join(B1)
    b2 = (df['close'] - MA + 2 * MSD) / (4 * MSD)
    B2 = pd.Series(b2, name='Bollinger%b_' + str(n))
    df = df.join(B2)
    return df


df1 = cc_historical('xrp')
df2 = cc_historical('str')

df1['pct_change'] = df1.close.pct_change()
df1['log_return'] = np.log(df1.close) - np.log(df1.close.shift(1))

df2['pct_change'] = df2.close.pct_change()
df2['log_return'] = np.log(df2.close) - np.log(df2.close.shift(1))

p1 = figure(x_axis_type='datetime', title='Prices')
p2 = figure(x_axis_type='datetime', title='Prices2')
p1.grid.grid_line_alpha = .3
p1.yaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Price'

# the number of columns is the number of lines that we will make
numlines = len(df.columns)

# import color pallet
mypalette = Spectral11[0:2]

# remove unwanted columns
col_list = ['Column A', 'Column B']
df = df[col_list]


p1.line(df1['date'], df1['close'], color='#A6CEE3', legend=df1['ticker'][0])
p2.line(df2['date'], df2['close'], color='#A6CEE3', legend=df2['ticker'][0])

show(gridplot([[p1, p2]], plot_width=1000, plot_height=700))
#r = BBANDS(t, n=30)


colors_list = ['blue', 'red']
legends_list = ['first', 'second']
xs = [df1['date'], df2['date']]
ys = [df1['log_return'], df2['log_return']]

p = figure(plot_width=800, plot_height=500)

for (colr, leg, x, y) in zip(colors_list, legends_list, xs, ys):
    my_plot = p.line(x, y, color=colr, legend=leg)

show(p)
