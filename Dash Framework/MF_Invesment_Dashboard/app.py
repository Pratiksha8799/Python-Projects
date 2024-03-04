# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:43:02 2023

@author: pr@t!ksha

"""

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load data from the mutual_funds.xlsx file
df = pd.read_excel('mutual_funds.xlsx')

# Initialize Dash app
app = dash.Dash(__name__)

# Get unique investment options from the 'InvestmentType' column
investment_options = df['FUNDNAME'].unique()

# App layout
app.layout = html.Div(children=[
    html.H1("Investment Analysis Dashboard",style={'textAlign': 'center'}),

    # Dropdown for selecting investment option
    html.Label("Select Investment Option:",style={'margin': '10px'}),
    dcc.Dropdown(
        id='investment-dropdown',
        options=[{'label': option, 'value': option} for option in investment_options],
        value=investment_options[0],  # Set default value
        style={'width': '50%', 'margin': '10px', 'color': 'black'},
    ),

    # Bar chart for identifying popular investments
    # dcc.Graph(id='popular-investments-chart'),
    # Scatter plot for displaying INVESTMENTACCOUNTID against INVESTMENTAMOUNT
    dcc.Graph(id='scatter-plot'),

    # Line chart for top-performing mutual funds
    dcc.Graph(id='top-performing-funds-chart'),

    # Pie chart for identifying high-net-worth investors
    dcc.Graph(id='high-net-worth-investors-chart'),

    # Line chart for historical returns of mutual funds
    dcc.Graph(id='historical-returns-chart'),

    # Bar chart for tax assessment
    dcc.Graph(id='tax-assessment-chart'),

], style={'backgroundColor': 'black', 'color': 'white'},)

# Callback to update charts based on dropdown selection
@app.callback(
    [Output('scatter-plot', 'figure'),
     #Output('popular-investments-chart', 'figure'),
     Output('top-performing-funds-chart', 'figure'),
     Output('high-net-worth-investors-chart', 'figure'),
     Output('historical-returns-chart', 'figure'),
     Output('tax-assessment-chart', 'figure')],
    [Input('investment-dropdown', 'value')]
)
def update_charts(selected_investment):
    # Filter data based on the selected investment option
    filtered_df = df[df['FUNDNAME'] == selected_investment]
    # Calculate historical returns
    filtered_df['HistoricalReturns'] = (filtered_df['NAV'].pct_change() * 100).fillna(0)


    # Charts
    # Scatter plot
    scatter_plot = px.scatter(filtered_df, x='INVESTMENTACCOUNTID', y='INVESTMENTAMOUNT',
                              title=f'{selected_investment} - Investment Amount vs. Account ID',
                              labels={'INVESTMENTACCOUNTID': 'Investment Account ID', 'INVESTMENTAMOUNT': 'Investment Amount','FUNDTYPE': 'Fund Type'},
                              hover_data=['FUNDTYPE'])  # Add additional columns to show in hover data)
    scatter_plot.update_layout(plot_bgcolor='black', paper_bgcolor='black', font_color='white')
    
    # popular_investments_chart = px.bar(filtered_df, x='INVESTMENTACCOUNTID', y='INVESTMENTAMOUNT', title='Popular Investments')
    # top_performing_funds_chart = px.line(filtered_df, x='INVESTMENTDATE', y='INVESTMENTAMOUNT', title='Top-Performing Mutual Funds')
    top_performing_funds_chart = px.scatter(filtered_df, 
                                         x='INVESTMENTACCOUNTID', 
                                         y='INVESTMENTAMOUNT', 
                                         size='INVESTMENTAMOUNT',
                                         color='INVESTMENTAMOUNT',
                                         title='INVESTMENTAMOUNT by INVESTMENTACCOUNTID',
                                         labels={'INVESTMENTAMOUNT': 'Investment Amount', 'INVESTMENTACCOUNTID': 'Investment Account ID','FUNDTYPE': 'Fund Type'},
                                         hover_data=['FUNDTYPE'])  # Add additional columns to show in hover data)
    top_performing_funds_chart.update_layout(plot_bgcolor='black', paper_bgcolor='black', font_color='white')
    
    high_net_worth_investors_chart = px.pie(filtered_df, names='FUNDTYPE', title='High-Net-Worth Investors',
                                            labels={'NAV':'Net asset Value','FUNDTYPE': 'Fund Type','INVESTMENTAMOUNT': 'Investment Amount'},
                                            hover_data=['NAV','INVESTMENTAMOUNT'])  # Add additional columns to show in hover data))
    high_net_worth_investors_chart.update_layout(plot_bgcolor='black', paper_bgcolor='black', font_color='white')
    # historical_returns_chart = px.line(filtered_df, x='INVESTMENTDATE', y='INVESTMENTAMOUNT', title='Historical Returns of Mutual Funds')
    # Candlestick chart for historical returns
    historical_returns_chart = px.scatter(filtered_df, x='INVESTMENTDATE', y='HistoricalReturns', 
                                         title=f'Historical Returns of {selected_investment}',
                                         labels={'HistoricalReturns': 'Returns (%)', 'INVESTMENTDATE': 'Investment Date'}
                                         )  # Use a dark template for financial charts template='plotly_dark'
    historical_returns_chart.update_layout(plot_bgcolor='black', paper_bgcolor='black', font_color='white')
    
    # Filter data based on the selected mutual fund and Tax Saving fund type
    filtered_df1 = df[(df['FUNDNAME'] == selected_investment) & (df['FUNDTYPE'] == 'Tax-Saving')]

   # Bar chart for tax assessment in Tax Saving funds
    tax_assessment_chart = px.bar(filtered_df1, x='INVESTMENTACCOUNTID', y='INVESTMENTAMOUNT', 
                                             title=f'Tax Assessment for {selected_investment} - Tax Saving Funds',
                                             labels={'INVESTMENTAMOUNT': 'Invesment Amount (Tax-Saving)', 'INVESTMENTACCOUNTID': 'Investment Account ID'})

    tax_assessment_chart.update_layout(plot_bgcolor='black', paper_bgcolor='black', font_color='white')
    # tax_assessment_chart = px.bar(filtered_df, x='FUNDNAME', y='FUNDTYPE', title='Tax Assessment')

    return scatter_plot, top_performing_funds_chart, high_net_worth_investors_chart, historical_returns_chart, tax_assessment_chart

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
