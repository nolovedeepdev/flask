from flask import Flask, render_template, request, Response, url_for, redirect
from app import app
import cv2


# Route from index's page
@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


# Route from interaction's page
@app.route("/interact/", methods=['POST', 'GET'])
def inter():
    return render_template('interact.html')

def main(): # função que percorre toda a imagem para encontrar os pixels
    obj_img = cv2.imread('img/bar0.png')
@app.route("/interact/axis", methods= ['POST','GET'])
def main(): # fuction that returns the axes
    obj_img = cv2.imread(r'app/static/img/bar0.png')
    altura, largura, cores = obj_img.shape

    for y in range(0, altura):
        for x in range(0, largura):
            print('x: {} y: {}'.format(x,y))
            x = str(x); y = str(y)
