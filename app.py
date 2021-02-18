from flask import Flask, render_template, request, redirect, url_for
# from flask_pymongo import PyMongo
import pymongo
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import numpy as np

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'WokeRUS'
app.config['MONGO_URI'] = "mongodb://localhost:27017/WokeRUS"
# mongo = PyMongo(app)


# Classification model
model_classfy = pickle.load(open('model_calssify.pkl', 'rb'))
model_scaler_classfy = pickle.load(open('scaler_calssify.pkl', 'rb'))

# Interest model 
model_regression = pickle.load(open('model_regression.pkl', 'rb'))
model_scaler_regression = pickle.load(open('scaler_regresion.pkl', 'rb'))

# print(model_scaler_classfy, model_classfy)
# print(model_scaler_regression, model_regression) # to see if the model works or is loaded.


@app.route("/")
def welcome():
       return render_template('classify.html') 

@app.route('/predict', methods=['POST'])
def predict():
       cs = request.form['Credit_Score']
       eml = request.form['Emp_Length']
       dti = request.form['Debt_income_ratio'] 
       loa = request.form['Loan_Amount']

       # int_features = {'Credit_Score':cs, 'Emp_Length':eml, 'Debt_income_ratio':dti, 'Loan_Amount':loa}
       if float(cs) < 600 or float(dti) > 45:
              return render_template('classify.html', prediction_text = 'your application is rejected')
       else:
              final_features = [np.array([cs,eml,dti,loa])]
              scaler = StandardScaler()
              scaled_inputs = scaler.fit_transform (final_features)
              prediction = model_classfy.predict(final_features)
              
              if prediction == 0:
                     return render_template('classify.html', prediction_text = 'your application is rejected')
              else:
                     # return redirect(url_for('/interest', args1= cs, args2=eml), code=307)
                     return redirect ('/interest?', code=302) #render_template('classify.html', prediction_text = 'your application is Approved')
                     # return redirect ('/')

@app.route('/interest', methods=['GET'])
def interest():
       return render_template ('interest.html')

@app.route('/interest', methods=['POST'])
def calculation():
 
       loa = request.form['Loan_Amount']
       dti = request.form['Debt_income_ratio']
       eml = request.form['Emp_Length']
       cs = request.form['Credit_Score']
       ai = request.form['annual_inc']
       inq = request.form['inq_last_6mths']
       acc = request.form['mo_sin_rcnt_tl']   

       features = [float(x) for x in request.form.values()]
       final_features = [np.array(features)]
  
       scaler = StandardScaler()
       scaled = scaler.fit_transform(final_features)
       
       print(features)
       print(final_features)
       print(scaled)
       predictions = model_regression.predict(scaled)
       print (predictions)
       output = round(predictions[0],0)
       print(output)
       predictions_low = output-3
       predictions_high = output+3
       prediction_range = f'Your estimated interesed is between {predictions_low}% - {predictions_high}%'
       return render_template('interest.html', prediction_text = prediction_range)



       # This information page would 
@app.route("/information")
def dataset():
       col = mongo.db.sample_consolidated
       c = col.find({}, {'_id' : False})
       d = [i for i in c]
       return render_template('datadb.html', variable=d) 

# @app.route('/')
#        def refresh():
#               return redirect


if __name__ == "__main__":
       app.run(port=8000, debug=True)