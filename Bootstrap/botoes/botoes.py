import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

button_group = dbc.ButtonGroup(
    [
        dbc.Button("Left", color="danger"),
        dbc.Button("Middle", color="warning"),
        dbc.Button("Right", color="success"),
    ]
)

app.layout = html.Div([
        
    dbc.ButtonGroup(
    [
        dbc.Button("Left", color="danger"),
        dbc.Button("Middle", color="warning"),
        dbc.Button("Right", color="success"),
    ]
    )    
        
    dbc.Button("Primary", color="primary", className="me-1"),
    dbc.Button("Secondary", color="secondary", className="me-1"),
    dbc.Button("Success", color="success", className="me-1"),
    dbc.Button("Warning", color="warning", className="me-1"),
    dbc.Button("Danger", color="danger", className="me-1"),
    dbc.Button("Info", color="info", className="me-1"),
    dbc.Button("Light", color="light", className="me-1"),
    dbc.Button("Dark", color="dark", className="me-1"),
    dbc.Button("Link", color="link")
    ]
    )


@app.callback(
    [Input('Primary', 'value'),
     Input('Secondary', 'value'),
     Input('Sucess', 'value'),
     Input('Warning', 'value'),
     Input('Danger', 'value'),
     Input('Sucess', 'value'),
     Input('Info', 'value'),
     Input('Light', 'value'),
     Input('Dark', 'value'),
     Input('Link', 'value')
     ]
)

def update_graph(dpdn_a, dpdn_b, dpdn_c):

    dash.layout.update()


if __name__ == "__main__":
    app.run_server(debug=True)


# https://youtu.be/vqVwpL4bGKY
