from flask import Flask, render_template, url_for, redirect, json, request
from app import app

@app.route('/')
@app.route('/index',methods= ['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route("/api",methods= ['POST','GET'])
def api():
    return render_template('api.html')

@app.route("/bar",methods= ['POST','GET'])
def bar():
    return render_template('gra-bar.html')

@app.route("/pie",methods= ['POST','GET'])
def pie():
    return render_template('gra-pie.html')

@app.route("/scatter",methods= ['POST','GET'])
def scatter():
    return render_template('gra-scatterplot.html')

@app.route("/about",methods= ['POST','GET'])
def about():
    return render_template('about.php')

@app.route("/refe",methods= ['POST','GET'])
def refe():
    return render_template("/refe.html")

