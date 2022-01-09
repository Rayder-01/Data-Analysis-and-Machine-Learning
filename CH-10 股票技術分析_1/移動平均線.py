import datetime
import pandas as pd
from talib import abstract
import yfinance as yf
import matplotlib.pyplot as plt

#移動平均(Moving Average)簡稱「均線」
#60日均線又稱為生命線(均線)
#分析概念為低於季線較有機會買在低點

#中文設定
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

#設定爬蟲時間
start = datetime.datetime.now() - datetime.timedelta(days=720)  # timedelta 使用運算子來算出時間變化
end = datetime.date.today()

#設定股票代號
sid = '2330'
#取得股票資料 API
stock_yf = yf.download(sid+'.Tw',start,end)
print(stock_yf.tail(10))

stock_yf.rename(columns = {'Open':'open','High':'high','Low':'low','Close':'close'},inplace=True)

# 技術分析
stock_yf['MA20'] = abstract.MA(stock_yf['close'],timeperiod=20)
stock_yf['MA60'] = abstract.MA(stock_yf['close'],timeperiod=60)

stock_yf['close'].plot(figsize=(16,8),label='2330')
stock_yf['MA60'].plot(secondary_y=True, figsize=(16, 8), label='MA60')
stock_yf['MA20'].plot(secondary_y=True, figsize=(16, 8), label='MA20')



#顯示側標
plt.legend(loc='upper left', shadow=False, fontsize='x-large')

#顯示標題
plt.title('台積電'+sid+'均線趨勢圖')

print(stock_yf.tail(10))
plt.show()