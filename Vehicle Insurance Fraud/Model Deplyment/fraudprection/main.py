from re import template
import numpy as np
from flask import Flask, jsonify, render_template,request
import pickle
from joblib import dump, load

app = Flask(__name__, template_folder='template')  # Initialize the flask App
# loading the trained model
model = pickle.load(
    open(r'C:\Users\Aniket Pc\Desktop\projects\fraudprection\fraudmodel.pkl', 'rb'))
#sc = load(r'C:\Users\Aniket Pc\Desktop\projects\fraudprection\std_scaler.bin')


@app.route('/')  # Homepage
def home():
    print("Aniket")
    return render_template('index.html')


@app.route('/predict/', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print("TEST")

    # retrieving values from form
    print(request.form.values)
    init_features = [[int(x)for x in request.form.values()]]
    print(init_features)

    prediction = model.predict((np.array(init_features)))
    print(prediction)

    # rendering the predicted result
    return render_template('index.html', Prediction_text='Predicted Insurance Fraud: {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
