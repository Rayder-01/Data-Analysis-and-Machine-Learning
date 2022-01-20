import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split

titanic = pd.read_csv(r'CH-15 ML_分類\titanic.csv')
titanic['SexCode'] = titanic['sex'].map({'female':0,'male':1}).astype(int)

X = pd.DataFrame([titanic['fare'],titanic['SexCode'], titanic['pclass']]).T
y = titanic['survived']

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33, random_state=1)

#執行迴圈找出最佳 max_depth 階層
# i = 1
# while i <=20:
#         dtree = tree.DecisionTreeClassifier(max_depth=i)
#         dtree.fit(XTrain, yTrain)
#         print("準確度",dtree.score(XTest,yTest))
#         i = i + 1


dtree = tree.DecisionTreeClassifier(max_depth=18)
dtree.fit(XTrain, yTrain)
print("準確度",dtree.score(XTest,yTest))
# print(dtree.predict(XTest))
# print(yTest.values)