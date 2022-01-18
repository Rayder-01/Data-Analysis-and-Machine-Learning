import pandas as pd
import numpy as np
from sklearn import linear_model

#注意讀寫與路徑常發生的錯誤
titanic = pd.read_csv(r'CH-15 ML_分類\titanic.csv')
titanic['SexCode'] = titanic['sex'].map({'female':0,'male':1}).astype(int)
print(titanic.info())

X = pd.DataFrame([titanic['pclass'],titanic['SexCode'], titanic['age']]).T
y = titanic['survived']

logistic = linear_model.LogisticRegression(penalty='l2', solver='lbfgs')
logistic.fit(X,y)
print("迴歸係數:", logistic.coef_)
print("截距:", logistic.intercept_)

preds = logistic.predict(X)
print(pd.crosstab(preds, titanic['survived']))
print("準確率:",logistic.score(X,y))