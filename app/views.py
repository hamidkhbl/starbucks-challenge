from app import app
from flask import Flask, request, redirect, render_template, flash, url_for, session, send_from_directory, abort
from datetime import datetime
import sys
sys.path.append('app/code')
from plot import plot
sys.path.append('model')
from filter_offer import user_offers_history, load_data, user_history_analyzer

@app.route("/")
@app.route("/index", methods = ["GET", "POST"])
def index():
    df1_html = ""
    df1=""
    if request.method == "POST":
        req = request.form
        user_id = req.get("user_id")
        df1 = user_offers_history(int(user_id), load_data())
        new_offer = user_history_analyzer(df1)
        df1_html = df1.to_html(classes="table table-hover table-striped table-sm table-bordered")
    return render_template("public/index.html",  df1 = df1_html, count = len(df1), new_offer = new_offer)


@app.route("/dashboard")
def dashboard():
    return render_template("public/dashboard.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/plots")
def plots():
    ids, graphJSON = plot()
    return render_template("public/plots.html", ids=ids, graphJSON=graphJSON)