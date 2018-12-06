import pandas as pd
import quandl
import math
import numpy as np
import datetime
# to plot stuff
import matplotlib.pyplot as plt
import pickle

# to make it look decent
from matplotlib import style
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import psycopg2


connection = psycopg2.connect(user= "postgres",
    password= "bethebest1",
    database= "sumbal",
    host= "206.189.44.45",
    port= "5432")

cursor = connection.cursor()
cursor.execute("""SELECT * FROM public.position """)
data = cursor.fetchall()
print(data)

print(len(data))

features = np.array(data)[:, [0, 1]]
label = np.array(data)[:, [4]]

print(features, label)
#features = preprocessing.scale(features)

X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=42)

# select classifier
clf = LinearRegression()
#clf = svm.SVR()
clf.fit(X_train, y_train)

# wola we have accuracy
accuracy = clf.score(X_test, y_test)
print(accuracy)

print(clf.predict(np.array([[11,8]])))

# closing database connection.
if (connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")

# decent style
style.use('ggplot')
