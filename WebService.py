from flask import Flask, jsonify, request
import json
import tensorflow as tflow
# https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html

app = Flask(__name__)

# Sets route index of app
@app.route('/')
def parseIndex():
    return app.send_static_file('index.html')

# takes speed data and uses model to calculate power
@app.route('/process/pow', methods=['POST'])
def parsePost():
    data = request.data
    myJson = json.loads(data)

    wSpeedValue = float(myJson['wSpeedValue'])
    model = tflow.keras.models.load_model('predictionModel.h5')

    prediction = model.predict([wSpeedValue])
    flatten = prediction.flatten()

    return str(flatten[0]) 