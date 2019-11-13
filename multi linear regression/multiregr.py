#MULTIPLE LINEAR REGRESSION
import pandas as pd
import numpy as np

dataset=pd.read_csv("50_Startups.csv")

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
X[:, 3] = labelencoder_x.fit_transform(X[:,3]) 
onehotencoder = OneHotEncoder(categorical_features= [3])
X = onehotencoder.fit_transform(X).toarray()

X = X[:,1:]

from sklearn.cross_validation import train_test_split
X_train, X_test,y_train,t_test = train_test_split(X, y, test_size=0.2)

#fitting the data using multiple regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
y_predict = regressor.predict(X_test)

"""in this part we will try to find the optimal sol using min no of independent var. reducing the no of var 
should not negatively affect the sol but should remove un wanted var without which also the model would 
return excellent results each independent var cab ahve an affect in the model,it maybe +ve or -ve

we know that the eq for multiple regression is y= b0+b1x1+....
but normlly the b0 constant is not considered in the the test/training set as there is no extra col for this var 
so whta we do is add another col in the datset that consists of all 1s and when multipied with b0 will give b0 as
result, hence b0 would also be included
"""

X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis = 1) #adds a column of 1s in X 
#backward elimination
import statsmodels.formula.api as sm
X_opt = X[:, [0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt ).fit()
regressor_OLS.summary()
X_opt = X[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X[:,[0,3,4,5]]
regressor_OLS = sm.OLS( endog = y, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X[:, [0,3,5]]
regressor_OLS = sm.OLS( endog = y, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X[:, [0,3]]
regressor_OLS = sm.OLS(endog = y, exog= X_opt).fit()
regressor_OLS.summary()

y_predict = regressor_OLS.predict(X_test)
