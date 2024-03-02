import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import pandas as pd

# Read the CSV file from the provided link
url = "../testfile1.csv"
df = pd.read_csv(url)

# Number of data points to display at a time
DATA_POINTS_TO_DISPLAY = 34

dash.register_page(__name__, path='/realtime')

# Define layout of the app
layout = html.Div([
    html.H1("Realtime"),
    html.H2(id="data-name", children="Data 1"),
    html.Div([
        dcc.Graph(id='line-chart-2nd'),
        dcc.Graph(id='line-chart-4th'),
    ], style={'display': 'inline-block'}),
    html.Div([
        dcc.Graph(id='line-chart-3rd'),
        dcc.Graph(id='line-chart-5th'),
    ], style={'display': 'inline-block'}),
    dcc.Interval(
        id='interval-component',
        interval=1000,  # Update every 1 second
        n_intervals=0
    ),
    dcc.Interval(
        id='interval-data',
        interval=30*1000,
        n_intervals=1,
        max_intervals=-1
    ),

    html.Div(className='row', children=[
        dcc.Link(href='/', children=[
            html.Button('Back')
        ]), 
    ])
])

# Define callback to update line charts for specific columns
@callback(
    Output('line-chart-2nd', 'figure'),
    Output('line-chart-3rd', 'figure'),
    Output('line-chart-4th', 'figure'),
    Output('line-chart-5th', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_line_charts(n_intervals):
    total_data_points = 1000

    # Calculate the start and end indices based on the current n_intervals
    start_index = (n_intervals * DATA_POINTS_TO_DISPLAY) % total_data_points
    end_index = start_index + DATA_POINTS_TO_DISPLAY

    # Select the data points for each column within the index range


    if df.empty:
        index = [i for i in range(1000)][start_index:end_index]
        values = []
        traces_2nd = [{
            'x': index,
            'y': values,
            'type': 'line',
            'name': 'Empty'
        }]
        traces_3rd = [{
            'x': index,
            'y': values,
            'type': 'line',
            'name': 'Empty'
        }]
        traces_4th = [{
            'x': index,
            'y': values,
            'type': 'line',
            'name': 'Empty'
        }]
        traces_5th = [{
            'x': index,
            'y': values,
            'type': 'line',
            'name': 'Empty'
        }]

        return {
            'data': traces_2nd,
            'layout': {
                'title': 'Line Chart for Channel 1',
                'xaxis': {'title': 'Index'},
                'yaxis': {'title': 'Empty'}, 'range': [-3, 5]
            }
        }, {
            'data': traces_3rd,
            'layout': {
                'title': 'Line Chart for Channel 2',
                'xaxis': {'title': 'Index'},
                'yaxis': {'title': 'Empty'}, 'range': [-3, 5]
            }
        }, {
            'data': traces_4th,
            'layout': {
                'title': 'Line Chart for Channel 3',
                'xaxis': {'title': 'Index'},
                'yaxis': {'title': 'Empty'}, 'range': [-3, 5]
            }
        }, {
            'data': traces_5th,
            'layout': {
                'title': 'Line Chart for Channel 4',
                'xaxis': {'title': 'Index'},
                'yaxis': {'title': 'Empty'}, 'range': [-3, 5]
            }
        }, ['empty']
    
    data_2nd = df[df.columns[1]][start_index:end_index]
    data_3rd = df[df.columns[2]][start_index:end_index]
    data_4th = df[df.columns[3]][start_index:end_index]
    data_5th = df[df.columns[4]][start_index:end_index]

    traces_2nd = [{
        'x': data_2nd.index,
        'y': data_2nd.values,
        'type': 'line',
        'name': df.columns[1]
    }]
    traces_3rd = [{
        'x': data_3rd.index,
        'y': data_3rd.values,
        'type': 'line',
        'name': df.columns[2]
    }]
    traces_4th = [{
        'x': data_4th.index,
        'y': data_4th.values,
        'type': 'line',
        'name': df.columns[3]
    }]
    traces_5th = [{
        'x': data_5th.index,
        'y': data_5th.values,
        'type': 'line',
        'name': df.columns[4]
    }]

    return {
        'data': traces_2nd,
        'layout': {
            'title': 'Line Chart for Channel 1',
            'xaxis': {'title': 'Index'},
            'yaxis': {'title': df.columns[1], 'range': [-3, 5]}, 
            
        }
    }, {
        'data': traces_3rd,
        'layout': {
            'title': 'Line Chart for Channel 2',
            'xaxis': {'title': 'Index'},
            'yaxis': {'title': df.columns[2], 'range': [-3, 5]}, 
        }
    }, {
        'data': traces_4th,
        'layout': {
            'title': 'Line Chart for Channel 3',
            'xaxis': {'title': 'Index'},
            'yaxis': {'title': df.columns[3], 'range': [-3, 5]},
        }
    }, {
        'data': traces_5th,
        'layout': {
            'title': 'Line Chart for Channel 4',
            'xaxis': {'title': 'Index'},
            'yaxis': {'title': df.columns[4], 'range': [-3, 5]},
        }
    }, df.Channel1.tolist()


@callback(
    [Output('data-name', 'children')],
    [Input('interval-data', 'n_intervals')]
)
def update_data(n_intervals):
    global url
    global df
    l = url.split('/')
    l.pop()
    url = '/'.join(l) + '/testfile' + str(n_intervals) + '.csv'

    try:
        df = pd.read_csv(url)
    except:
        df = pd.DataFrame()
        return ['No data ' + url]
    return ['testfile ' + str(n_intervals)]