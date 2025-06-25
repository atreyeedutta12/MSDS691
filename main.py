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
    
    #fetch('/predict', {
            #method: 'POST',
            #headers: {
                #'Content-Type': 'application/json'
            #},
            #body: JSON.stringify({ key: 'value' })
        #});
    #GeoEco1 = request.get_json(silent=True)
    #if request.is_json:
        #GeoEco1=request.form.get('some_field')
         #GeoEco1 = request.get_json(force=True)
        
         #print(list(GeoEco1))
         #return jsonify(GeoEco1)
    #else:
        #return "GET!"
    #if request.is_json:
    
    #else:
        #return jsonify({"error": "Not Json"}), 400

#if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=9696)
