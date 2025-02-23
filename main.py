import pandas as pd
from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
df=pd.read_csv("cleaned_data")
pipe = pickle.load(open("Ridgemodel.pkl","rb"))

@app.route('/')
def index():
    locations= sorted(df['location'].unique())
    return render_template('index.html',locations=locations)

@app.route('/predict',methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')
    print( location,bhk,bath,sqft)
    input = pd.DataFrame([[location,sqft,bhk,bath]],columns=['location','total_sqft','bhk','bath'])
    prediction = pipe.predict(input)[0] *1e5
    return str(np.round(prediction))
if __name__=='__main__':
    app.run(debug=True,port=5001)