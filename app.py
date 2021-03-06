from flask import Flask , render_template , request
import pickle
import numpy as np
import pandas as pd

from models_and_datasets.data_science_jobs_analysis import analysisModel

with open(f'models_and_datasets/startup_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open(f'models_and_datasets/training_cols.pkl', 'rb') as f:
    traincols = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/startup')
def startup():
    return render_template('startup_form.html')


@app.route('/datascience')
def datascience():
    return render_template('data_science_form.html')


@app.route('/result_datascience', methods = ['post'])
def result_ds():
    d = request.form.to_dict()
    data = d.values()
    score = analysisModel.predict(data)
    return render_template('result_datascience.html',data = score)

@app.route('/result_startup' , methods = ['post'])
def result_st():
    location = request.form['location']
    category = request.form['category']
    hasvc = request.form['vc']
    hasangel = request.form['angel']
    if hasangel == "hasAngel":
        angel = 1
    else:
        angel = 0

    if hasvc == "hasVC":
        vc = 1
    else:
        vc = 0

    df1 = pd.DataFrame([[location, category,vc,angel]],columns=['city', 'category_code', 'has_VC', 'has_angel'])    
    df1 = pd.get_dummies(df1, columns =['city','category_code','has_VC','has_angel'])
    testcols = df1.columns
    missingcols = set(traincols) - set(testcols)
    a = np.zeros(len(missingcols) ,dtype = int)
    df2 = pd.DataFrame([a],columns=missingcols)     
    data = pd.concat([df1, df2], axis=1)
    data = data[traincols]
    predicted_y = model.predict(data)
    return render_template('result_startup.html',data = predicted_y)

if __name__ == "__main__":
    app.run(debug=True)