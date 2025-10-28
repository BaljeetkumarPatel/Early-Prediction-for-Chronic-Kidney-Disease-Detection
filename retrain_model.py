import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv('Dataset/kidney_disease.csv')

# Clean up classification values
df['classification'] = df['classification'].replace({'ckd\t': 'ckd'})

# Prepare features
features = ['rbc', 'pc', 'bgr', 'bu', 'pe', 'ane', 'dm', 'cad']

# Create X (features) array
X = []
for _, row in df.iterrows():
    try:
        # Convert features to numeric
        rbc = 1 if str(row.get('rbc')).lower() == 'abnormal' else 0
        pc = 1 if str(row.get('pc')).lower() == 'abnormal' else 0
        bgr = float(row['bgr']) if pd.notna(row['bgr']) else 100
        bu = float(row['bu']) if pd.notna(row['bu']) else 30
        pe = 1 if str(row.get('pe')).lower() == 'yes' else 0
        ane = 1 if str(row.get('ane')).lower() == 'yes' else 0
        dm = 1 if str(row.get('dm')).lower() == 'yes' else 0
        cad = 1 if str(row.get('cad')).lower() == 'yes' else 0
        X.append([rbc, pc, bgr, bu, pe, ane, dm, cad])
    except Exception as e:
        print(f"Error processing row: {e}")
        continue

X = np.array(X)

# Create y (target) array - encode 'ckd' as 0, 'notckd' as 1
y = np.where(df['classification'] == 'notckd', 1, 0)

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model with balanced class weights
model = LogisticRegression(class_weight='balanced', random_state=42)
model.fit(X_scaled, y)

# Save scaler and model
with open('CKD_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open('CKD.pkl', 'wb') as f:
    pickle.dump(model, f)

# Test some cases
def test_case(values, label):
    scaled_values = scaler.transform([values])
    pred = model.predict(scaled_values)
    proba = model.predict_proba(scaled_values)
    print(f"\n{label}:")
    print("Input:", values)
    print("Prediction:", pred[0], "('ckd' if 0, 'notckd' if 1)")
    print("Probabilities:", proba[0])

print("\nTesting retrained model:")

# Test healthy case
test_case([0, 0, 95, 20, 0, 0, 0, 0], "Healthy case (all normal)")

# Test CKD case
test_case([1, 1, 400, 200, 1, 1, 1, 1], "CKD case (multiple issues)")

# Test borderline case
test_case([0, 0, 140, 45, 0, 0, 1, 0], "Borderline case")