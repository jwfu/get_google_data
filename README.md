# get_google_data
Gets intraday data (including realtime on certain exchanges) from Google Finance and returns a Pandas Dataframe.

This code is an extension of MKTSTK's script from [here] (https://mktstk.wordpress.com/2014/12/31/how-to-get-free-intraday-stock-data-with-python/) with the added functionality of being able to select the exchange from which the data is coming.  There are also a few changes on the backend.

Find out more about the nature of the data and delays from [here] (http://www.google.com/intl/en/googlefinance/disclaimer/).

Note that the Google Finance API is depricated so use at your own hazard.

# Usage
```
get_google_data(symbol, period, window, exch = 'NYSE')
```

**symbol**: ticker

**period**: sample frequency in seconds

**window**: number of days in days

**exch**: exchange to get data

# Example
```
get_google_data('FM', 6000, 1, 'TSE')
```
