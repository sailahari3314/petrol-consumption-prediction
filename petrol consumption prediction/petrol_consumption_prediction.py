# -*- coding: utf-8 -*-
"""11July_Petrol_Consumption_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xROAdy1knd2UDWD43q87QZiE32fqRhjr
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('petrol_consumption.csv')
df.head()

df.shape

df.isnull().sum()

df.dtypes

x = df.iloc[:,:-1]
y = df.iloc[:,-1]
print(x.shape)
print(y.shape)
print(type(x))
print(type(y))

x.head()

y.head()

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

"""### 1) Linear Regression"""

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

def gen_metrics(ytest,ypred):
    mse = mean_squared_error(ytest,ypred)
    rmse = np.sqrt(mean_squared_error(ytest,ypred))
    mae = mean_absolute_error(ytest,ypred)
    r2s = r2_score(ytest,ypred)
    print('MSE',mse)
    print('RMSE',rmse)
    print('MAE',mae)
    print('R2_Score',r2s)

from sklearn.linear_model import LinearRegression

m1 = LinearRegression()
m1.fit(x_train,y_train)

print('Training Score',m1.score(x_train,y_train))
print('Testing Score',m1.score(x_test,y_test))

ypred_m1 = m1.predict(x_test)
print(ypred_m1)

gen_metrics(y_test,ypred_m1)
