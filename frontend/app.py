import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from backend.nasdaq_100 import Nasdaq100

app = dash.Dash(__name__)
nasdaq100 = Nasdaq100()
sector_list = nasdaq100.get_sector_list(Nasdaq100.load_nasdaq_100_data())
nasdaq100_sectors_dict = nasdaq100.get_nasdaq_100_sectors_dict()
electronic_technology_df = nasdaq100_sectors_dict.get(sector_list[0])

fig = px.bar(electronic_technology_df, x="P/E", y="PRICE", color="TICKER", barmode="group")

app.layout = html.Div(children=
                      [html.H1(children='Electronic Technology'),
                       html.Div(children='''Companies in the Electronic Technology sector of the Nasdaq 100.'''),
                       dcc.Graph(id='electronic-technology', figure=fig)])

if __name__ == '__main__':
    app.run_server(debug=True)



