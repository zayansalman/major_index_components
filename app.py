import dash
from dash import dcc
from dash import html
import plotly.express as px
from scoring.pe_ratio_scoring import Nasdaq100PERatioScoring

app = dash.Dash(__name__)
server = app.server

npe = Nasdaq100PERatioScoring()
sector_dict = npe.add_pe_ratio_scores_to_sectors_dict()


electronic_technology_fig = px.bar(sector_dict['Electronic Technology'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
technology_services_fig = px.bar(sector_dict['Technology Services'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
utilities_fig = px.bar(sector_dict['Utilities'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
health_tech_fig = px.bar(sector_dict['Health Technology'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
producer_mfg_fig = px.bar(sector_dict['Producer Manufacturing'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
retail_trade_fig = px.bar(sector_dict['Retail Trade'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
consumer_durables_fig = px.bar(sector_dict['Consumer Durables'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
consumer_services_fig = px.bar(sector_dict['Consumer Services'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
commercial_services_fig = px.bar(sector_dict['Commercial Services'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
transportation_fig = px.bar(sector_dict['Transportation'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
distribution_services_fig = px.bar(sector_dict['Distribution Services'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
consumer_non_durables_fig = px.bar(sector_dict['Consumer Non-Durables'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")
communications_fig = px.bar(sector_dict['Communications'], x="P/E Rating", y="PRICE", color="NAME", barmode="group")

app.layout = html.Div(children=
                      [html.H1(children='Nasdaq100 Components Daily P/E Analyser'),
                       html.Div(children='''Rating stocks out of 10 based on their current PE ratios in their sector.
                       While many tech companies trade on future potential and projected growth and do not have earnings.
                       This tool is just for fun and to show you a comparison of current tech companies who have earnings and are a
                       part of the Nasdaq100 Index.
                       - Hover over bars to see name and price. 
                       - Click to select and unselect stocks to see in chart.
                       '''),
                       html.H1(children='Electronic Technology'),
                       dcc.Graph(id='electronic-technology', figure=electronic_technology_fig),
                       html.H1(children='Technology Services'),
                       dcc.Graph(id='technology-services', figure=technology_services_fig),
                       html.H1(children='Utilities'),
                       dcc.Graph(id='utilties', figure=utilities_fig),
                       html.H1(children='Health Technology'),
                       dcc.Graph(id='health-technology', figure=health_tech_fig),
                       html.H1(children='Producer Manufacturing'),
                       dcc.Graph(id='producer-manufacturing', figure=producer_mfg_fig),
                       html.H1(children='Retail Trade'),
                       dcc.Graph(id='retail-trade', figure=retail_trade_fig),
                       html.H1(children='Consumer Durables'),
                       dcc.Graph(id='consumer-durables', figure=consumer_durables_fig),
                       html.H1(children='Consumer Services'),
                       dcc.Graph(id='consumer-services', figure=consumer_services_fig),
                       html.H1(children='Commercial Services'),
                       dcc.Graph(id='commercial-services', figure=commercial_services_fig),
                       html.H1(children='Transportation'),
                       dcc.Graph(id='transportation', figure=transportation_fig),
                       html.H1(children='Distribution Services'),
                       dcc.Graph(id='distribution-services', figure=distribution_services_fig),
                       html.H1(children='Consumer Non-Durables'),
                       dcc.Graph(id='consumer-non-durables', figure=consumer_non_durables_fig),
                       html.H1(children='Communications'),
                       dcc.Graph(id='communications', figure=communications_fig)
                       ])

if __name__ == '__main__':
    app.run_server(debug=True)
