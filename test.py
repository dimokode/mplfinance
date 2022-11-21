from dataController import dataController
import pandas as pd
import json
import datetime as dt
import mplfinance as mpf
import numpy as np



dc = dataController("btcusdt", "1d")
imageFilename = dc.getProp('imageFilename')
rawData = dc.readDataFromFile()
#rawData = dc.getDataFromBinance()
#dc.saveDataInFile(rawData)

jsonData = json.loads(rawData)
df = pd.DataFrame(jsonData)

df.columns = ['open_time',
            'Open', 'High', 'Low', 'Close', 'Volume',
            'close_time', 'qav', 'num_trades',
            'taker_base_vol', 'taker_quote_vol', 'ignore']
#df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.close_time]
#df['Date'] = [dt.datetime.fromtimestamp(x/1000.0) for x in df.close_time]
data = df[['open_time', 'Open', 'High', 'Low', 'Close', 'Volume']]
data = data.rename(columns={'open_time':'Date'})

data['Date'] = data['Date'].map(lambda v: dt.date.fromtimestamp(v/1000.0))
#dat.set_index('Date')
data.index = pd.DatetimeIndex(data['Date'])
data['Open'] = data['Open'].astype('float')
data['High'] = data['High'].astype('float')
data['Low'] = data['Low'].astype('float')
data['Close'] = data['Close'].astype('float')
data['Volume'] = data['Volume'].astype('float')
data.pop('Date') #remove column

data['MA20'] = data['Close'].rolling(20).mean()
data['MA50'] = data['Close'].rolling(50).mean()
data = data.dropna()
#print(dat)

print(data.tail())


buy_signals = []
sell_signals = []

for i in range(len(data)):
    if (data['MA20'].iloc[i] > data['MA50'].iloc[i]) and (data['MA20'].iloc[i-1] < data['MA50'].iloc[i-1]):
        buy_signals.append(data.iloc[i]['Close'] * 0.98)
    else:
        buy_signals.append(np.nan)
    
    if (data['MA20'].iloc[i] < data['MA50'].iloc[i]) and (data['MA20'].iloc[i-1] > data['MA50'].iloc[i-1]):
        sell_signals.append(data.iloc[i]['Close'] * 1.02)
    else:
        sell_signals.append(np.nan)

buy_markers = mpf.make_addplot(buy_signals, type='scatter', markersize=120, marker='^')
sell_markers = mpf.make_addplot(sell_signals, type='scatter', markersize=120, marker='v')
apds = [buy_markers, sell_markers]


mpf.plot(data, type='candle', mav=[20, 50], volume=True, addplot=apds, savefig=imageFilename)
#mpf.savefig(imageFilename)
