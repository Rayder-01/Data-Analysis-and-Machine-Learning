from types import prepare_class
import numpy as np
import pandas as pd
from sklearn.base import RegressorMixin
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

temperatures = np.array([29, 28, 34, 31,
                         25, 29, 32, 31,
                         24, 33, 25, 31,
                         26, 30])
drink_sales = np.array([7.7, 6.2, 9.3, 8.4,
                        5.9, 6.4, 8.0, 7.5,
                        5.8, 9.1, 5.1, 7.3,
                        6.5, 8.4])

X = pd.DataFrame(temperatures, columns=["Temperature"])
taget = pd.DataFrame(drink_sales, columns=["Drink_sales"])
y = taget["Drink_sales"]

lm = LinearRegression()
X = X.values
lm.fit(X, y)
print("迴歸係數 :", lm.coef_)
print("截距 :", lm.intercept_)

#預測氣溫26, 30度的業績
new_temperatures = pd.DataFrame(np.array([26,30]))
predicted_sales = lm.predict(new_temperatures)
print('預測氣溫26, 30度的業績 :')
print(predicted_sales)

# plt.scatter(temperatures,drink_sales)
# Regression_sales = lm.predict(X)
# plt.plot(temperatures, Regression_sales, color="blue")
# plt.plot(new_temperatures, prepare_sales, color="red", marker="0", markersize=10)

#使用 Sklearn LinearRegression
# 線性回歸簡單來說，就是將複雜的資料數據，擬和至一條直線上，就能方便預測未來的資料。接下來我們一樣使用房價預測資料集，並使用 Sklearn 提供的 LinearRegression 來求解。

# Parameters:

# fit_intercept: 是否有截距，如果沒有則直線過原點。

# Attributes:

# coef_: 取得係數。
# intercept_: 取得截距。

# Methods:

# fit: 放入X、y進行模型擬合。
# predict: 預測並回傳預測類別。
# score: R2 score 模型評估。