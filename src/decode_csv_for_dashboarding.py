import pandas as pd

# Step 1: Load the CSV file 
df = pd.read_csv('../data/final_churn_predictions.csv') 

# Step 2: Defining reverse mappings:
reverse_maps = {
    'gender': {0: 'Female', 1: 'Male'},
    'SeniorCitizen':{0: 'No', 1: 'Yes'},
    'Partner': {0: 'No', 1: 'Yes'},
    'Dependents': {0: 'No', 1: 'Yes'},
    'PhoneService': {0: 'No', 1: 'Yes'},
    'PaperlessBilling': {0: 'No', 1: 'Yes'},
    'MultipleLines': {0: 'No/No phone service', 1: 'Yes'},
    'OnlineSecurity': {0: 'No/No internet service', 1: 'Yes'},
    'OnlineBackup': {0: 'No/No internet service', 1: 'Yes'},
    'DeviceProtection': {0: 'No/No internet service', 1: 'Yes'},
    'TechSupport': {0: 'No/No internet service', 1: 'Yes'},
    'StreamingTV': {0: 'No/No internet service', 1: 'Yes'},
    'StreamingMovies': {0: 'No/No internet service', 1: 'Yes'},
    'InternetService': {0: 'DSL', 1: 'Fiber optic', 2: 'No'},
    'Contract': {0: 'Month-to-month', 1: 'One year', 2: 'Two year'},
    'PaymentMethod': {
        0: 'Electronic check',
        1: 'Mailed check',
        2: 'Bank transfer (automatic)',
        3: 'Credit card (automatic)'
    },
    'Churn': {0: 'No', 1: 'Yes'},
    'Churn_Predicted': {0: 'No', 1: 'Yes'}
}

# Step 3: Apply reverse mapping to the appropriate columns
for col, mapping in reverse_maps.items():
    if col in df.columns:
        df[col] = df[col].map(mapping)

# Step 4: Save the cleaned dataset
df.to_csv('../data/churn_dashboard_ready.csv', index=False)
print("Cleaned file saved: churn_dashboard_ready.csv")
