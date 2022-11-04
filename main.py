from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "Computation"


@app.route('/compute', methods=['POST'])
def compute():
    slackUsername = 'ibukun lawson'
    operator_type = request.json['operation_type']
    x = int(request.json["x"])
    y = int(request.json["y"])

    if operator_type == 'addition':
        results = x + y

    elif operator_type == 'subtraction':
        results = x - y
    elif operator_type == 'multiplication':
        results = x * y
    return jsonify({
        'slackUsername': slackUsername,
        'operation_type': operator_type,
        'result': results
    })


app.run(host='0.0.0.0', port=81)
