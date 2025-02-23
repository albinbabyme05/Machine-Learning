from flask import Flask, jsonify, request, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app = application

ridge_model = pickle.load(open(r'./model/ridge.pkl', 'rb'))
std_scalar = pickle.load(open(r'./model/scalar.pkl', 'rb'))



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/preidctdata', methods=['GET', 'POST'])
def predict():
    if request== 'POST':
        pass
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
