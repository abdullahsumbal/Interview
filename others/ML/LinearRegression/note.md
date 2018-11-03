# Linear Regression


Linear is like solving for line equation. y = mx + c  

here x is the features and y is the label.

There can be a multiple features. And feature can be preprocessed to be between 0 and 1 and it can help in prediction.

Coefficient of determination: is the percentage of error calculated by distance between best fit line and points.   

```
# separate the data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# select classifier
clf = LinearRegression()
#clf = svm.SVR()
clf.fit(X_train, y_train)

```
