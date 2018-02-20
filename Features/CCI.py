# Load the necessary packages and modules
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
# Commodity Channel Index
def CCI(data, ndays):
    TP = (data['High'] + data['Low'] + data['Close']) / 3
    CCI = pd.Series((TP - TP.rolling(ndays).mean()) / (0.015 * TP.rolling(ndays).std()),name = 'CCI')
    data = data.join(CCI)
    return data

if __name__ =='__main__':
    # Retrieve the Nifty data from Quandl:
    data = web.DataReader('AAPL',data_source='quandl',start='1/1/2017', end='1/1/2018')
    data = pd.DataFrame(data)
    # Compute the Commodity Channel Index(CCI) for NIFTY based on the 20-day Moving average
    n = 20
    NIFTY_CCI = CCI(data, n)
    CCI = NIFTY_CCI['CCI']
    # Plotting the Price Series chart and the Commodity Channel index below
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(2, 1, 1)
    ax.set_xticklabels([])
    plt.plot(data['Close'],lw=1)
    plt.title('AAPL Price Chart')
    plt.ylabel('Close Price')
    plt.grid(True)
    bx = fig.add_subplot(2, 1, 2)
    plt.plot(CCI,'k',lw=0.75,linestyle='-',label='CCI')
    plt.legend(loc=2,prop={'size':9.5})
    plt.ylabel('CCI values')
    plt.grid(True)
    plt.setp(plt.gca().get_xticklabels(), rotation=30)
    plt.show()
