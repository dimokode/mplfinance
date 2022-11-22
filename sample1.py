import mplfinance as mpf
import pandas as pd
import datetime as dt
import pandas_datareader as pdr

#now = dt.datetime.now()
#start = now - dt.timedelta(60)

stock = "^GSPC" #S&P500
stock = "BTC-USD" #S&P500
filename = stock.lower()+'.png'

#df = pdr.get_data_yahoo(stock, start , now)
df = pdr.get_data_yahoo(stock, "2020-01-01" , "2022-11-21")
print(df.head())
#mpf.plot(df,type='candle',style='yahoo',savefig=filename)
mpf.plot(df, type='candle',style='yahoo', volume=True)