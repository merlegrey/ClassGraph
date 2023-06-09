# Importing the libraries
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px

import datetime

# Creating the app
app = dash.Dash(__name__)

refresh_button = html.Button(
    "Refresh", 
    id="refresh_button", 
    style={"color": "white", "background-color": "blue"}
)

@app.callback(
    Output("bar-graph", "figure"), # The output is the children of the output div
    Input("refresh_button", "n_clicks") # The input is the n_clicks of the button
)
def update_figure(n):
    reading_data = pd.read_csv("data.csv")

    return px.bar(
        reading_data, 
        x="Books", 
        y="Student", 
        orientation='h',
    )

def main():
    fig = update_figure(0)

    # Creating the layout
    app.layout = html.Div([
        html.H1(
            "Book's R Kewl!", 
            style={"font-family": "Arial", "font-size": "36px"}
        ),
        dcc.Graph(id="bar-graph", figure=fig),
        refresh_button
    ])

    app.run_server(debug=True)

# Running the app
if __name__ == "__main__":
    main()