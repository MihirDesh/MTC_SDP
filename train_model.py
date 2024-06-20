import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os

data = pd.read_csv('./modified_data.csv')

print(data.head())
for col in ['MonthlyIncome', 'NumberOfDependents', 'TotalAssets', 'TotalLiabilities']:
    data[col].fillna(data[col].mean(), inplace=True)

features = ['SeriousDlqin2yrs', 'RevolvingUtilizationOfUnsecuredLines', 'age', 'NumberOfTime30-59DaysPastDueNotWorse',
            'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
            'NumberRealEstateLoansOrLines', 'TotalAssets', 'TotalLiabilities', 'EmploymentStatus_Student', 'EmploymentStatus_Unemployed',
            'EducationLevel_Bachelor Degree', 'EducationLevel_High School', 'EducationLevel_Master Degree',
            'EducationLevel_PhD', 'FeedbackSentimentScore', 'ServiceLogSentimentScore']

target = 'CreditScore'

X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

models_dir = 'models/'
os.makedirs(models_dir, exist_ok=True)

# Save the trained model using Joblib
joblib.dump(model, os.path.join(models_dir, 'random_forest_model.joblib'))