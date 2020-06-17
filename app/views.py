from app import app
import pandas as pd
from flask import Flask, request, redirect, render_template, flash, url_for, session, send_from_directory, abort
from datetime import datetime
import sys
sys.path.append('app/code')
from plot import plot
sys.path.append('model')
from filter_offer import user_offers_history, load_data, user_history_analyzer, load_all_data
from sklearn.externals import joblib

@app.route("/")
@app.route("/index", methods = ["GET", "POST"])
def index():
    df1_html = ""
    df1=""
    new_offer=""
    if request.method == "POST":
        req = request.form
        user_id = req.get("user_id")
        df1 = user_offers_history(int(user_id), load_data())
        new_offer = user_history_analyzer(df1)
        df1_html = df1.to_html(classes="table table-hover table-striped table-sm table-bordered")
    return render_template("public/index.html",  df1 = df1_html, count = len(df1), new_offer = new_offer)


@app.route("/predict", methods = ["GET", "POST"])
def predict():
    message = ""
    if request.method == "POST":
        req = request.form
        age = req.get("age")
        income = req.get("income")
        gender = req.get("gender")

        model = joblib.load("model/model.pkl")
        query =  pd.DataFrame({'age': [int(age)], 'gender': [ 1 if gender == "Male" else 0], 'income': [int(income)]})
        #query =  [int(age), 1 if gender == "Male" else 0, int(income)]
        completed = model.predict(query)

        message = "{} users with the age of {} who has an income of around {} are most likely to {} offers.".format("Male" if gender == 1 else "Female", age, income, "complete" if completed == 1 else "not compelete")
    return render_template("public/predict.html", message = message)

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/plots")
def plots():
    ids, graphJSON = plot()
    return render_template("public/plots.html", ids=ids, graphJSON=graphJSON)

@app.route("/data_sample", methods = ["GET", "POST"])
def data_sample():
    df_profile, df_portfolio, df_transcript = load_all_data()
    return render_template("public/data_sample.html",
     df_profile = df_profile.sample(20).to_html(classes="table table-hover table-striped table-sm table-bordered"),
     df_portfolio = df_portfolio.to_html(classes="table table-hover table-striped table-sm table-bordered"),
      df_transcript = df_transcript.sample(20).to_html(classes="table table-hover table-striped table-sm table-bordered"))