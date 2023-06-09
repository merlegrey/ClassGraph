import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px
import plotly.io as pio

# Constants
TITLE = "THIS NEEDS A TITLE"
INTERVAL = 30000
DATA_FILEPATH = "data.csv"

# setup the theme
pio.templates.default = "gridon"

# Dash application instance
app = dash.Dash(__name__)




# Callback function that creates the dataset.
@app.callback(
    Output("bar-graph", "figure"),
    Input("interval", "n_intervals")
)
def create_figure(n):
    reading_data = pd.read_csv(DATA_FILEPATH)

    # sort by highest first.
    reading_data.sort_values("Books", inplace=True)

    fig =  px.bar(
        reading_data, 
        x="Books", 
        y="Student", 
        orientation='h',
        title=TITLE,
    )
    # fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(visible=False)

    return fig



# Entry point to instanciate and run the server.
def main():
    # setup the layout.
    app.layout = html.Div(
        [
            dcc.Graph(
                id="bar-graph", 
                figure=create_figure(0),
                style={"maxHeight": "400px", "maxWidth":"700px",  "overflow": "scroll"},
                config=dict(
                    displayModeBar=False
                )
            ),
            dcc.Interval(id="interval", interval=INTERVAL)
        ]
    )

    app.run_server(debug=False, host='0.0.0.0')



# run main
if __name__ == "__main__":
    main()