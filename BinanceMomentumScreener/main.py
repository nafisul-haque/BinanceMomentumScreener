import requests
import pandas as pd
from binance import Client
import datetime as dt
import time
import numpy as np

client = Client('8sFToJNlu727nDtrhPX3AVQsAI1ugCCgDE9PSjj4LE1N279rWbUegPDdOxvDzbq2', 'EwlApkxxb57uSJXRIrezGvnBnSK0t6Z9dS6veJIFkIBAN9OKkKq5JebGegofMwnW')
historical_data = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, '17 July 2022')

length = 10
T = 365

t10 = (pd.DataFrame(historical_data)).tail(length)
close_arr = t10[4].to_numpy()

tickers = pd.DataFrame(client.get_ticker())
tickers_arr = tickers['symbol'].to_numpy()
print(len(tickers_arr))

def h_vol():
    i = 1
    diff = []

    for i in range(len(close_arr)):
        log_return = np.log(float(close_arr[-i]) / float(close_arr[-i - 1]))
        diff.append(log_return)
        i += 1

    std_dev = np.std(diff)
    hv = np.sqrt(T) * std_dev * 100

    return(diff, std_dev, hv)

#while True:
 #   hv_one = h_vol(close_arr)
  #  time.sleep(60)




# hv = 100 * ta.stdev(math.log(close / close[1]), length) * math.sqrt(annual / per)
