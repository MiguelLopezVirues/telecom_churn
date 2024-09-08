# End to end ML solution for Telecom Churn prediction
This end to end project consists on providing a solution for a churn business case given a telecom churn dataset. Value is provided through:
- Data analysis: Understanding the root of the problem and providing actionable insights.
- ML model evaluation and configuration: Proposing several ML models and evaluating them, then proposing on the configuration of batch and real-time inference.
- Deployment of the ML solution: Containerizing the selected ML model to be deployed as a real-time inference solution in AWS Elasticbeanstalk.

## Install
To run the projects file, download it and run `pip install -r requirements.txt` for the home directory. Otherwise, ``Pipfile`` and ``Pipfile.lock`` are available inside `\Deployment`

## Using the application
To test the project, run `python predict_request-test.py`. It will make a request to the AWS application and return the churn prediction {0,1} for the example written on the script.

## Contents
- ``Churn_Business_Case.md``: Summary description of the business case for telecom churn.
- ``requirements.txt``
- ``\Development``
    - ``churn_all.csv``: Source dataset
    - ``Churn_ML_model_evaluation.ipynb``: Notebook with the exploratory data analysis and insights, evaluation and selection of the ML model, proposal of inference configuration and final recommendations.
- ``\Deployment``
    - ``train.py``: Data import from the source dataset, data processing and training of the selected model configuration from the Churn_ML_model_evaluation notebook.
    - ``predict_request.py``: Model loading and prediction, served as a flask application. Receives a JSON file with the variables for a single customer. Returns either 1 or 0 as a churn prediction.
    - ``predict_request-test.py``: Test of the request with the information of a single customer.
    - ``model.pkl``
    - ``category_group_map.pkl``: Category mapping automatically engineered through training, called by predict_request to preprocess the customer data.
    - ``Pipfile and Pipfile.lock``
    - ``Dockerfile``