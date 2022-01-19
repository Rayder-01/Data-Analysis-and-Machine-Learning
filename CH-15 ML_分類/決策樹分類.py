import pandas as pd
from sklearn import tree
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

#查詢資料
print(iris.keys())
# print(iris['DESCR'])
print(iris.feature_names)

X = pd.DataFrame(iris.data, columns=iris.feature_names)
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33, random_state=1)

dTree = tree.DecisionTreeClassifier(max_depth=8)
dTree.fit(XTrain, yTrain)
print("準確率:",dTree.score(XTest,yTest))
print(dTree.predict(XTest))
print(yTest.values)