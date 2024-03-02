import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Welcome to Project HMI'),

    html.Div(
        className='container',
        children=[
            html.Div(
                className='row',
                children=[
                    dcc.Link(
                        href='/realtime',className='six columns',
                        children=[
                                html.Div(
                                    children=[
                                        html.H1('Realtime', style={'text-align': 'center'}),
                                    ]
                                )
                        ],
                        style={'border': '1px solid #ccc', 'height': '200px'}
                    ),
                    dcc.Link(
                        href='/dashboard',className='six columns',
                        children=[
                                html.Div(
                                    children=[
                                        html.H1('Dashboard', style={'text-align': 'center'}),
                                    ]
                                )
                        ],
                        style={'border': '1px solid #ccc', 'height': '200px'}
                    ),
                ],
            ),
            html.Div(
                className='row',
                children=[
                    dcc.Link(
                        href='/diagram',className='six columns',
                        children=[
                                html.Div(
                                    children=[
                                        html.H1('HV Network Diagram', style={'text-align': 'center'}),
                                    ]
                                )
                        ],
                        style={'border': '1px solid #ccc', 'height': '200px'}
                    ),
                    dcc.Link(
                        href='/configuration',className='six columns',
                        children=[
                                html.Div(
                                    children=[
                                        html.H1('Software & Unit Configuration', style={'text-align': 'center'}),
                                    ]
                                )
                        ],
                        style={'border': '1px solid #ccc', 'height': '200px'}
                    ),
                ],
            ),
        ]
    ),
])