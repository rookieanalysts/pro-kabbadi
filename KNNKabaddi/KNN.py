# Importing pandas
import pandas as pd
# Importing training data set
X_train=pd.read_csv('X_train.csv')
Y_train=pd.read_csv('Y_train.csv')
# Importing testing data set
X_test=pd.read_csv('X_test.csv')
Y_test=pd.read_csv('Y_test.csv')

#print (X_train.head())

import matplotlib.pyplot as plt
X_train[X_train.dtypes[(X_train.dtypes=="float64")|(X_train.dtypes=="int64")]
                        .index.values].hist(figsize=[11,11])

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train[['SuccRaids']],Y_train.values.ravel())
# Checking the performance of our model on the testing data set
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,knn.predict(X_test[['SuccRaids']]))*100,"%")
#Above 100 multiply because for we need accuracy in percentage...
