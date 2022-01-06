import numpy as np

# arange([start],[stop],[dtype])
x1 = np.arange(1,6,1)

x2 = np.arange(0,5,1)
x3 = x2.reshape(5,1)
A = x3 + x1

print(A)


y1 = np.arange(9,4,-1)

y2 = np.arange(0,5,1)
y3 = y2.reshape(5,1)
B = y1 - y3
print(B)

C = B+A
print("C :")
print(C)

print('資料型態:%s' %type(C))
print('平均值:%s' %np.mean(C))
print('中位數:%s' %np.median(C))
print('標準差:%s' %np.std(C))
print('變異數:%s' %np.var(C))
print('極差值:%s' %np.ptp(C))