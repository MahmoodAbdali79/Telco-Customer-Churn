# Predicting Telecom Customer Churn
## Introduction
Telecommunicationcompanies often face the challenge of retaining customers who are at risk of churning, i.e., discontinuing their services. Losing customers can significantly impact the company's revenue and profitability. To address this issue, we embarked on a project to develop a predictive model that identifies customers likely to churn, enabling proactive retention strategies.

##  Problem Statement
The primary objective of this project is to create a predictive model capable of identifying telecom customers who are likely to churn. By analyzing historical customer data, we aim to develop a model that can predict churn with high accuracy, enabling the company to take preventive measures and retain valuable customers.

## Dataset and Approach
We utilized a telecom churn dataset for our analysis, which contains information about customers' demographics, services availed, and churn status. The project was divided into two main phases:

1. Exploratory Data Analysis (EDA):
In the first phase, we conducted exploratory data analysis (EDA) to gain insights into the dataset's characteristics. We explored various features, visualized distributions, and identified patterns and correlations. The EDA process helped us understand the factors influencing customer churn.

Notebook: Telecom EDA_v1.ipynb

2. Model Development:
In the second phase, we developed a predictive model to forecast customer churn. We experimented with different machine learning algorithms and techniques, fine-tuning hyperparameters to optimize model performance. Given the importance of correctly identifying churn cases, we prioritized **recall** as the primary evaluation metric.

Notebook: Telecom Churn_Model.ipynb

## Model Performance
After rigorous experimentation and evaluation, we achieved promising results with our predictive model:

- **Recall**: 0.88
- **Precision**: 0.71
- **F1 Score**: 0.79  
These metrics indicate that our model is effective at identifying customers who are likely to churn, with a high proportion of actual churners correctly classified.

**To Do**: Conduct error analysis to find out which users are more challenging.

## Conclusion
In conclusion, our project demonstrates the effectiveness of machine learning in predicting telecom customer churn. By leveraging predictive analytics, telecom companies can proactively identify at-risk customers and implement targeted retention strategies, ultimately improving customer satisfaction and reducing churn rates.


# Telecom Churn Prediction API

This API predicts whether a customer will churn or not based on their telecom service usage.

How to Run the Server
To run the server hosting the Telecom Churn Prediction API, follow these steps:

1. Install the required dependencies listed in the requirements.txt file. You can do this using pip:
```
pip install -r requirements.txt
```

2. Start the server using Uvicorn. Assuming your FastAPI app is in a file named app.py, run the following command:
```
uvicorn app:app --host 0.0.0.0 --port 8000
```
This command tells Uvicorn to run the FastAPI app defined in the app module (app.py) and listen on port 8000. Adjust the host and port as needed.


## Endpoint

### Predict Churn

- **URL**: `/predict`
- **Method**: `POST`
- **Description**: Endpoint to predict churn for a given customer.

#### Request Body

| Field             | Type   | Description                                           |
|-------------------|--------|-------------------------------------------------------|
| `SeniorCitizen`   | integer| Whether the customer is a senior citizen (0 or 1)     |
| `Partner`         | string | Whether the customer has a partner (Yes or No)        |
| `Dependents`      | string | Whether the customer has dependents (Yes or No)       |
| `tenure`          | integer| Number of months the customer has been with the company|
| `OnlineSecurity`  | string | Customer's online security status                     |
| `OnlineBackup`    | string | Customer's online backup status                       |
| `DeviceProtection`| string | Customer's device protection status                   |
| `TechSupport`     | string | Customer's tech support status                        |
| `Contract`        | string | Customer's contract type (Month-to-month, One year, Two year) |
| `PaperlessBilling`| string | Whether the customer has paperless billing (Yes or No)|
| `PaymentMethod`   | string | Customer's payment method                             |
| `MonthlyCharges`  | float  | Customer's monthly charges                            |
| `TotalCharges`    | float  | Customer's total charges                              |

#### Example Request Body

```json
{
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 24,
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "Contract": "One year",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Credit card (automatic)",
  "MonthlyCharges": 65.5,
  "TotalCharges": 1564.2
}
```

### Response
- Type: JSON Object
- Fields:
    - prediction: Predicted churn status (Churn or Not Churn)

Example Response
```json
{
  "prediction": "Not Churn"
}
```

## Usage
To use this API, send a POST request to the /predict endpoint with the required input data in the request body.
The API will return the predicted churn status for the given customer.



