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

#線型圖，收盤價，5日平均、20日平均、60日平均 ,
#Adjusted close 簡單來說,就是調整價格能更好的反應出股票實際的價格，
#因為收盤價本身可能不能完全反應股票的價值，比如現金分紅，股票分紅，股票分割。
stock_yf['Adj Close'].plot(figsize=(16,8),label = sid)
stock_yf['Adj Close'].rolling(window=5).mean().plot(figsize=(16,8), label = '5日均線(周)')
stock_yf['Adj Close'].rolling(window=20).mean().plot(figsize=(16,8), label = '20日均線(月)')
stock_yf['Adj Close'].rolling(window=60).mean().plot(figsize=(16,8), label = '60日均線(季)')
stock_yf['Adj Close'].rolling(window=120).mean().plot(figsize=(16,8), label = '120日均線(半年)')
#顯示側標
mat.legend(loc='upper left',shadow=True, fontsize='6')

#顯示標題
mat.title(sid+'台積電-年度股市趨勢圖')

mat.show()

