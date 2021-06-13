from flask import Flask , render_template , request
import pickle
import numpy as np
import pandas as pd
from csv import writer


with open(f'models_and_datasets/startup_model.pkl', 'rb') as f:
    model = pickle.load(f)

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


@app.route('/result_datascience')
def result_ds():
    return render_template('result_datascience.html')

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

    df = pd.DataFrame([[location, category,vc,angel]],columns=['city', 'category_code', 'has_VC', 'has_angel'])    
    print(df)
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    df['category_code'] = label_encoder.fit_transform(df['category_code'])
    df['city'] = label_encoder.fit_transform(df['city'])
    print(df)
    predicted_y = model.predict(df)
    print(predicted_y)
    return render_template('result_startup.html')
if __name__ == "__main__":
    app.run(debug=True)