from flask import Flask 

##creating a flask app and naming it "app"
app = Flask('app')

@app.route('/test', methods=['GET'])
def test():
    return 'Pinging Model Application!!'

import pickle
from flask import Flask, request, jsonify
from model_files.ml_model import predict_GovRevnGDP

@app.route('/predict', methods=["POST","GET"])
def predict():
    if request.method == "POST":
        return "POST!"
