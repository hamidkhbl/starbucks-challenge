import json
import plotly
import pandas as pd
import numpy as np

from flask import Flask
from flask import render_template, request, jsonify
from flask import abort, redirect, url_for
from plotly.graph_objs import Scatter
from plotly.graph_objs import Figure
from plotly.graph_objs import Bar, histogram, histogram2d



app = Flask(__name__ , static_folder='app/static')

# load data
offer_details = pd.read_csv('..//data//offer_details.csv')
person_offer = pd.read_csv('..//data//person_offer.csv')



# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    return render_template('master.html')

@app.route('/plots')
def plots():
    
    # data for bar chart
    # event_offer_completed,event_offer_received,event_offer_viewed,event_transaction
    offers_count = []
    offers_status = ['Received Offers', 'Viewed Offers', 'Completed Offers']
    offers_count.append(person_offer.event_offer_received.sum())
    offers_count.append(person_offer.event_offer_viewed.sum())
    offers_count.append(person_offer.event_offer_completed.sum())

    #data for age histogram
    ages = offer_details[offer_details.age < 116].drop_duplicates(['person_id']).age

    # data for income histogram
    income = offer_details[offer_details.income.notna()].drop_duplicates(['person_id'])['income'].values

    # data for offer type (bogo, discount) offer status

    # create visuals
    graphs = [
                 {
            'data': [
                dict(
                    x=ages,
                    type='histogram'
                    
                )
            ],

            'layout': {
                'title': 'Age distribution of users',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Age"
                }
            }
        },
            {
            'data': [
                dict(
                    x=income,
                    type='histogram'
                    
                )
            ],

            'layout': {
                'title': 'Income distribution of users',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Income"
                }
            }
        },
        {
            'data': [
                Bar(
                    x=offers_status,
                    y=offers_count
                )
            ],

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

    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('plots.html', ids=ids, graphJSON=graphJSON)

# @app.route('/go')
# def go():
    # save user input in query
    # query = request.args.get('query', '') 

    # use model to predict classification for query
    # classification_labels = model.predict([query])[0]
    # classification_results = dict(zip(df.columns[3:], classification_labels))

    # This will render the go.html Please see that file. 
    # return render_template(
    #     'go.html',
    #     query=query,
    #     classification_result=classification_results
    # )




def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()