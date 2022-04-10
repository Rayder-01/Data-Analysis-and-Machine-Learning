from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

#中文設定
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

iris = load_iris()

X = iris.data
X = X[:,2:]
y = iris.target

XTrain, XTest, yTrain, yTest =  train_test_split(X,y,test_size=0.2,random_state=1)

plt.scatter(XTrain[:,0],XTrain[:,1], c=yTrain)

# print(XTrain[:,0])   取全部二維資料的第0項 也就是第一行
# print(XTrain[:])     取全部二維資料

# 支援向量機(SVM) 是一個監督學習演算法

clf = SVC()
clf.fit(XTrain,yTrain)

y_predict = clf.predict(XTest)
print(y_predict)
plt.scatter(XTest[:,0],XTest[:,1], c=y_predict)
plt.show()

print("準確率:",clf.score(XTest,yTest))
x1, x2 = np.meshgrid(np.arange(0,7,0.02), np.arange(0,3,0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
Z = Z.reshape(x1.shape)
plt.contourf(x1, x2, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(X[:,0], X[:,1], c=y)
plt.title("鳶尾花-SVM的分類切割線")
plt.show()

