from flask import Flask 

##creating a flask app and naming it "app"
app = Flask('app')

@app.route('/test', methods=['GET'])
def test():
    return 'Pinging Model Application!!'

import pickle
from flask import Flask, request, jsonify
from ml_model import predict_GovRevnGDP

@app.route('/predict', methods=["POST","GET"])
def predict():
    if request.method == "POST":
        let requestData = JSON.parse(pm.request.body.raw)
        return jsonify(requestData)
