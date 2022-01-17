import pandas as pd
from sklearn import datasets

boston = datasets.load_boston()

X = pd.DataFrame(boston.data, columns=boston.feature_names)
print(boston.DESCR)
print(boston.keys())
print(boston.data.shape)
print(boston.feature_names)
print(X.head)

#target = pd.DataFrame(boston.target, columns=["E"])
print(boston.target)