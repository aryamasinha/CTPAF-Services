# -*- coding: utf-8 -*-
"""startup_prediction_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vSmZCz6Ct3wHq99lNw72o3HnBYQtOLXr
"""

# import statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


df = pd.read_csv('startup_data.csv', header=0)
df = df.dropna()
df.drop(df.columns[[0]], axis = 1, inplace = True)

data = pd.get_dummies(df, columns =['city', 'category_code', 'has_VC', 'has_angel'])

data
X = data.iloc[:,1:]
Y = data.iloc[:,0]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)

classifier = LogisticRegression(solver='lbfgs',random_state=0)
classifier.fit(X_train, Y_train)

predicted_y = classifier.predict(X_test)

print('Accuracy: {:.2f}'.format(classifier.score(X_test, Y_test)))

