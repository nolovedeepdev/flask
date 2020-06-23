from flask import Flask, render_template, url_for, redirect, json, request, Response, jsonify
from app import app
import cv2
from datetime import datetime
import os
import jinja2


# route from index's page
@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


# route from interaction's page
@app.route("/interact/", methods=['POST', 'GET'])
def inte():
    return render_template('interact.html')


def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')


@app.route("/interact/axis", methods=['POST', 'GET'])
def mouseClick():
    outputFrame = None
    img = cv2.imread(r'app/static/img/bar0.png')  # Carregar a imagem do terminal p/ o opencv
    clicked = False  # Declarar a variável global
    xpos = ypos = 0  # xpos = posição x, ypos = posição y
    axislist = []  # List to take the axis positions

    def generate(img):
        # grab global references to the output frame and lock variables
        global outputFrame, lock

        # loop over frames from the output stream
        while True:
            # wait until the lock is acquired
            with lock:
                # check if the output frame is available, otherwise skip
                # the iteration of the loop
                if outputFrame is None:
                    continue

                # encode the frame in JPEG format
                (flag, encodedImage) = cv2.imshow("image", img)

                # ensure the frame was successfully encoded
                if not flag:
                    continue

            # yield the output frame in the byte format
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                   bytearray(encodedImage) + b'\r\n')


    def takeAxis(event, x, y, flags, param):  # Função para pegar as cordenadas x e y com o mouse
        if event == cv2.EVENT_LBUTTONDBLCLK:
            global xpos, ypos, clicked
            clicked = True
            axislist.append(y)
            axislist.append(x)

    cv2.namedWindow("image")
    cv2.setMouseCallback('image', takeAxis)  # Comando que permite a comunicação/ recebimento dos clicks

    while 1:  # Laço que permite um proximo click para resgatar o eixo
        generate()

        if clicked:  # Condicional para captura o eixo em uma lista
            clicked = False

        if cv2.waitKey(20) & 0xFF == 27:  # Condicional para parar o laço ao teclar Esc
            break

    return 'cuh', axislist


@app.route("/image_output", methods=['POST', 'GET'])
def image_output():
    return Response(mouseClick())
