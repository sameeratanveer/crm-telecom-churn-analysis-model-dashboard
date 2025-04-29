# importing
import pandas as pd
import joblib
from encoding_new_data import encode_new_data

# Load model and scaler
model = joblib.load('../models/logistic_regression_churn_model.pkl')
scaler = joblib.load('../models/scaler.pkl')
features = joblib.load('../models/features_used.pkl')

# New sample(s)
data = {
    'customerID': ['7590-VHVEG'],
    'gender': ['Female'],
    'SeniorCitizen': [0],
    'Partner': ['Yes'],
    'Dependents': ['No'],
    'tenure': [1],
    'PhoneService': ['No'],
    'MultipleLines': ['No phone service'],
    'InternetService': ['DSL'],
    'OnlineSecurity': ['No'],
    'OnlineBackup': ['Yes'],
    'DeviceProtection': ['No'],
    'TechSupport': ['No'],
    'StreamingTV': ['No'],
    'StreamingMovies': ['No'],
    'Contract': ['Month-to-month'],
    'PaperlessBilling': ['Yes'],
    'PaymentMethod': ['Electronic check'],
    'MonthlyCharges': [29.85],
    'TotalCharges': [29.85]
}
new_df = pd.DataFrame(data)
encoded = encode_new_data(new_df)

# Only use selected features
X_input = encoded[features].copy()

# Scale numeric features
num_cols = ['MonthlyCharges', 'TotalCharges', 'tenure']
X_input[num_cols] = scaler.transform(X_input[num_cols])

# Predict
prediction = model.predict(X_input)
prob = model.predict_proba(X_input)[0][1]

# Output
print(f"🔍 Churn Prediction: {'Yes' if prediction[0]==1 else 'No'} (Probability: {prob:.2f})")
