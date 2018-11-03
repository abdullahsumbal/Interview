import pandas as pd
import quandl
import math
import numpy as np
import datetime
# to plot stuff
import matplotlib.pyplot as plt

# to make it look decent
from matplotlib import style
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# decent style
style.use('ggplot')

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
forecast_out = int(math.ceil(0.1*len(df)))
print(forecast_out)

# predict column is called label
df['label'] = df[forecast_col].shift(-forecast_out)
# so now we got XXXXX features and Y label
x = np.array(df.drop(['label'], 1))

# scale the data for accuracy
x = preprocessing.scale(x)

# this new data with no future value
x_lately = x[-forecast_out:]

# we know the y values for this
x = x[:-forecast_out:]

# drop nas
df.dropna(inplace=True)

y = np.array(df['label'])

print(df.tail())
# separate the data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# select classifier
clf = LinearRegression()
#clf = svm.SVR()
clf.fit(X_train, y_train)

# wola we have accuracy
accuracy = clf.score(X_test, y_test)

# making prediction with the unknown
forecast_set = clf.predict(x_lately)


df['Forecast'] = np.nan
print(df.head())

# time stuff for graph
last_date = df.iloc[-1].name

last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day


# putting dates for the new forecast values
for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

print(df.tail())
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.xlabel('Date')
plt.ylabel('Price')
# plt.show()


