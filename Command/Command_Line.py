import GUI
from GUI import LoginCredentials
from Stratgey import MarketData
print('STOCK SYMBOL')

enter_stockname = input(str())

print('exchange :BSE,NSE,NFO,MCX')
exc = input(str())
print('enter quantity')
qty = input(int())
print(qty)
price = MarketData.g['data'][4][-1]
price = int(price)
a = MarketData.ema(MarketData.getHistoricalAPI(1660,'ONE_MINUTE'))
token_info = MarketData.gettokeninfo(MarketData.token_df,exc,'EQ',enter_stockname,price,'CE').iloc[0]
print(token_info)
print(token_info['symbol'])
print(token_info['token'])
command = ''
if a > price:
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": token_info['symbol'],
            "symboltoken": token_info['token'],
            "transactiontype": "SELL",
            "exchange": "NSE",
            "ordertype": "LIMIT",
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
else:
    command = 'SELL'
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": token_info['symbol'],
            "symboltoken": token_info['token'],
            "transactiontype": "BUY",
            "exchange": "NSE",
            "ordertype": "LIMIT",
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

