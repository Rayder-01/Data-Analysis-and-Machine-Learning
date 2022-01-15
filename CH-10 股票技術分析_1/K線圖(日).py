import datetime
import pandas as pd

import mplfinance as mpl

import yfinance as yf

#設定爬蟲時間
start = datetime.datetime.now() - datetime.timedelta(days=90)
end = datetime.date.today()

#設定爬蟲股票代號
sid = '2324'  

#取得股票資料
stock_yf = yf.download(sid+'.TW', start, end)
print(stock_yf.tail(10))

# ==============================  K線圖  ======================================
df = pd.DataFrame(stock_yf)
df.index.name = 'Date'

mpl.plot(df, type='candle', style='charles',
        title='',
        ylabel='',
        ylabel_lower='',
        volume=True,
        figscale=1.5,
        mav=(5,20),  
        figratio =(12,6)
        )

mpl.show()