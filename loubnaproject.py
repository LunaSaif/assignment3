import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

data_url = "https://raw.githubusercontent.com/LunaSaif/assignment3/main/COVID-19%20Coronavirus.csv"
data = pd.read_csv(data_url)
data = data.head(10)
data2 = data[["Country", "Death percentage"]]
data3 = data[["Country", "Continent", "Total Cases", "Total Deaths"]]
data3 = data3.sort_values("Total Cases", ascending=False)

# Create a list of all available continents for the checklist
available_continents = data3["Continent"].unique()

# Define the app layout with tabs and a horizontal checklist for "Total Cases and Deaths" tab
app.layout = html.Div(
    [
        html.H1("Luna Assignment 3"),
        dcc.Tabs(
            id="tabs",
            value="tab-total-cases",
            children=[
                dcc.Tab(label="Total Cases and Deaths", value="tab-total-cases"),
                dcc.Tab(label="Cases by Continent", value="tab-cases-by-continent"),
            ],
        ),
        html.Div(id="tab-content"),
    ]
)


# Define callback to update tab content and filter data based on the checklist
@app.callback(Output("tab-content", "children"), Input("tabs", "value"))
def render_content(tab):
    if tab == "tab-total-cases":
        return html.Div(
            [
                dcc.Dropdown(
                    id="total-cases-death-dropdown",
                    options=[
                        {"label": "Total Cases", "value": "Total Cases"},
                        {"label": "Total Deaths", "value": "Total Deaths"},
                    ],
                    value="Total Cases",  # Default value
                    clearable=False,  # Prevent the user from clearing the selection
                ),
                dcc.Graph(id="total-cases-death-bar-chart"),
            ]
        )
    elif tab == "tab-cases-by-continent":
        return html.Div(
            [
                html.Label("Select Continents:", style={"font-weight": "bold"}),
                dcc.Checklist(
                    id="continent-checklist",
                    options=[
                        {"label": continent, "value": continent}
                        for continent in available_continents
                    ],
                    value=[
                        "Continent 1"
                    ],  # Default selected continents, change as needed
                    inline=True,  # Display options inline horizontally
                ),
                dcc.Graph(id="cases-pie-chart"),
            ]
        )


# Define callback to update the bar chart based on the selected option (Total Cases or Total Deaths)
@app.callback(
    Output("total-cases-death-bar-chart", "figure"),
    Input("total-cases-death-dropdown", "value"),
)
def update_bar_chart(selected_option):
    if selected_option == "Total Cases":
        fig = px.bar(
            data3, x="Country", y="Total Cases", title="Total Cases by Country"
        )
    elif selected_option == "Total Deaths":
        fig = px.bar(
            data3, x="Country", y="Total Deaths", title="Total Deaths by Country"
        )
    return fig


# Define callback to update the pie chart based on the selected continents
@app.callback(
    Output("cases-pie-chart", "figure"), Input("continent-checklist", "value")
)
def update_pie_chart(selected_continents):
    filtered_data3 = data3[data3["Continent"].isin(selected_continents)]
    fig = px.pie(
        filtered_data3,
        values="Total Cases",
        names="Continent",
        title="Cases of Covid-19 by Continent",
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
