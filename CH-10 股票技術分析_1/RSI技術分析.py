import datetime
from talib import abstract
import yfinance as yf
import matplotlib.pyplot as plt
#RSI 又稱為 相對強弱指標
#RSI 是以某段時間，股價「平均漲幅」與「平均跌幅」所計算出來的數值
#RSI 是一個大小介在 0 ~ 100 的數值，越高代表市場越熱，越小代表越冷
#RSI 公式： （一定時間內）漲幅平均值 ÷〔 （一定時間內）漲幅平均值 ＋（一定時間內）日跌幅平均值 〕× 100

#中文設定
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

''' RSI 技術分析 '''

#設定爬蟲時間
start = datetime.datetime.now() -datetime.timedelta(days=180)
end  = datetime.date.today()

#設定股票代號
sid = '2330'
#取得資料
stock_yf = yf.download(sid+'.Tw', start, end)
print(stock_yf.tail(10))

stock_yf.rename(columns = {'Open':'open','High':'high','Low':'low','Close':'close'},inplace=True)


stock_yf['close'].plot(figsize=(16,8), label='2330')

output = abstract.RSI(stock_yf)
output.plot(secondary_y=True,figsize=(16,8), label='RSI')


#顯示側標['RSI指數','2330']
plt.legend(['RSI指數','2330'],loc='upper left', shadow=False, fontsize='x-large')
plt.ylabel('(百分比%)')

#顯示標題
plt.title(sid+'-台積電'+'RSI指標')

plt.grid(linestyle='dotted')
plt.show()