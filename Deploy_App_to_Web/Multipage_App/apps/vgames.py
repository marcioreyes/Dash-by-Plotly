import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

dfv = pd.read_csv(DATA_PATH.joinpath("alarmes.csv"))  # GregorySmith Kaggle
lista_col = ["ID", "Alarme", "Tipo", "Descrição", "Data", "Horário", "Atendente", "Horário Atendimento"]


layout = html.Div([
    html.H1('SAMA - Alarmes', style={"textAlign": "center"}),

    html.Div([
        html.Div(dcc.Dropdown(
            id='genre-dropdown', value='Strategy', clearable=False,
            options=[{'label': x, 'value': x} for x in sorted(dfv.Genre.unique())]
        ), className='six columns'),

        html.Div(dcc.Dropdown(
            id='sales-dropdown', value='EU Sales', clearable=False,
            persistence=True, persistence_type='memory',
            options=[{'label': x, 'value': x} for x in lista_col]
        ), className='six columns'),
    ], className='row'),

    dcc.Graph(id='my-bar', figure={}),
])


@app.callback(
    Output(component_id='my-bar', component_property='figure'),
    [Input(component_id='genre-dropdown', component_property='value'),
     Input(component_id='sales-dropdown', component_property='value')]
)
def display_value(genre_chosen, sales_chosen):
    dfv_fltrd = dfv[dfv['Genre'] == genre_chosen]
    dfv_fltrd = dfv_fltrd.nlargest(10, sales_chosen)
    fig = px.bar(dfv_fltrd, x='Video Game', y=sales_chosen, color='Platform')
    fig = fig.update_yaxes(tickprefix="$", ticksuffix="M")
    return fig
