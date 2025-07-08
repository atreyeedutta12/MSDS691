from flask import Flask 
# added as WIX not working
from flask_cors import CORS

##creating a flask app and naming it "app"
app = Flask('app')
# added as WIX not working
CORS(app) 
# added as WIX not working
@app.route('/')
def index():
    return "CORS is enabled for all!"

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
        'GovRevnGDP_prediction': list(round(predictions,2))
        }
        return jsonify(result)
        #return jsonify(GeoEco1)
