import datetime
import pandas as pd
from talib import abstract
import yfinance as yf
import matplotlib.pyplot as plt

#移動平均(Moving Average)簡稱「均線」
#20日、60日均線又稱為生命線(月線、季線)
#低於季線較有機會買在低點
#公式:加總 N 天的收盤價再除以 N，得到第 N 天的算術平均線數值。

#中文設定
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

#設定爬蟲時間
start = datetime.datetime.now() - datetime.timedelta(days=360)  # timedelta 使用運算子來算出時間變化
end = datetime.date.today()

#設定股票代號
sid = '2330'
#設定均線
MA_1 = 'MA5'
MA_2 = 'MA60'
#取得股票資料 API
stock_yf = yf.download(sid+'.Tw',start,end)
print(stock_yf.tail(10))

stock_yf.rename(columns = {'Open':'open','High':'high','Low':'low','Close':'close'},inplace=True)

# 技術分析
stock_yf[MA_1] = abstract.MA(stock_yf['close'],timeperiod=5) # MA_1 
stock_yf[MA_2] = abstract.MA(stock_yf['close'],timeperiod=60) # MA_2

stock_yf['close'].plot(figsize=(16,8),label='2330')
stock_yf[MA_1].plot(secondary_y=True, figsize=(16, 8), label=MA_1)
stock_yf[MA_2].plot(secondary_y=True, figsize=(16, 8), label=MA_2)

#顯示側標
plt.legend([MA_1,MA_2],loc='upper left', shadow=False, fontsize='x-large')
plt.ylabel('(MA收盤價)')

#顯示標題
plt.title('台積電'+sid+'均線趨勢圖')

print(stock_yf.tail(10))


plt.grid(linestyle='dotted')
plt.show()