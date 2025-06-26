from flask import Flask 

##creating a flask app and naming it "app"
app = Flask('app')

@app.route('/test', methods=['GET'])
def test():
    return 'Pinging Model Application!!'

import pickle
from flask import Flask, request, jsonify
from ml_model import predict_GovRevnGDP

@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        GeoEco1 = request.get_json(force=True, silent=True)
        print(list(GeoEco1))
        with open('model.bin', 'rb') as f_in:
            model = pickle.load(f_in)
            f_in.close()
        predictions = predict_GovRevnGDP(GeoEco1, model)
        result = {
        'GovRevnGDP_prediction': list(predictions)
        }
        return jsonify(result)
