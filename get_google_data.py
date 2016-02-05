import urllib.request
import datetime as dt
import pandas as pd

def get_google_data(symbol, period, window, exch = 'NYSE'):
    url_root = 'http://www.google.com/finance/getprices?i='
    url_root += str(period) + '&p=' + str(window)
    url_root += 'd&f=d,o,h,l,c,v&df=cpct&x=' + exch.upper() + '&q=' + symbol.upper()
    response = urllib.request.urlopen(url_root)
    data=response.read().decode().split('\n')            #decode() required for Python 3
    data=pd.DataFrame([data[i].split(',') for i in range(len(data)-1)])
    anchor_stamp=dt.datetime.fromtimestamp(int(data.ix[7,0][1:]))
    df=data.drop(range(7))
    df.index = pd.date_range(start = anchor_stamp,
                             periods = len(data)-7, 
                             freq = str(int(period/60)) + 'min')
    df = df.drop(0, axis =1)
    df.columns = ['Open', 'Hi', 'Lo', 'Close', 'Volume']
    
    return df
