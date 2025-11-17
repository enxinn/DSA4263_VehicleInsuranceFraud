#importing libraries
import numpy as np
import pandas as pd
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
    #return "Hello World"

# #prediction function
# def ValuePredictor(to_predict_list):
#     to_predict = np.array(to_predict_list).reshape(1,12)
#     loaded_model = pickle.load(open(r"models/model.pkl","rb"))
#     result = loaded_model.predict(to_predict)
#     return result[0]


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        predict_list = request.form.to_dict()
        to_predict_list = {key: int(value) for key, value in predict_list.items()}
        # print(to_predict_list)
        to_predict_list["AgeVehicleRatio"] = to_predict_list["Age"] / (to_predict_list["AgeOfVehicle"] + 1)
        # to_predict_list=list(to_predict_list.values())
        # to_predict_list = list(map(int, to_predict_list))
        print(to_predict_list)
        to_predict = pd.DataFrame(to_predict_list, index = [0])
        print("yes")
        loaded_model = pickle.load(open(r"models/model.pkl","rb"))
        result = loaded_model.predict(to_predict)
        
        if int(result)==1:
            prediction='Fraud suspected'
        else:
            prediction='Fraud not suspected'
            
        return render_template("result.html",prediction=prediction)

if __name__ == "__main__":
	app.run(debug=True)