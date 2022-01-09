import datetime
from talib import abstract
import yfinance as yf
import matplotlib.pyplot as plt

#設定爬蟲時間
start = datetime.datetime.now() -datetime.timedelta(days=360)
end  = datetime.date.today()

#設定股票代號
sid = '2330'
#取得資料
stock_yf = yf.download(sid+'.Tw', start, end)
print(stock_yf.tail(10))

stock_yf.rename(columns = {'Open':'open','High':'high','Low':'low','Close':'close'},inplace=True)