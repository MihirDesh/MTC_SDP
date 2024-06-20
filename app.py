from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# import os
# print(os.getcwd())

# import joblib

# model_path = 'models/random_forest_model.joblib'

# if os.path.exists(model_path):
#     model = joblib.load(model_path)
# else:
#     print(f"Error: File '{model_path}' does not exist.")

model = joblib.load('models/random_forest_model.joblib')

features = ['SeriousDlqin2yrs', 'RevolvingUtilizationOfUnsecuredLines', 'age', 'NumberOfTime30-59DaysPastDueNotWorse',
            'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
            'NumberRealEstateLoansOrLines', 'TotlAssets', 'TotalLiabilities', 'EmploymentStatus_Student', 'EmploymentStatus_Unemployed',
            'EducationLevel_Bachelor Degree', 'EducationLevel_High School', 'EducationLevel_Master Degree',
            'EducationLevel_PhD', 'FeedbackSentimentScore', 'ServiceLogSentimentScore']

@app.route('/predict', methods=['GET','POST'])
def predict():
    data = request.get_json()
    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data[features])[0]
    return jsonify({'CreditScore': prediction})

if __name__ == '__main__':
    app.run(debug=True)