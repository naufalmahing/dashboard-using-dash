import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State
import pandas as pd
from io import StringIO
import base64

dash.register_page(__name__, path='/diagram')

# Create dropdown options for selecting columns
dropdown_options = []

layout = html.Div([
    html.H1("HV Network Diagram"),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True,
        accept='.csv'
    ),
    html.H5('No Data Selected', id='data-info'),
    dcc.Dropdown(
        id='column-dropdown',
        options=dropdown_options,
        value=None
    ),
    dcc.Graph(id='line-chart'),
    dcc.Interval(
        id='interval-component',
        interval=1000,  # in milliseconds
        n_intervals=0
    ),

    html.Div(className='row', children=[
        dcc.Link(href='/', children=[
            html.Button('Back')
        ]), 
    ])
])

# Define callback to update dropdown options based on uploaded file
@callback(
    [Output('column-dropdown', 'options'),
     Output('data-info', 'children')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def update_dropdown_options(contents, filename):
    if contents is not None:
        content_type, content_string = contents[0].split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(StringIO(decoded.decode('utf-8')))
        dropdown_options = [{'label': col, 'value': col} for col in df.columns[1:]]
        return dropdown_options, filename
    else:
        return [], 'No Data Selected'

DATA_POINTS_TO_DISPLAY = 34

# Define callback to update the line chart based on dropdown selection and interval
@callback(
    Output('line-chart', 'figure'),
    [Input('column-dropdown', 'value'),
     Input('interval-component', 'n_intervals'),
     Input('upload-data', 'contents')]
)
def update_line_chart(selected_column, n_intervals, contents):
    if selected_column is None:
        return {
            'data': [],
            'layout': {
                'title': 'No Selected Column',
                'xaxis': {'title': 'Index'},
                'yaxis': {'title': 'Value'}
            }
        }
    else:
        # Fetch data from uploaded file
        content_type, content_string = contents[0].split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(StringIO(decoded.decode('utf-8')))

        # Calculate the total number of data points
        total_data_points = len(df[selected_column])

        # Calculate the start and end indices based on the current n_intervals
        start_index = (n_intervals * DATA_POINTS_TO_DISPLAY) % total_data_points
        end_index = (start_index + DATA_POINTS_TO_DISPLAY) % total_data_points

        # Select the data points within the index range
        if end_index > start_index:
            data = df[selected_column][start_index:end_index]
        else:
            data = pd.concat([df[selected_column][start_index:], df[selected_column][:end_index]])

        x = data.index
        y = data.values

        return {
            'data': [{
                'x': x,
                'y': y,
                'type': 'line',
                'name': selected_column
            }],
            'layout': {
                'title': f'Line Chart for {selected_column}',
                'xaxis': {'title': 'Index'},
                'yaxis': {'title': selected_column, 'range': [-3, 5]}  # Set y-axis range
            }
        }

