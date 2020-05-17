import json
import plotly
import pandas as pd
import numpy as np
import json
from flask import Flask
from flask import render_template, request, jsonify
from flask import abort, redirect, url_for
from plotly.graph_objs import Scatter
from plotly.graph_objs import Figure
from plotly.graph_objs import Bar, histogram, histogram2d

def plot():
    graphs = []
    # load data
    offer_details = pd.read_csv('..//data//offer_details.csv')
    person_offer = pd.read_csv('..//data//person_offer.csv')


    # data for bar chart
    offers_count = []
    offers_status = ['Received Offers', 'Viewed Offers', 'Completed Offers']
    offers_count.append(person_offer.event_offer_received.sum())
    offers_count.append(person_offer.event_offer_viewed.sum())
    offers_count.append(person_offer.event_offer_completed.sum())

    offer_status_graph ={'data': [Bar(x=offers_status,y=offers_count)],
                         'layout': {
                            'title': 'Offer Status Bar chart',
                            'yaxis': {
                                'title': "Count"
                            },
                            'xaxis': {
                                'title': "Offer Status"
                            }
                        }
                     }
    graphs.append(offer_status_graph)

    #data for age histogram
    ages = offer_details[offer_details.age < 116].drop_duplicates(['person_id']).age
    age_graph = {'data': [dict(x=ages,type='histogram')],
                'layout': {
                    'title': 'Age distribution of users',
                    'yaxis': {
                        'title': "Count"
                    },
                    'xaxis': {
                        'title': "Age"
                    }
                }
                }
    graphs.append(age_graph)
    # data for income histogram
    income = offer_details[offer_details.income.notna()].drop_duplicates(['person_id'])['income'].values
    income_graph = {'data': [dict(x=income,type='histogram')],
                    'layout': {
                        'title': 'Income distribution of users',
                        'yaxis': {
                            'title': "Count"
                        },
                        'xaxis': {
                            'title': "Income"
                        }
                    }
                }
    graphs.append(income_graph)


    # data for offer type (bogo, discount) offer status

    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return ids, graphJSON