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


#======================= KD指標 =============================
# == K值 ==
# K 值為「快速平均值」，又稱快線。以公式來看就知道，
# 今天的 K 值是把昨天的 K 值和今天的 RSV 加權平均的結果，所以對股價變化的反應較靈敏、快速。

# == D值 ==
# D 值為「慢速平均值」，又稱慢線。以公式來看就知道，今天的 D 值是把昨天 D 值和今天的 K 值再加權平均一次的結果，
# 經過兩次平均後，今天股價對 D 值的影響就比較小，所以 D值對股價變化的反應較不靈敏

# == K、D值的關係 ==
# K 值 > D 值：上漲行情，適合做多
# D 值 > K 值：下跌行情，適合空手或做空
#========================================
# KD 黃金交叉：建議買進
# 當 K 值 由下往上 突破 D 值，建議買進做多

# KD 死亡交叉：建議賣出
# 當 K 值 由上往下 跌破 D 值時，建議賣出做空
#========================================
# D > 80：超買區
# 當 D 值 > 80，為高檔超買訊號，代表多頭強勢，市場過熱，
# 隨時可能回檔或下跌，但還要注意反轉，所以建議等出現死亡交叉後再賣出。

# D < 20：超賣區
# 當 D 值 < 20，為低檔超賣訊號，代表空頭強勢，市場過冷，
# 隨時可能反彈或回升，但需考慮鈍化問題，所以建議等出現黃金交叉後再買進。

stock_yf.rename(columns = {'Open':'open','High':'high','Low':'low','Close':'close'},inplace=True)
KDvalue = abstract.STOCH(stock_yf)
print(KDvalue.tail(10))

plt.figure(figsize=(16,8))
plt.plot(stock_yf['close'], label='2330')
plt.plot(KDvalue['slowk'], 'r', alpha=0.5, label='K')
plt.plot(KDvalue['slowd'], 'g', alpha=0.5, label='D')

#側標
plt.legend(loc='upper left',shadow=False, fontsize='x-large')
#標題
plt.title(sid+'台積電'+'-KD指數')
plt.grid(linestyle='dotted')
plt.show()
