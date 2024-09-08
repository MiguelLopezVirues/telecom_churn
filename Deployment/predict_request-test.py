import requests


host = "churn-serving-2.eba-2u7sye8k.eu-west-1.elasticbeanstalk.com"
url = f"http://{host}/predict_request"

customers = [
    {
        "state":"KS",
        "area_code":415,
        "phone_number":" 382-4657",
        "international_plan":" no",
        "voice_mail_plan":" yes",
        "number_vmail_messages":25,
        "total_day_minutes":265.1,
        "total_day_calls":110*1.8,
        "total_day_charge":45.07*1.8,
        "total_eve_minutes":197.4,
        "total_eve_calls":99,
        "total_eve_charge":16.78,
        "total_night_minutes":244.7,
        "total_night_calls":91,
        "total_night_charge":11.01,
        "total_intl_minutes":10.0,
        "total_intl_calls":3,
        "total_intl_charge":2.7,
        "number_customer_service_calls":1
    }
]

response = requests.post(url, json=customers).json()
print(response)

# for prediction in response["churn_prediction"]:
#     if prediction == True:
#         print("Customer will churn")