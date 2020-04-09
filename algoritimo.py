from sklearn.cluster import KMeans
import cv2
import numpy as np
from pytesseract import Output
import pytesseract as ocr
import pandas as pd
import math
from matplotlib import pyplot as plt
from operator import itemgetter
import json
from os import listdir
from os.path import isfile
from os.path import join
import sys
import firevent
import json

def extract(sourceimg):
    
    imgFiltered, imgResized = filterImage(sourceimg)  # Filter IMG for OCR and Resize it for the rest
    imgFiltered = imgResized
    maskList = findBarMasks(sourceimg.copy())  # Find the masks of the bars
    maskContours = findMasksContours(maskList, sourceimg)  # Find the bar contours of the bars


    if (DEBUG):  # Draw the contours to see if everything is alright
        barsimg = sourceimg.copy()
        cv2.drawContours(barsimg, maskContours, -1, (0, 255, 0), 1)
        cv2.imshow("Contornos", barsimg)
        cv2.waitKey(0)

    orientation = inferOrientation(maskContours)  # Infer orientation, True if vertical, False if horizontal


    xAxis = getXAxis(maskContours, orientation, sourceimg.copy())  # Find the X Axis
    #printAXIS(xAxis, imgResized.copy())
    #scale, dict = runOCR(imgFiltered, xAxis)  #  Run OCR and return the scale
    #print("Scale", scale)

    barras = calulateBars(maskContours) #  Store the bars as a list of x, y, w, h. Example: The x of the first bar is in barras[0][0]
    sortedBarras = sorted(barras, key=itemgetter(0)) #  Left to right order
    barrasComZeros = calulateZeros(sortedBarras, xAxis, sourceimg.copy()) #  Added the zeros in the middle
    sortedBarras = sorted(barrasComZeros, key=itemgetter(0))  #  Left to right order with the zeros included

    if (DEBUG):
        print("NOVAS BARRAS", sortedBarras)

    #datavalues = calculateDataValues(sortedBarras, scale, dict['p'])
    #print("OCR STATUS:", dict['p'])
    imageForOCR = getScaleSegment(sourceimg.copy(), sortedBarras)
    scale, dict, ponto = runOCR(imageForOCR, sourceimg, xAxis)


    datavalues = calculateDataValues(sortedBarras, scale, dict['p'])



    if (DEBUG):
        print("ESCALA", scale)
        printvalues(sortedBarras, scale, sourceimg.copy())
    #print("DATAVALUES: ", datavalues)

    for g in range(len(sortedBarras)):  #Fix Scale, this will have to be adjusted to the scaling factor once the OCR is implemented correctly
        sortedBarras[g] = tuple(ti//1 for ti in sortedBarras[g])

    getTitles(sourceimg.copy(), sortedBarras)

    return {'Barras': sortedBarras, 'xAxis': xAxis//1, 'OCRStatus': dict['p'], 'ponto': ponto, 'ValorBarras': datavalues}