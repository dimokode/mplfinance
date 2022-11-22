import matplotlib.pyplot as plt
import mplfinance as mpf
import yfinance as yf

tickers = ['AAPL','GOOG','TSLA']
data = yf.download(tickers, start="2021-01-01", end="2021-03-01", group_by='ticker')

aapl = data[('AAPL',)]
goog = data[('GOOG',)]
tsla = data[('TSLA',)]

fig = mpf.figure(style='yahoo', figsize=(12,9))
#fig.subplots_adjust(hspace=0.3)
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

mpf.plot(aapl, type='line', ax=ax1, axtitle='AAPL', xrotation=0)
mpf.plot(goog, type='line', ax=ax2, axtitle='GOOG', xrotation=0)
mpf.plot(tsla, type='line', ax=ax3, axtitle='TSLA', xrotation=0)
ax1.set_xticklabels([])
ax2.set_xticklabels([])

N = len(tickers)
fig, axes = plt.subplots(N, figsize=(20, 5*N), sharex=True)

for df,t,ax in zip([aapl,goog,tsla], tickers, axes):
    mpf.plot(df, ax=ax, axtitle=t, type='line', show_nontrading=True)# volume=True 