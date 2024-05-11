from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import os
import pickle
app=Flask(__name__)
model=pickle.load(open(r'rdf.pkl','rb'))
scale=pickle.load(open(r'scaler.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=["POST","GET"])
def predict() :
    return render_template("input.html")
@app.route('/submit',methods=["POST","GET"])
def submit():
    input_feature=[int(x) for x in request.form.values()]
    input_feature=[np.array(input_feature)]
    print(input_feature)
    names=['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']
    data=pd.DataFrame(input_feature,columns=names)
    print(data)
    prediction=model.predict(data)
    print(prediction)
    prediction=int(prediction)
    print(type(prediction))
    if (prediction==0):
        return render_template("output.html",result="loan will not be approved")
    else:
        return render_template("output.html",result="loan will be approved")
    
if __name__=="__main__":
        app.run(debug=False)