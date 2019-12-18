#SUPPORT VECTOR REGRESSION(NON-LINEAR MODEL)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("Position_Salaries.csv")

X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

plt.scatter(X,y)
plt.show()

from sklearn.preprocessing import StandardScaler
X_sc = StandardScaler()
y_sc = StandardScaler()
X = X_sc.fit_transform(X)
y = y_sc.fit_transform(y)

from sklearn.svm import SVR
support_vector_regressor = SVR()
support_vector_regressor.fit(X,y)


y_predict = y_sc.inverse_transform(support_vector_regressor.predict(X_sc.transform(np.array(6.5))))

plt.scatter(X,y)
plt.plot(X,y_predict,color="blue")
plt.show()
