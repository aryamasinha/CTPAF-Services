import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('startup_data.csv', header=0)


df.drop(df.columns[0], 
   axis = 1, inplace = True)


data = pd.get_dummies(df, columns =['city','category_code','has_VC','has_angel'])

X = data.iloc[:,1:]
Y = data.iloc[:,0]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)

classifier = LogisticRegression(solver='lbfgs',random_state=0)
classifier.fit(X_train, Y_train)

with open('startup_model.pkl', 'wb') as file:
    pickle.dump(classifier, file)

traincols = X.columns 

with open('training_cols.pkl', 'wb') as file:
    pickle.dump(traincols, file)

