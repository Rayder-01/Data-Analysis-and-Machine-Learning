import datetime
import matplotlib.pyplot as mat
import yfinance as yf

#//  股市趨勢圖  //

#中文設定
mat.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
mat.rcParams['axes.unicode_minus'] = False

#設定爬蟲時間
start = datetime.datetime.now() - datetime.timedelta(days=360)
end = datetime.date.today()

#設定爬蟲股票代號
sid = '2330'
#把資料放進本機
yf.pdr_override()

#取得股票資料
stock_yf = yf.download(sid+'.TW', start, end)
print(stock_yf.tail(10))

#線型圖，收盤價，5日平均、20日平均、60日平均
stock_yf['Adj Close'].plot(figsize=(16,8))
stock_yf['Adj Close'].rolling(window=5).mean().plot(figsize=(16,8), label = '5_Day_Mean(周)')
stock_yf['Adj Close'].rolling(window=20).mean().plot(figsize=(16,8), label = '20_Day_Mean(月)')
stock_yf['Adj Close'].rolling(window=60).mean().plot(figsize=(16,8), label = '60_Day_Mean(季)')
stock_yf['Adj Close'].rolling(window=120).mean().plot(figsize=(16,8), label = '120_Day_Mean(半年)')
#顯示側標
mat.legend(loc='upper left',shadow=True, fontsize='6')

#顯示標題
mat.title(sid+'台積電-年度股市趨勢圖')

mat.show()

