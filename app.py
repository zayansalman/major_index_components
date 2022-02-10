import dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
from scoring.pe_ratio_scoring import Nasdaq100PERatioScoring

app = dash.Dash(__name__)
server = app.server

npe = Nasdaq100PERatioScoring()
sector_dict = npe.add_pe_ratio_scores_to_sectors_dict()


app.layout = html.Div([
    html.H1('Nasdaq100 Components P/E Ratio Z-Score to rating 1-10 by Sector'),
    html.Div(
        children=[
            html.Div(
                children=[
                html.Br(),
                html.H3('Select Sector'),
                dcc.Dropdown(id='sector_dd',
                options=[
                    {'label': 'Electronic Technology', 'value': 'Electronic Technology'},
                    {'label': 'Technology Services', 'value': 'Technology Services'},
                    {'label': 'Utilities', 'value': 'Utilities'},
                    {'label': 'Health Technology', 'value': 'Health Technology'},
                    {'label': 'Producer Manufacturing', 'value': 'Producer Manufacturing'},
                    {'label': 'Retail Trade', 'value': 'Retail Trade'},
                    {'label': 'Consumer Durables', 'value':'Consumer Durables'},
                    {'label': 'Consumer Services', 'value': 'Consumer Services'},
                    {'label': 'Commercial Services', 'value': 'Commercial Services'},
                    {'label': 'Transportation', 'value': 'Transportation'},
                    {'label': 'Distribution Services', 'value': 'Distribution Services'},
                    {'label': 'Consumer Non-Durables', 'value': 'Consumer Non-Durables'},
                    {'label': 'Communications', 'value': 'Communications'}, ],
                    style={'width': '200px', 'margin': '0 auto'})
                ],
                style={'width': '350px', 'height': '150px', 'display': 'inline-block', 'vertical-align': 'top',
                       'border': '1px solid black', 'padding': '20px'}),
            html.Div(children=[
                    # Add a graph component with identifier
                    dcc.Graph(id='sector'),
                    ],
                     style={'width':'1000px','display':'inline-block'}
                     ),
            ])],
          style={'text-align': 'center', 'display': 'inline-block', 'width': '100%'}
          )

@app.callback(
    Output(component_id='sector', component_property='figure'),
    Input(component_id='sector_dd', component_property='value')
)
def update_plot(input_sector):
    df = sector_dict[input_sector]
    return px.bar(df, x="P/E Rating", y="PRICE", color="TICKER")


if __name__ == '__main__':
    app.run_server(debug=True)
