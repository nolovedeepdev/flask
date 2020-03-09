from flask import Flask, render_template, url_for, redirect
from app import app

@app.route("/index")
@app.route("/")

def index():
    return render_template('index.html')

@app.route("/index/bar")
def bar():
    return render_template('gra-bar.html')

@app.route("/pie")
def pie():
    return render_template('gra-pie.html')

@app.route("/scatter")
def scatter():
    return render_template('gra-scatterplot.html')
