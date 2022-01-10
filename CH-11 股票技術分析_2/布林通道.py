import datetime
from talib import abstract
import yfinance as yf
import matplotlib.pyplot as plt

#中文設定
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

#設定爬蟲時間
start = datetime.datetime.now() -datetime.timedelta(days=360)
end  = datetime.date.today()

#設定股票代號
sid = '2330'
#取得資料
stock_yf = yf.download(sid+'.Tw', start, end)
print(stock_yf.tail(10))

#=============== 布林通道 =================
# 中軌道 = 平均成本
# 上軌 = 股價的壓力線
# 下軌 = 股價的支撐線

# =====多頭訊號=====
# 價格由下向上，穿越下軌線時是買進訊號。

# 價格由下向上，穿越中間線時股價可能加速向上，是加碼買進訊號。

# 價格在中間線與上軌線之間，波動為多頭市場，可做多

# =====空頭訊號=====
# 價格在中間線與上軌線間，由上往下跌破中間線，為賣出訊號。

# 價格在中間線與下軌線間，向下波動時為空頭市場，可做空。

#定義欄位
stock_yf.rename(columns = {'Open':'open','High':'high','Low':'low','Close':'close'},inplace=True)
BBAVD = abstract.BBANDS(stock_yf,timeperiod=20)

plt.figure(figsize=(16,8))
plt.plot(stock_yf['close'],label='2330')
plt.plot(BBAVD['middleband'],'r',alpha=0.5,label='上軌')
plt.plot(BBAVD['upperband'],'g',alpha=0.5,label='中軌')
plt.plot(BBAVD['lowerband'],'y',alpha=0.5,label='下軌')

#側標
plt.legend(loc='upper left',shadow=False, fontsize='x-large')
#標題
plt.title(sid+'台積電'+'-布林通道')

plt.show()