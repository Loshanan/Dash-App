### Import packages ###
import dash
from dash import dcc 
from dash import html
from dash.dependencies import Input, Output

### Import Dash Instance and pages ###
from app import app
from pages import page1, page2

### page container ###
page_container = html.Div(
    children=[
        # represents the URL bar, doesn't render anything
        dcc.Location(id='url', refresh=False),

        # content will be rendered in this element
        html.Div(id='page-content')
    ]
)

### Set app layout and page container ###
app.layout = page_container

app.validation_layout = html.Div(
    children=[
        page_container,
        #Index_layout,
        page1.layout,
        page2.layout
    ]
)

### update page conteainer ###
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def displaypage(pathname):
    # if pathname == '/':
    #     return Index_layout
    if pathname == '/page-1':
        return page1.layout
    elif pathname == '/page-2':
        return page2.layout
    else:
        return '404'
