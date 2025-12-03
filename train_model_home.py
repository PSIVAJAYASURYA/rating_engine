# train_model_home.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Generate synthetic data

n = 500
df = pd.DataFrame({
'age': np.random.randint(18, 80, n),
'building_years': np.random.randint(0, 100, n),
'sum_insured': np.random.randint(100000, 1000000, n)
})
df['ml_multiplier'] = 1 + (0.001 * df['building_years']) + (0.000001 * df['sum_insured'])

X = df[['age', 'building_years', 'sum_insured']]
y = df['ml_multiplier']

model = RandomForestRegressor(n_estimators=10, random_state=42)
model.fit(X, y)

if not os.path.exists('models'):
    os.makedirs('models')

joblib.dump(model, 'models/home_risk_model_v1.joblib')
df.to_csv('training_data.csv', index=False)

print("Model trained and saved as models/home_risk_model_v1.joblib")
