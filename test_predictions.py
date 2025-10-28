import pickle
import pandas as pd
import numpy as np

def test_prediction(model, values, label="Test case"):
    df = pd.DataFrame([values], columns=['rbc', 'pc', 'bgr', 'bu', 'pe', 'ane', 'dm', 'cad'])
    pred = model.predict(df)
    proba = model.predict_proba(df)
    print(f"\n{label}:")
    print("Input values:", values)
    print("Prediction:", pred[0], "('ckd' if 0, 'notckd' if 1)")
    print("Probabilities:", proba[0])
    return pred[0]

# Load model and dataset
model = pickle.load(open('CKD.pkl', 'rb'))
df = pd.read_csv('Dataset/kidney_disease.csv')

# Print model details
print("Model classes:", model.classes_)
print("\nModel type:", type(model))

# Test case 1: Known healthy case (all normal values)
healthy_case = [0, 0, 95, 20, 0, 0, 0, 0]  # All normal values
test_prediction(model, healthy_case, "Healthy case (all normal)")

# Test case 2: Known CKD case (multiple issues)
ckd_case = [1, 1, 400, 200, 1, 1, 1, 1]  # Multiple risk factors
test_prediction(model, ckd_case, "CKD case (multiple issues)")

# Test case 3: Borderline case
borderline = [0, 0, 140, 45, 0, 0, 1, 0]  # Slightly elevated values
test_prediction(model, borderline, "Borderline case")

# Find and test actual notckd cases from dataset
notckd_cases = df[df['classification'] == 'notckd'].head(3)
print("\nTesting actual 'notckd' cases from dataset:")
for idx, row in notckd_cases.iterrows():
    try:
        # Converting string to numeric
        rbc = 1 if str(row.get('rbc')).lower() == 'abnormal' else 0
        pc = 1 if str(row.get('pc')).lower() == 'abnormal' else 0
        bgr = float(row['bgr']) if pd.notna(row['bgr']) else 100
        bu = float(row['bu']) if pd.notna(row['bu']) else 30
        pe = 1 if str(row.get('pe')).lower() == 'yes' else 0
        ane = 1 if str(row.get('ane')).lower() == 'yes' else 0
        dm = 1 if str(row.get('dm')).lower() == 'yes' else 0
        cad = 1 if str(row.get('cad')).lower() == 'yes' else 0
        
        values = [rbc, pc, bgr, bu, pe, ane, dm, cad]
        test_prediction(model, values, f"Real notckd case {idx}")
    except Exception as e:
        print(f"Error processing row {idx}:", e)