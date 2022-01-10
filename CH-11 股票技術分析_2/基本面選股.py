import requests as rq
import csv
import pandas as pd

url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_ALL?response=open_data'
r = rq.request('GET',url)
data = list(csv.reader(r.text.split('\n'),delimiter=',')) 
#print(*data,sep=' ', end=",")

df = pd.DataFrame(data[1:], columns=['股票代號', '股票名稱', '本益比', '殖利率(%)', '股價淨值比'])
df = df.dropna() #找到DataFrame類型數據的空值（缺失值）
df['本益比'] = df['本益比'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['本益比'] = df['本益比'].astype(float)
df['殖利率(%)'] = df['殖利率(%)'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['殖利率(%)'] = df['殖利率(%)'].astype(float)


df1 = df['本益比'] >= 0.1
df2 = df['本益比'] <= 8
df3 = df['殖利率(%)'] >= 8.0
A = df[df1 & df2 & df3]
print(A)