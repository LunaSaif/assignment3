import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

data_url = "https://raw.githubusercontent.com/LunaSaif/assignment3/main/COVID-19 Coronavirus.csv"
data = pd.read_csv(data_url)
    
    # Add the first bar chart
    dcc.Graph(
        id='total-cases-bar-chart',
        figure=px.bar(data, x='Country', y='Total Cases', title='Total Cases by Country'),
    ),
    
    # Add the second bar chart
    dcc.Graph(
        id='total-deaths-bar-chart',
        figure=px.bar(data, x='Country', y='Total Deaths', title='Total Deaths by Country'),
    ),
    
    # Add the pie chart
    dcc.Graph(
        id='cases-pie-chart',
        figure=px.pie(data, values='Total Cases', names='Continent', title='Cases of Covid-19 by Continent'),
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
