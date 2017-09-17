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

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(X_train[['EmptyRaids', 'SuccRaids','TotalRaids','UnSuccRaids']],Y_train.values.ravel())

# Checking the performance of our model on the testing data set
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,clf.predict(X_test[['EmptyRaids', 'SuccRaids','TotalRaids','UnSuccRaids']])))
