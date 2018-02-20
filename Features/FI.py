################# Force Index ########################################################

# Load the necessary packages and modules
import pandas as pd
import pandas_datareader as web

# Force Index
def ForceIndex(data, ndays):
    FI = pd.Series(data['Close'].diff(ndays) * data['Volume'], name = 'ForceIndex')
    data = data.join(FI)
    return data

if __name__ == '__main__':
    # Retrieve the Apple data from quandl:
    data = web.DataReader('AAPL',data_source='quandl',start='1/1/2015', end='1/1/2016')
    data = pd.DataFrame(data)

    # Compute the Force Index for Apple
    n = 1
    AAPL_ForceIndex = ForceIndex(data,n)
    print(AAPL_ForceIndex)
