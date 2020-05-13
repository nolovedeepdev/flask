from flask import Flask, render_template, url_for, redirect, json, request, Response
from app import app
from datetime import datetime
import os
import jinja2
import cv2
from flask import jsonify

# route from index's page
@app.route('/')
@app.route('/index', methods= ['POST', 'GET'])
def index():
    return render_template('index.html')

# route from bar's page
@app.route("/bar", methods= ['POST','GET'])
def bar():
    return render_template('gra-bar.html')

# route from pie's page
@app.route("/pie", methods= ['POST','GET'])
def pie():
    return render_template('gra-pie.html')

# route from scatter's page
@app.route("/scatter", methods= ['POST','GET'])
def scatter():
    return render_template('gra-scatterplot.html')

img = 'C:/Users/computador/Documents/flask/app/static/img/bar0.png'

def showImage(img):
    from matplotlib import pyplot as plt
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def main(): # função que percorre toda a imagem para encontrar os pixels
    obj_img = cv2.imread('img/bar0.png')
    altura, largura, cores = obj_img.shape

    for y in range(0, altura):
        for x in range(0, largura):
            print(obj_img[y][x])

# route from interaction's page
@app.route("/interact", methods= ['POST','GET'])   
def inte():
    return render_template('interact.html')


