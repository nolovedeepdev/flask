from flask import Flask, render_template, url_for, redirect, json, request, Response
from app import app
from datetime import datetime
import os
import jinja2
import cv2
from flask import jsonify

#route from index's page
@app.route('/')
@app.route('/index',methods= ['POST', 'GET'])
def index():
    return render_template('index.html')

#route from bar
@app.route("/bar",methods= ['POST','GET'])
def bar():
    return render_template('gra-bar.html')

#route from pie's page
@app.route("/pie",methods= ['POST','GET'])
def pie():
    return render_template('gra-pie.html')

#route from scatter's page
@app.route("/scatter",methods= ['POST','GET'])
def scatter():
    return render_template('gra-scatterplot.html')

# route from opencv to get coordinates of image on mouseclick
@app.route("/capture")
def capture_image(self):
    return jsonify({'image_url': r'app/static/img'})
    self.cam = cv2.VideoCapture(0)
    self.img = self.cam.read()
    self.cam.release()
    render_template(upload.html,ob=self.img)

# line what save images from client    
app.config["IMAGE_UPLOADS"] = r"app/static/img/uploads"

@app.route("/upload",methods= ['POST','GET'])
def upload():
    # upload images from client (future) 
    if request.files:
        image = request.files["image"]
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
        print("image saved")
        return redirect(request.url)
    return render_template('upload.html')
