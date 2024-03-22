import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

ext_style = "https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/darkly/bootstrap.min.css"
app = dash.Dash(external_stylesheets=[ext_style])
server = app.server

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x = "Fruit", y = "Amount", color = "City", barmode = "group", template = "plotly_dark")

app.layout = html.Div(children=[
    html.H1(children = 'Hello Dash'),
    
    html.Div(children='''Dash: A web application framework for your data.'''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)