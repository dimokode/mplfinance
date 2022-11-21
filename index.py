import pandas as pd
import json
import datetime as dt
import matplotlib.pyplot as plt
from dataController import dataController




try:
    dc = dataController("btcusdt", "1h")
    imageFilename = dc.getProp('imageFilename')

    def get_bars():

        

        #data = dc.getDataFromBinance()

        #dc.saveDataInFile(data)

        data = dc.readDataFromFile()
        jsonData = json.loads(data)
        df = pd.DataFrame(jsonData)
        df.columns = ['open_time',
                    'o', 'h', 'l', 'c', 'v',
                    'close_time', 'qav', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore']
        df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.close_time]
        return df
    
    btcusdt = get_bars()
    #print(btcusdt.head())
    
    #btcusdt.plot(figsize=(16,9))
    #print(btcusdt.index)
    #plt.plot(btcusdt['close_time'].astype('float'), btcusdt['c'].astype('float') )
    
    """
    #two charts one under another
    fig, ax = plt.subplots(2, 1, sharex=True)
    ax[0].plot(btcusdt.index, btcusdt['c'].astype('float'), color="tab:red")
    ax[1].bar(btcusdt.index, btcusdt['taker_base_vol'].astype('float'))
    """
    """
    fig, ax = plt.subplots(1, 1)
    ax.plot(btcusdt.index, btcusdt['c'].astype('float'), color="tab:red")
    ax.bar(btcusdt.index, btcusdt['taker_base_vol'].astype('float'))
    """

    fig, ax1 = plt.subplots()
    ax1.plot(btcusdt.index, btcusdt['c'].astype('float'), color="tab:red")
    ax2 = ax1.twinx()
    
    ax2.margins(0.99)
    ax2.set_ylim(0, 200000)
    ax2.bar(btcusdt.index, btcusdt['taker_base_vol'].astype('float'))
    #plt.plot(btcusdt.index, btcusdt['c'].astype('float'), btcusdt['taker_base_vol'].astype('float'))
    plt.show()
    #plt.savefig(imageFilename)
    #btcusdt["c"].plot()
except Exception as e:
    print(e)
