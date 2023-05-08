### Import packages ###
import dash
from dash import dcc 
from dash import html
from dash.dependencies import Input, Output

### Import Dash Instance ###
from app import app

### Page 1 layout and callback ###
layout = html.Div(
    children=[
        dcc.Link(children='Go to page 2', href='/page-2'),
        html.H1("page 1"),
        dcc.Dropdown(
            id='page-1-dropdown',
            options=[{'label':i, 'value':i} for i in ['Kothavari', 'Erumai', 'Kaluthai']],
            value='Kothavari',
        ),
        html.Div(id='page-1-content'),
        html.Br()
    ]
)


@app.callback(
    Output('page-1-content', 'children'),
    [Input('page-1-dropdown', 'value')]
)
def page_1_dropdown(value):
    return f"You have selected {value}."