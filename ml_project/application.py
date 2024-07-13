import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

## import ridge regressor and standard scaler pickle files
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0")
