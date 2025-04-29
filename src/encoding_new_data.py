def encode_new_data(df):
    df = df.copy()

    # 1. Target column (if present)
    if 'Churn' in df.columns:
        df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # 1.1: Gender
    df['gender'] = df['gender'].map({'Female': 0, 'Male': 1})

    # 1.2: Partner, Dependents, PhoneService, PaperlessBilling
    for col in ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']:
        df[col] = df[col].map({'No': 0, 'Yes': 1})

    # 1.3: OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies
    for col in ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']:
        df[col] = df[col].map({'No internet service': 0, 'No': 0, 'Yes': 1})

    # 1.4: MultipleLines
    df['MultipleLines'] = df['MultipleLines'].map({'No phone service': 0, 'No': 0, 'Yes': 1})

    # 1.5: InternetService
    df['InternetService'] = df['InternetService'].map({'DSL': 0, 'Fiber optic': 1, 'No': 2})

    # 1.6: Contract
    df['Contract'] = df['Contract'].map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})

    # 1.7: PaymentMethod
    df['PaymentMethod'] = df['PaymentMethod'].map({
        'Electronic check': 0, 
        'Mailed check': 1, 
        'Bank transfer (automatic)': 2, 
        'Credit card (automatic)': 3
    })

    return df
