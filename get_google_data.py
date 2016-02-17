import urllib.request
import datetime as dt
import pandas as pd

def get_google_data(symbol, period, window, exch = 'NYSE'):
    url_root = ('http://www.google.com/finance/getprices?i='
                + str(period) + '&p=' + str(window)
                + 'd&f=d,o,h,l,c,v&df=cpct&x=' + exch.upper() 
                + '&q=' + symbol.upper())
    response = urllib.request.urlopen(url_root)
    data=response.read().decode().split('\n')       #decode() required for Python 3
    data = [data[i].split(',') for i in range(len(data)-1)]
    header = data[0:7]
    data = data[7:]
    header[4][0] = header[4][0][8:]                           #get rid of 'Columns:' for label row
    df=pd.DataFrame(data, columns=header[4])
    
    ind=pd.Series(len(df))
    for i in range(len(df)):
        if df['DATE'].ix[i][0] == 'a':
            anchor_time = dt.datetime.fromtimestamp(int(df['DATE'].ix[i][1:]))  #make datetime object out of 'a' prefixed unix timecode
            ind[i]=anchor_time
        else:
            ind[i] = anchor_time +dt.timedelta(seconds = (period * int(df['DATE'].ix[i])))
    df.index = ind
    for i in range(1,6): #shitty implementation because to_numeric is pd but does not accept df
        df.ix[:,i]=pd.to_numeric(df.ix[:,i])
        
    df=df.drop('DATE', 1)
    
    return df, url_root
