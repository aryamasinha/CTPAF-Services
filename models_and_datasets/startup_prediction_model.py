import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


df = pd.read_csv('startup_data.csv', header=0)
df = df.dropna()
df.drop(df.columns[[0]], axis = 1, inplace = True)
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['category_code'] = label_encoder.fit_transform(df['category_code'])
df['city'] = label_encoder.fit_transform(df['city'])

x_data = df.iloc[:,0:-1]
y_data = df.iloc[:,-1]
X_train, X_test, Y_train, Y_test = train_test_split(x_data, y_data, random_state=0)

classifier = LogisticRegression(solver='lbfgs',random_state=0)
classifier.fit(X_train, Y_train)


with open('startup_model.pkl', 'wb') as file:
    pickle.dump(classifier, file)

