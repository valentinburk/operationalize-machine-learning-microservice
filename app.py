from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

TITLE = "Sklearn Prediction Home"
HOST = "0.0.0.0"
PORT = 80
DEBUG = True
DATA_FILE = "./model_data/boston_housing_prediction.joblib"
LOG_LEVEL = logging.INFO

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(LOG_LEVEL)

def scale(payload):
    """Scales Payload"""
    
    LOG.info(f"Scaling Payload: \n{payload}")
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))

    return scaled_adhoc_predict

@app.route("/")
def home():
    html = f"<h3>{TITLE}</h3>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction
        
        input looks like:
        {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }
        
        result looks like:
        { "prediction": [ <val> ] }
        
        """
    
    # Logging the input payload
    json_payload = request.json
    LOG.info(f"JSON payload: \n{json_payload}")

    inference_payload = pd.DataFrame(json_payload)
    LOG.info(f"Inference payload DataFrame: \n{inference_payload}")

    # scale the input
    scaled_payload = scale(inference_payload)
    LOG.info(f"Scaled payload: \n{scaled_payload}")

    prediction = list(clf.predict(scaled_payload))
    LOG.info(f"Prediction: \n{prediction}")

    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    # load pretrained model as clf
    clf = joblib.load(DATA_FILE)
    app.run(host=HOST, port=PORT, debug=DEBUG)
