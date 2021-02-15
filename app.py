from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import pymongo
import pickle
import numpy as np

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'WokeRUS'
app.config['MONGO_URI'] = "mongodb://localhost:27017/WokeRUS"
mongo = PyMongo(app)

model = pickle.load(open('model.pkl', 'rb'))
print(model) # to see if the model works or is loaded.

@app.route("/")
def welcome():
       return render_template('classify.html') 

@app.route('/predict', methods=['POST'])
def predict():
       # print (request.form.values())
       cs = request.form['Credit_Score']
       print(cs)
       eml = request.form['Emp_Length']
       dti = request.form['Debt_income_ratio'] 
       loa = request.form['Loan_Amount']
       # int_features = {'Credit_Score':cs, 'Emp_Length':eml, 'Debt_income_ratio':dti, 'Loan_Amount':loa}
       if float(cs) < 600:
              return render_template('classify.html', prediction_text = 'your application is rejected')
       else:
              final_features = [np.array([cs,eml,dti,loa])]
              prediction = model.predict(final_features)
              
              if prediction == 0:
                     return render_template('classify.html', prediction_text = 'your application is rejected')
              else:
                     return render_template('classify.html', prediction_text = 'your application is Approved')
      
# This information page would 
@app.route("/information")
def dataset():
       col = mongo.db.sample_consolidated
       c = col.find({}, {'_id' : False})
       d = [i for i in c]
       return render_template('datadb.html', variable=d) 


if __name__ == "__main__":
       app.run(port=8000, debug=True)