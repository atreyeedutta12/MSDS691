from flask import Flask 

##creating a flask app and naming it "app"
app = Flask('app')

@app.route('/test', methods=["GET"])
def test():
    return 'Pinging Model Application!!'

import pickle
from flask import Flask, request, jsonify
from ml_model import predict_GovRevnGDP

@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        data=request.get_json()
        print(list(data))
        with open('model.bin', 'rb') as f_in:
            model = pickle.load(f_in)
            f_in.close()
        predictions = predict_GovRevnGDP(data, model)
        result = {
        'GovRevnGDP_prediction': list(predictions)
        }
        return jsonify(result)
        #return jsonify(GeoEco1)
