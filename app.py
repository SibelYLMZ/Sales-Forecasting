from flask import Flask
from flask import request
import pickle
import statsmodels
import numpy as np
import pandas
global model

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/predict')
def predict():
    feature1 = float(request.args.get('OTV'))
    feature2 = float(request.args.get('Faiz'))
    feature3 = float(request.args.get('EUR'))

    predictions = model.predict(pandas.DataFrame([[feature1,feature2,feature3]], columns = ['OTV Orani','Faiz','EUR/TL']))
    print(predictions.to_json())
    return predictions.to_json().values()
def load_model():
    with open('res_new.pkl', 'rb') as file:
        model_new = pickle.load(file)
    return model_new
model = load_model()
if __name__ == '__main__':
    
    app.run()