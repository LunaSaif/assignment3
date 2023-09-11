import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

data_url = "https://raw.githubusercontent.com/LunaSaif/assignment3/main/COVID-19%20Coronavirus.csv"
data = pd.read_csv(data_url)
    # Limit the data to the first 10 rows
data = data.head(10)
data2 = data[['Country','Death percentage']]
data2.head(10)

data3 = data[['Country','Continent','Total Cases','Total Deaths']]
data3 = data3.sort_values('Total Cases', ascending=False)
data3.head(10)

app.layout = html.Div([
    html.H1("Luna Assignment 3"),

    # bar chart
    dcc.Graph(
        id='total-cases-bar-chart',
        figure=px.bar(data3, x='Country', y='Total Cases', title='Total Cases by Country'),
    ),
    
    # second bar chart
    dcc.Graph(
        id='total-deaths-bar-chart',
        figure=px.bar(data3, x='Country', y='Total Deaths', title='Total Deaths by Country'),
    ),
    
    # Add the pie chart
    dcc.Graph(
        id='cases-pie-chart',
        figure=px.pie(data3, values='Total Cases', names='Continent', title='Cases of Covid-19 by Continent'),
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
