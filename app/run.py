import json
import plotly

from flask import Flask
from flask import render_template, request, jsonify
from flask import abort, redirect, url_for
import sys
sys.path.append("code")
from plot import plot



app = Flask(__name__ , static_folder='app/static')

# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    return render_template('master.html')

@app.route('/plots')
def plots():
    
    graphs = plot()
    
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