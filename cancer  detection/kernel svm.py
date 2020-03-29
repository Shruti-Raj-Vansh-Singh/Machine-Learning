# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:01:29 2019

@author: shruti
"""

#importing libraries
import pandas as pd
import numpy as np
import matplotlib as plt

#importing Pima Indian Diabetes Dataset
dataset = pd.read_csv("diabetes.csv")
X = dataset.iloc[:,1:8].values
y = dataset.iloc[:,8].values

#checking for missing data
dataset.isnull().sum()


#ENCODING CATEGORICAL DATA
from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#SPLITING THE DATASET INTO TRAINING AND TEST SETS
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

#FEATURE SCALING
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#USING KERNEL SUPPORT VECTOR MACHINE TO TRAIN THE MODEL
from sklearn.svm import SVC
classifier = SVC(kernel ="rbf",random_state =0 )
classifier.fit(X_train,y_train)

#PREDICTING THE RESULT
y_predict = classifier.predict(X_test)

#ACCURACY OF THE RESULT
from sklearn import metrics
acc = metrics.accuracy_score(y_predict,y_test)
print("Accuracy of Kernel Support Vector Machine is ",acc)

