
#using avergae voting for increasing the accuracy of the model

#importing libraries
import pandas as pd

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


#logistic regression
from sklearn.linear_model import LogisticRegression
lr =LogisticRegression()
lr.fit(X_train,y_train)

#USING KERNEL SUPPORT VECTOR MACHINE TO TRAIN THE MODEL
from sklearn.svm import SVC
SVM = SVC(kernel ="rbf",random_state =0 )
SVM.fit(X_train,y_train)

#decision tree
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
dt.fit(X_train, y_train)

#random forest
from sklearn.ensemble import RandomForestClassifier
rt = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
rt.fit(X_train, y_train)

#USING NEAREST NEIGHBOUR ALGORITHM TO TRAIN THE MODEL
from sklearn.neighbors import KNeighborsClassifier
nn = KNeighborsClassifier(n_neighbors =5, metric="minkowski", p=2)
nn.fit(X_train,y_train)

lr.score(X_test,y_test)
SVM.score(X_test,y_test)
dt.score(X_test,y_test)
rt.score(X_test,y_test)
nn.score(X_test,y_test)

from sklearn.ensemble import VotingClassifier
vc = VotingClassifier(estimators=[('lr',lr),('dt',dt),('SVM',SVM)],voting='hard')
vc.fit(X_train,y_train)
vc.score(X_test,y_test)