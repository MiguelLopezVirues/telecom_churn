
# Business Case Introduction for Churn Prediction

## 1. Business Problem

The telecom company is experiencing customer churn, which directly impacts revenue and customer lifetime value. **Churn rate**, the percentage of customers leaving the service, needs to be predicted in order to design targeted retention strategies. The goal is to develop a machine learning model that can accurately predict which customers are at the highest risk of churning, enabling the company to intervene proactively and reduce customer turnover.

## 2. Data Provided

You have been provided with a dataset that includes the following variables:

- **state**: Two-letter code of the customer’s state
- **area_code**: Telephone area code (prefix)
- **phone_number**: Customer's telephone number
- **international_plan**: Whether the customer has an international plan (Yes/No)
- **voice_mail_plan**: Whether the customer has a voice mail plan (Yes/No)
- **number_vmail_messages**: Number of messages in the voice mail
- **total_day_minutes**: Morning usage in minutes
- **total_day_calls**: Number of morning calls
- **total_day_charge**: Morning charges (billing)
- **total_eve_minutes**: Evening usage in minutes
- **total_eve_calls**: Number of evening calls
- **total_eve_charge**: Evening charges
- **total_night_minutes**: Night usage in minutes
- **total_night_calls**: Number of night calls
- **total_night_charge**: Night charges
- **total_intl_minutes**: International usage in minutes
- **total_intl_calls**: Number of international calls
- **total_intl_charge**: International charges
- **number_customer_service_calls**: Number of customer service interactions

## 3. Expectations and Deliverables

The company expects the following actions to be accomplished:
- **Data analysis** to understand which variables are most predictive of churn, including any relationships between usage patterns and customer churn behavior.
- **Feature creation** to segment customers effectively based on their service usage.
- **Churn prediction model** to anticipate which customers are at risk of leaving.
- **Actionable insights** to recommend how the company can leverage these predictions to select customers in two scenarios: 
    1. A fixed budget for the 500 top-risk customers 
    2. Adjusting the risk tolerance to maximize churn prevention campaigns profit. 

The completion of this talk will enable the business to mitigate churn, increase retention, and improve overall profitability.
