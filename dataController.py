#import json
import requests
import re

class dataController:
    #https://api.binance.com/api/v1/klines?symbol=STEEMETH&interval=1h

    def __init__(self, symbol, interval) -> None:
        

        try:
            symbol = symbol.upper()


            result = re.match(r"^[A-Z0-9-_.]{1,20}$", symbol)
            #print(result)
            if(result == None):
            #if re.match(r"^[A-Z0-9-_.]{1,20}$", symbol) == False:
                raise Exception("Symbol isn't match")

            self.symbol = symbol
            self.interval = interval
            self.filename = f"{symbol}_{interval}.txt"
            self.imageFilename = f"{symbol}_{interval}.png"
        except Exception as e:
            #print(e)
            raise e

    
    def getProp(self, propName):
        return self.__dict__[propName]


    def getDataFromBinance(self):
        try:
            url = f"https://api.binance.com/api/v1/klines?symbol={self.symbol}&interval={self.interval}"
            return requests.get(url).text
        except Exception as e:
            print(e)

    

    def saveDataInFile(self, data):
        try:
            f = open(self.filename, 'w')
            f.write(data)
            f.close()
        except Exception as e:
            print(e)


    def readDataFromFile(self):
        try:
            f = open(self.filename, 'r')
            data = f.read()
            f.close()
            return data
        except FileNotFoundError as e:
            print(f"File {self.filename} wasn't found")
        except Exception as e:
            print(e)


    def convertDataToCSV(self, data):
        print(data)
