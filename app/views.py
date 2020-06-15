from app import app
from flask import Flask, request, redirect, render_template, flash, url_for, session, send_from_directory, abort
from datetime import datetime

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