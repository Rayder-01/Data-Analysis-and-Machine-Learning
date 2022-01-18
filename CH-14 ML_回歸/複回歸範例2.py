import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


boston = datasets.load_boston()

X = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=["MEDV"])
y = target["MEDV"]

lm = LinearRegression()
lm.fit(X,y)

print("迴歸係數:", lm.coef_)
print("截距:", lm.intercept_)

#建立一個物件來查詢每個特徵的係數
coef = pd.DataFrame(boston.feature_names, columns=["Features"])
coef["迴歸係數"] = lm.coef_
print(coef)

# 繪圖:價格與RM的關係分布
# plt.scatter(X.RM,y)
# plt.xlabel("Average numbwer of  room per dwelling(RM)")
# plt.ylabel("Housing Price(MEDV)")
# plt.title("Relationship between RW and Price")
# plt.show()

#建立一個預測物件
predicted_price = lm.predict(X)
print(predicted_price[0:5])

# 繪圖: 預測價格
plt.scatter(y,predicted_price)
plt.xlabel("Price")
plt.ylabel("Predicted Price")
plt.title("Price vs Predicted Price")
plt.show()

#查詢資料個說明
# print(boston.DESCR)
# print(boston.keys())
# print(boston.data.shape)
# print(boston.feature_names)
# print(X.head)

# target = pd.DataFrame(boston.target, columns=["E"])
# print(boston.target)