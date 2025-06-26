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
    if request.is_json:
        GeoEco1 = request.json
        Inflation_CPI = GeoEco1.get('Inflation_CPI')
        GDP_Current_USD = GeoEco1.get('GDP_Current_USD')
        return jsonify({"message":f"Received data: Inflation_CPI={Inflation_CPI},GDP_Current_USD={GDP_Current_USD}"})
    else:
        return jsonify({"error": "Request must be JSON"})
        #with open('model.bin', 'rb') as f_in:
            #model = pickle.load(f_in)
            #f_in.close()
        #predictions = predict_GovRevnGDP(GeoEco1, model)
        #result = {
        #'GovRevnGDP_prediction': list(predictions)
        #}
        #return jsonify(result)
        #return jsonify(GeoEco1)
