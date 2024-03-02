import dash
from dash import dcc, html
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/configuration')

# Define dropdown options
options = [{'label': f'Field {i}', 'value': f'{i}'} for i in range(1, 6)]

# Define layout for a single parameter
def parameter_dropdown(param_id):
    return html.Div([
        html.Label(f'Parameter {param_id}'),
        dcc.Dropdown(
            id=f'param-{param_id}',
            options=options,
            value=options[0]['value']
        ),
        html.Br()
    ])

# Define layout for a single panel
def panel_layout(panel_id):
    return html.Div([
        html.H2(f'Channel {panel_id}'),
        *[parameter_dropdown(i) for i in range(1, 7)]
    ], style={'display': 'inline-block', 'width': '45%', 'margin': '10px'})

# Define the overall layout of the app with four panels
layout = html.Div([
    html.H1("Software & Unit Configuration"),
    html.Div([panel_layout(1), panel_layout(2)], style={'width': '100%', 'display': 'inline-block'}),
    html.Div([panel_layout(3), panel_layout(4)], style={'width': '100%', 'display': 'inline-block'}),

    html.Div(className='row', children=[
        dcc.Link(href='/', children=[
            html.Button('Back')
        ]), 
    ])
])

