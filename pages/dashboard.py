import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go
import requests

# Read the CSV file from the provided link
url = "../testfile1.csv"
df = pd.read_csv(url)

# Calculate the maximum value for each column (except the first one)
max_values = df.iloc[:, 1:].max()
min_values = df.iloc[:, 1:].min()

# Initialize the Dash app
dash.register_page(__name__, path='/dashboard')

# Define the layout of the app
layout = html.Div([
    html.H1("Dashboard"),
    html.Div([
        dcc.Graph(id='gauge-chart-1'),
        dcc.Graph(id='gauge-chart-3'),
    ], style={'display': 'inline-block'}),
    html.Div([
        dcc.Graph(id='gauge-chart-2'),
        dcc.Graph(id='gauge-chart-4')
    ], style={'display': 'inline-block'}),
    dcc.Interval(id='interval-component', n_intervals=1),
   
    html.Div(className='row', children=[
        html.Button(id='toggle-button', n_clicks=0, children='Max Values', style={'float': 'right'})
    ]),
    html.Div(className='row', children=[
        dcc.Link(href='/', children=[
            html.Button('Back')
        ]), 
    ])
])

# Callbacks to update the gauge charts
@callback(
    [Output('gauge-chart-1', 'figure'),
    Output('gauge-chart-2', 'figure'),
    Output('gauge-chart-3', 'figure'),
    Output('gauge-chart-4', 'figure'),
    Output('toggle-button', 'children')],
    [Input('toggle-button', 'n_clicks')],
)
def update_gauge_charts(n):
    values = max_values if n % 2 == 0 else min_values
    button_text = 'Max Values' if n % 2 == 0 else 'Min Values'

    # Create a gauge chart for each maximum value
    figures = []
    for i in range(4):
        val = values[i]
        figures.append(go.Figure(go.Indicator(
            mode='gauge+number',
            value=val,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': f"Value Channel {i+1}"},
            gauge={'axis': {'range': [-3, 5]}},
            
        )))

    return figures[0], figures[1], figures[2], figures[3], button_text

