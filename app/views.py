from app import app
from flask import Flask, request, redirect, render_template, flash, url_for, session, send_from_directory, abort
from datetime import datetime
import sys
sys.path.append('app/code')
from plot import plot

@app.route("/")
@app.route("/index")
def index():
    return render_template("public/index.html")

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