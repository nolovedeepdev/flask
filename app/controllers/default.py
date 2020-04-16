from flask import Flask, render_template, url_for, redirect, json, request

from app import app

from datetime import datetime

import os

import jinja2

@app.route('/')
@app.route('/index',methods= ['POST', 'GET'])
def index():
    return render_template('index.html')

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

@app.route("/upload",methods= ['POST','GET'])
def upload():
    if request.files:
        image = request.files["image"]
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
        print("image saved")
        return redirect(request.url)
    return render_template('upload.html')
