from Command import *
from GUI import LoginCredentials
from Stratgey import MarketData
print('Enter the Symbol')
SYMBOL = input()
qty = input()
qty =str (qty)
print(type(qty))
print(qty)
print(type(qty))
def POSITION (SYMBOL):
    token_info = MarketData.gettokeninfo(MarketData.token_df, 'NSE', 'NSE_EQ', SYMBOL, 0, 'CE').iloc[0]
    a2 =token_info['token']
    a1 = MarketData.getHistoricalAPI(a2,'ONE_DAY')
    g = {}
    g = a1
    q = g['data'][0][4]
    q = int(q)
    a3 = MarketData.ema(g,250)
    if q > a3 :
        try:
            orderparams = {
                "variety": "NORMAL",
                "tradingsymbol": token_info['symbol'],
                "symboltoken": token_info['token'],
                "transactiontype": 'BUY',
                "exchange": 'NSE',
                "ordertype": 'MARKET',
                "producttype": "DELIVERY",
                "duration": "DAY",
                "price": '0',
                "squareoff": "0",
                "stoploss": "0",
                "quantity": qty,
            }
            orderId = LoginCredentials.obj.placeOrder(orderparams)
            print("The order id is: {}".format(orderId))
        except Exception as e:
            print("Order placement failed: {}".format(e.message))
    else:
        try:
            orderparams = {
                "variety": "NORMAL",
                "tradingsymbol": token_info['symbol'],
                "symboltoken": token_info['token'],
                "transactiontype": 'SELL',
                "exchange": 'NSE',
                "ordertype": 'MARKET',
                "producttype": "DELIVERY",
                "duration": "DAY",
                "price": '0',
                "squareoff": "0",
                "stoploss": "0",
                "quantity": qty,
            }
            orderId = LoginCredentials.obj.placeOrder(orderparams)
            print("The order id is: {}".format(orderId))
        except Exception as e:
            print("Order placement failed: {}".format(e.message))
print(POSITION(SYMBOL))