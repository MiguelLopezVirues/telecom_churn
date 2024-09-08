import sys 

import pandas as pd
import numpy as np

import pickle
import json

from flask import Flask
from flask import request
from flask import jsonify

app = Flask("churn")

@app.route('/predict_request', methods=['POST'])
def run():
    print("\nImporting data...")
    df = import_data(request)

    print("\nPreparing data...")
    df_preprocessed = preprocess_data(df)

    print("\nPredicting churn...")
    predictions = predict(df_preprocessed, "model.pkl")

    return predictions

def import_data(request):
    dtypes_dict = {
    'area_code': 'category',
    'state': 'category',
    'international_plan': 'category',  
    'voice_mail_plan': 'category'
    }
    customers = pd.DataFrame(request.get_json())
    df = customers.astype(dtypes_dict)
    print(df)
    return df

def preprocess_data(df):
    # Engineer features
    df["total_minutes"] = df["total_day_minutes"] + df["total_eve_minutes"] + df["total_night_minutes"] + df["total_intl_minutes"]
    df["total_charge"] = df["total_day_charge"] + df["total_eve_charge"] + df["total_night_charge"] + df["total_intl_charge"]

    df["avg_charge_per_minute"] = df["total_charge"] / df["total_minutes"]

    # prepare features for modelling - grouping
    with open('category_group_map.pkl', 'rb') as f:
        category_group_map = pickle.load(f)
    df['grouped_states'] = df['state'].map(category_group_map).astype('category')

    # prepare features for modelling - binning
    df["grouped_customer_service_calls"] = np.where(df["number_customer_service_calls"] >= 4, ">4", df["number_customer_service_calls"])
    df["grouped_customer_service_calls"] = df["grouped_customer_service_calls"].astype("category")

    # select features
    df = df[["grouped_states", "international_plan", "voice_mail_plan", "grouped_customer_service_calls", "total_charge", "avg_charge_per_minute"]]

    return df

def predict(X, pipeline_path):
    with open(pipeline_path, 'rb') as f:
        pipeline = pickle.load(f)


    probabilities = pipeline.predict_proba(X)[:,1][0]

    churn = int(probabilities >= 0.55)

    print(jsonify(churn))

    return jsonify(churn)

if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print(len(sys.argv))
    #     print("Usage: python predict.py <path_to_dataset_csv> <path_to_pipeline_pickle>")
    #     sys.exit(1)
    app.run(debug=True, host='0.0.0.0', port=9696)
    # run(sys.argv[1], sys.argv[2])