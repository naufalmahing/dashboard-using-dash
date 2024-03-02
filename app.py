from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    dash.page_container,
])

# Define the layout of page 2
page_2_layout = html.Div([
    html.H1('Page 2 Content'),
    dcc.Link('Go back to Home', href='/')
])

# # Callback to display page 2 layout when URL changes to '/page-2'
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     # content will be rendered in this element
#     if pathname == '/':
#         return html.Div(
#         id='page-content',
#         children=[
#             dcc.Link('Navigate to "/"', href='/'),
#             html.Br(),
#             dcc.Link('Navigate to "/page-2"', href='/page-2'),
#             ]
#         )
#     return html.Div([
#         html.H3(f'You are on page {pathname}')
#     ])

if __name__ == '__main__':
    app.run(debug=True)
