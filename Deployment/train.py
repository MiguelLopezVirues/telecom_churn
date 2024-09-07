# import pckgs 
import sys

import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer

import pickle
import json

def run(path):
    print("\nImporting data...")
    df = import_data(path)

    print("\nPreparing data...")
    df_prepared = prepare_data(df)

    print("\nCreating pipeline...")
    pipeline = create_pipeline()

    print("Training model...")
    fitted_pipeline = train_model(pipeline, df_prepared)

    print("Saving model pipeline in pickle file...")
    with open("model.pkl","wb") as f:
        pickle.dump(fitted_pipeline,f)
    
    print("Model pipeline saved in model.pkl")

def import_data(path):
    # read data
    dtypes_dict = {
    'area_code': 'category',
    'state': 'category',
    'international_plan': 'category',  
    'voice_mail_plan': 'category',
    'Churn': 'int'
    }
    df = pd.read_csv(path, dtype=dtypes_dict)

    return df


def prepare_data(df):
    # Drop rows with missing target values
    df.drop_duplicates()

    # Engineer features
    df["total_minutes"] = df["total_day_minutes"] + df["total_eve_minutes"] + df["total_night_minutes"] + df["total_intl_minutes"]
    df["total_charge"] = df["total_day_charge"] + df["total_eve_charge"] + df["total_night_charge"] + df["total_intl_charge"]

    df["avg_charge_per_minute"] = df["total_charge"] / df["total_minutes"]

    # Prepare features for modelling - grouping
    sorted_state_categories = df.groupby('state')['Churn'].mean().sort_values()

    group_labels, _ = pd.qcut(range(len(sorted_state_categories)), 10, retbins=True, labels=False)

    category_group_map = pd.Series(group_labels, index=sorted_state_categories.index)
    print(category_group_map)
    # Export to JSON file
    with open('category_group_map.pkl', 'wb') as f:
        pickle.dump(category_group_map, f)

    df['grouped_states'] = df['state'].map(category_group_map).astype('category')

    # Prepare features for modelling - binning
    df["grouped_customer_service_calls"] = np.where(df["number_customer_service_calls"] >= 4, ">4", df["number_customer_service_calls"])
    df["grouped_customer_service_calls"] = df["grouped_customer_service_calls"].astype("category")

    # select features
    df = df[["grouped_states", "international_plan", "voice_mail_plan", "grouped_customer_service_calls", "total_charge", "avg_charge_per_minute", "Churn"]]

    return df

def create_pipeline():
    model = LogisticRegression()
    
    numerical_transformer = Pipeline([('imputer',SimpleImputer(strategy="median")),("scaler",StandardScaler())])
    categorical_transformer = Pipeline([('imputer',SimpleImputer(strategy="most_frequent")),("encoder",OneHotEncoder(drop="first"))])

    data_prep = ColumnTransformer(transformers=[
        ("numeric",numerical_transformer,["total_charge","avg_charge_per_minute"]),
        ("categorical",categorical_transformer,["grouped_states", "international_plan", "voice_mail_plan", "grouped_customer_service_calls"]),
    ], remainder="drop")

    pipeline = make_pipeline(data_prep, model)

    return pipeline

def train_model(pipeline, df):
    y = df.pop("Churn")
    X = df

    return pipeline.fit(X, y)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(len(sys.argv))
        print("Usage: python train.py <path_to_dataset_csv>")
        sys.exit(1)
    
    run(sys.argv[1])


    
