from flask import Flask, render_template, url_for, redirect
from app import app

@app.route("/index",methods= ['POST','GET'])
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/api',methods= ['POST','GET'])
def process():
    try:
        return render_template('api.html')
    except expression as identifier:
        return jsonify({'error' : 'Missing data!'})

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
    return render_template('about.html')

@app.route("/refe",methods= ['POST','GET'])
def refe():
    return render_template("/refe.html")
