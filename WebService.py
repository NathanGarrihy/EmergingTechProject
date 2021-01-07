from flask import Flask, jsonify, request
import json
import tensorflow as tflow

app = Flask(__name__)

@app.route('/')
def parseIndex():
    return app.send_static_file('index.html')

@app.route('/index', methods=['GET'])
def parseGet():
    return app.send_static_file('index.html')

@app.route('/process/pow', methods=['POST'])
def parsePost():
    data = request.data
    myJson = json.loads(data)

    wSpeed = float(myJson['speed'])
    model = tflow.keras.models.load_model('predictionModel.h5')

    prediction = model.predict([wSpeed])
    flatten = prediction.flatten()
    print(flatten[0])
    return str(flatten[0]) 