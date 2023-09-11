import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load the dataset
data_url = "https://github.com/LunaSaif/assignment3/blob/main/COVID-19%20Coronavirus.csv" 
data = pd.read_csv(data_url, encoding='ISO-8859-1')


# Define the app layout
app.layout = html.Div([
    html.H1("COVID-19 Data Visualization"),
    
    # Dropdown for selecting a country
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in data['Country,Other']],
        value='Afghanistan'  # Default selected country
    ),
    
    # Graph to display COVID-19 data
    dcc.Graph(id='covid-graph'),
])

# Define callback to update the graph based on the selected country
@app.callback(
    Output('covid-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_graph(selected_country):
    # Filter the dataset for the selected country
    filtered_data = data[data['Country,Other'] == selected_country]

    # Create a bar chart for Total Cases and Total Deaths
    fig = px.bar(
        filtered_data,
        x='Total Cases',
        y='Total Deaths',
        title=f"COVID-19 Statistics for {selected_country}",
        labels={'Total Cases': 'Total Cases', 'Total Deaths': 'Total Deaths'}
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
