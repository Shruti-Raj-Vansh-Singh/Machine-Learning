import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("Data.csv")

X = dataset.iloc[:,-1].values
y = dataset.iloc[:,2].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
"""
the usage of labelencoder can be seen n the scenarios where on e or more han one col has values from a given set of 
values mostly in words and we want our modelto distinguish the words so we assign each word/category with a number 
so as to make it easier fro our model to interpret the values and use them in the equations for finding the values of y
"""
X[:,0] = labelencoder.fit_transform(X[:,0])
"""
there is one problem we face here. The values assigned to the different variables have numerical values of 1,2,3...
this that be interpreteed in a wrong way giving an idea that the var with vaule 2 is more important than the var 
with value 1 although this is not the case and hence we use the concept of OneHotEncoder that makes differnt col for 
each var and assigns a value 1 in the col correspomdong to that values"""
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarrray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

from sklearn.cross_validation import test_train_split
X_test,X_train,y_test,y_train = test_train_split(X,y,test_size=0.2)

#FOR LINEAR REGRESSION
from sklearn.linear_model import LinearRegression
regressor =LinearRegression()
regressor.fit(X_test,y_test)
y_predict = regressor.predict(y_test)
