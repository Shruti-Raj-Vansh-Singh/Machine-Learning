# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 01:44:23 2019

@author: shruti
"""

import pandas as pd

dataset = pd.read_csv("diabetes.csv")

X = dataset.iloc[:,0:8]
y = dataset.iloc[:,8:9]

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

from sklearn.preprocessing import StandardScaler
X_sc = StandardScaler()
X_train = X_sc.fit_transform(X_train)
X_test = X_sc.transform(X_test)


from xgboost import XGBClassifier
classifier = XGBClassifier(random_state=1,learning_rate=0.01)
classifier.fit(X_train,y_train)
classifier.score(X_test,y_test)