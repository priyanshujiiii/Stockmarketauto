import itertools
from GUI import LoginCredentials
import pandas as pd
from datetime import datetime
import requests
import numpy as np

#This part of code help to GET A TOKEN AND SYMBOL.
url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
d = requests.get(url).json()
token_df = pd.DataFrame.from_dict(d)
token_df['expiry']= pd.to_datetime(token_df['expiry'])
token_df = token_df.astype({'strike':float})
#token_df.to_csv(r'F:\\demo_file\\'+ 'angel_token.csv', header = True,( index = false)
def gettokeninfo (df,exch_seg,instrumenttype,symbol,strike_price,pe_ce):
    strike_price = strike_price*100
    if exch_seg == 'NSE':
        eq_df = df[(df['exch_seg'] == 'NSE') & (df['symbol'].str.contains('EQ'))]
        return eq_df[eq_df['name'] == symbol]
    elif exch_seg == 'NFO' and ((instrumenttype == 'FUTSTK') or (instrumenttype == 'FUTIDX')):
        return df[(df['exch_seg'] == 'NFO') & (df['instrumenttype'] == instrumenttype) & (df['name'] == symbol)].sort_values(by=['expiry'])
    elif exch_seg == 'NFO' and (instrumenttype == 'OPTSTK' or instrumenttype == 'OPTIDX'):
        return df[(df['exch_seg'] == 'NFO') & (df['instrumenttype'] == instrumenttype) & (df['name'] == symbol) & (df['strike'] == strike_price) & (df['symbol'].str.endswith(pe_ce))].sort_values( by= ['expiry'])
token_info = gettokeninfo(token_df,'NFO','FUTSTK','JSWSTEEL',700,'CE').iloc[0]

#print(token_info)
#print(token_info['symbol'])
#print(token_info['token'])


# historical data
import json
from datetime import datetime
def historicaldata ():
    try:
        historicparam = {
            'exchange':'NSE',
            'symboltoken':token_info['token'] ,
            'interval':'ONE_MINUTE',
            'fromdate':'2021-01-01 14:00',
            'todate':'2021-01-01 14:15'
        }
        return LoginCredentials.obj.getCandleData(historicparam)
    except Exception as e:
        print('Historic Api Failed'.format(e.message))
print(historicaldata())


#getting historical api
from datetime import datetime,timedelta
def getHistoricalAPI(token,interval):
    to_date = datetime.now()
    from_date = to_date - timedelta(days=2000)
    from_date_format = from_date.strftime("%Y-%m-%d %H:%M")
    to_date_format = to_date.strftime("%Y-%m-%d %H:%M")
    try:
        historicParam={
            'exchange':'NSE',
            'symboltoken':token,
            'interval':interval,
            'fromdate':from_date_format,
            'todate':to_date_format
        }
        candel_json = LoginCredentials.obj.getCandleData(historicParam)
        return candel_json
    except Exception as e:
        print('Historic Api failed:{}'.format(e.message))
        print('g')
#print(7)
#print(getHistoricalAPI(1660))
#print(8)
#g = {}
#g = getHistoricalAPI(1660)
#q = g['data'][0][4]



#ema
def ema(g,K):
    K = int(K)
    avg =  -1
    f = {}
    s = 0
    u = 0.0
    Z = 1
    while Z== 1:
        f = g['data'][avg][4]
        u = u + f
        avg = avg + (- 1)
        if avg == -K:
            break
    avgk = u /K
    avgk = int(avgk)
    return avgk
#print(ema(g))

def place_order(token,symbol,qty,exch_seg,buy_sell,ordertype,price):
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": symbol,
            "symboltoken": token,
            "transactiontype": buy_sell,
            "exchange": exch_seg,
            "ordertype": ordertype,
            "producttype": "INTRADAY",
            "duration": "DAY",
            "price": price,
            "squareoff": "0",
            "stoploss": "0",
            "quantity": qty,
        }
        orderId = LoginCredentials.obj.placeOrder(orderparams)
        print("The order id is: {}".format(orderId))
    except Exception as e:
        print("Order placement failed: {}".format(e.message))

