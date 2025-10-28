from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__,static_folder='static')

# Load model and scaler
model = pickle.load(open('CKD.pkl','rb'))
scaler = pickle.load(open('CKD_scaler.pkl','rb'))

print("Model and scaler loaded successfully")

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Prediction', methods=['POST', 'GET'])
def prediction():
    return render_template('assessment.html')

@app.route('/assessment.html')
def direct_assessment():
    return render_template('assessment.html')



# @app.route('/Home', methods=['POST', 'GET'])
# def my_home():
#    return render_template('home.html')

@app.route('/home.html')
def direct_home():
    return render_template('home.html')



# @app.route('/predict', methods=['POST']) # route to show the predictions in a web UI
# def predict():
#     # reading the inputs given by the user
#     # input_features = [float(x) for x in request.form.values()]

#     # features_value = [np.array(input_features)]

#     # features_name = ['bu', 'bgr', 'ane',
#     #                 'cad', 'pc', 'rbc',
#     #                 'dm', 'pe']
#     # Extract form values
#     bu = float(request.form['bu'])
#     bgr = float(request.form['bgr'])
#     ane = int(request.form['ane'])
#     cad = int(request.form['cad'])
#     pc = int(request.form['pc'])
#     rbc = int(request.form['rbc'])
#     dm = int(request.form['dm'])
#     pe = int(request.form['pe'])

#     # Create DataFrame
#     features = {
#         'rbc': rbc,
#         'pc': pc,
#         'bgr': bgr,
#         'bu': bu,
#         'pe': pe,
#         'ane': ane,
#         'dm': dm,
#         'cad': cad
#     }

#     df = pd.DataFrame([features])

#     # predictions using the loaded model file
#     output = model.predict(df)
#     # showing the prediction results in a UI
#     return render_template('result.html', prediction_text=output)

@app.route('/predict', methods=['POST'])
def predict():
    # Collect inputs
    bu = float(request.form['bu'])
    bgr = float(request.form['bgr'])
    ane = int(request.form['ane'])
    cad = int(request.form['cad'])
    pc = int(request.form['pc'])
    rbc = int(request.form['rbc'])
    dm = int(request.form['dm'])
    pe = int(request.form['pe'])

    # Create input array and scale it
    input_values = [[rbc,pc,bgr,bu,pe,ane,dm,cad]]
    input_scaled = scaler.transform(input_values)

    # Debug: print input values
    print("Input values:", input_values)
    print("Scaled values:", input_scaled)

    # Predict class
    prediction = model.predict(input_scaled)

    # In our model, class 0 means "ckd" (high risk) and class 1 means "notckd" (low risk)
    is_high_risk = (prediction[0] == 0)  # True if prediction is 0 (ckd)

    # Predict probability and get the confidence for the predicted class
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_scaled)
        # For high risk (ckd, class 0), use probability[0]
        # For low risk (notckd, class 1), use probability[1]
        confidence_score = round(proba[0][0 if is_high_risk else 1] * 100, 2)
        print(f"Prediction: {'CKD' if is_high_risk else 'Not CKD'}")
        print(f"Confidence: {confidence_score}%")
    else:
        confidence_score = None
        print("Model does not support predict_proba.")

    # Pass prediction and confidence to result page
    return render_template('result.html',
                           is_high_risk=is_high_risk,
                           confidence_score=confidence_score)


if __name__ == '__main__':
  # running the app
  app.run(debug=True)


