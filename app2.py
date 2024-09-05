from flask import Flask, render_template, Response,jsonify
import cv2
import mediapipe as mp 
import itertools
import copy
import numpy as np 
import string 
from tensorflow import keras
import pandas as pd 
import warnings
import time 
import pyttsx3
warnings.filterwarnings("ignore")
app = Flask(__name__)
cap = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
