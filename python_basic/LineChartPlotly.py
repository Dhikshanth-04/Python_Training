from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

data = {
    "x": [1, 2, 3, 4, 5],
    "y": [10, 15, 13, 17, 20]
}

fig = px.line(data, x="x", y="y", title="Simple Dashboard Chart")

app.layout = html.Div([
    html.H1("My First Dash Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)