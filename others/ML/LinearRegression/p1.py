import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = quandl.get('WIKI/GOOGL')
print(type(df))

df = df[['Adj. Open', 'Adj. High','Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'PCT_change', 'HL_PCT', 'Adj. Volume']]

# column to predict
forecast_col = 'Adj. Close'

# fill column with -99999. i have no idea why we did that
df.fillna(-99999, inplace=True)


# number days to predict
forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out)

# predict column is called label
df['label'] = df[forecast_col].shift(-forecast_out)
# so now we got XXXXX features and Y label
df.dropna(inplace=True)
x = np.array(df.drop(['label'], 1))
y = np.array(df['label'])
x = preprocessing.scale(x)

# separate the data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# select classifier
clf = LinearRegression()
#clf = svm.SVR()
clf.fit(X_train, y_train)

# wola we have accuracy
accuracy = clf.score(X_test, y_test)

print(accuracy)

