import os
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

df = pd.read_csv(os.path.join("dataset", "OnlineNewsPopularity.csv"))
train, test = train_test_split(df, test_size=0.2)

train_features = train[train.columns[1:-1]]
train_target = train[train.columns[-1]]

test_features = test[test.columns[1:-1]]
test_target_actual = test[test.columns[-1]]

regr = LinearRegression()
regr.fit(train_features, train_target)

print 'Coefficients: \n', regr.coef_
print "Residual sum of squares: %.2f" % np.mean((regr.predict(test_features) - test_target_actual) ** 2)
