import pandas as pd
import joblib

# Load processed dataset 
df = pd.read_csv('../data/telecom_churn_data_cleaned.csv')  

# Load trained model, scaler, and feature list
model = joblib.load('../models/logistic_regression_churn_model.pkl')
scaler = joblib.load('../models/scaler.pkl')
features = joblib.load('../models/features_used.pkl')

# Preparing feature input
X = df[features].copy()

# Scale numerical columns
num_cols = ['MonthlyCharges', 'TotalCharges', 'tenure']
X[num_cols] = scaler.transform(X[num_cols])

# Predict churn
churn_probs = model.predict_proba(X)[:, 1]
churn_preds = (churn_probs >= 0.5).astype(int)  # You can change threshold if needed

# Add predictions to original DataFrame
df['Churn_Prob'] = churn_probs
df['Churn_Predicted'] = churn_preds

# Save final CSV for Power BI
df.to_csv('../data/final_churn_predictions.csv', index=False)
print("Final dataset with predictions saved as final_churn_predictions.csv")
