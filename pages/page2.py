### Import packages ###
import dash
from dash import dcc 
from dash import html
from dash.dependencies import Input, Output

### Import Dash Instance ###
from app import app

### Page 2 layout and callback ###
layout = html.Div(
    children = [
        dcc.Link(children='Go to page 1', href='/page-1'),
        html.H1("page 2"),
        dcc.RadioItems(
            id='page-2-radios',
            options=[{'label':i, 'value':i} for i in ['Orange', 'Red', 'Blue']],
            value='Orange'
        ),
        html.Div(id='page-2-content'),
        html.Br()
    ]
)

@app.callback(
    Output('page-2-content', 'children'),
    [Input('page-2-radios', 'value')]
)
def page_2_radios(value):
    return f'You have selected {value}.'