# implementing my now linear regression

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

# styling bitches
style.use('fivethirtyeight')

def create_datatest(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val +  random.randrange(-variance, variance)
        ys.append(y)
        if(correlation and correlation == 'pos'):
            val+=step
        elif(correlation and correlation == 'neg'):
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

def best_fit_slope_intercept(xs, ys):

    m = ((  ( mean(xs)*mean(ys) ) - (mean(xs*ys))  ) /
         ( (mean(xs))**2 - mean(xs**2) )
         )
    b = mean(ys) - m*mean(xs)

    # that is the model of our system
    print(m, b)
    return m, b

def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig)**2)


def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regression = squared_error(ys, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regression / squared_error_y_mean)


xs, ys = create_datatest(40, 80, 2, correlation=False)
m, b = best_fit_slope_intercept(xs, ys)

regression_line = [(m*x) + b for x in xs]
se = squared_error(ys, regression_line)

predict_x = 8
predict_y = m*predict_x + b
r_square = coefficient_of_determination(ys, regression_line)

print(r_square )
plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y)
plt.plot(xs, regression_line)
plt.show()