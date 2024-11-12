import dash
from dash import dcc, html

# Create a Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("My First Dashboard"),
    dcc.Graph(
        id='graph-example',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [10, 11, 12], 'type': 'line', 'name': 'Example Line'},
            ],
            'layout': {
                'title': 'First Graph'
            }
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
