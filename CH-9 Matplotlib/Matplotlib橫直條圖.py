import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

table = pd.read_csv('Bank_ranking.csv', encoding= 'BIG5',sep=',')
print(table)

x = np.arange(1,14,1)
y = table['資產總額-新台幣百萬元']
index = table['銀行別']
#Bank_ranking

#設定畫布大小
plt.figure(figsize=(16,6))

#設定圖表類型及相關設定
plt.tick_params(axis='x', labelsize= 6)

#Axes.set_xscale(value, **kwargs)
#value{"linear", "log", "symlog", "logit", ...} or

plt.barh(x,y,  tick_label = index, label = "資產總額-新台幣百萬元")
plt.legend()
plt.xlabel("資產總額-單位兆")
plt.ylabel("銀行名稱")
plt.title("Matplotlib直條圖練習")

plt.show()