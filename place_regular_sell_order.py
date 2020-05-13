import logging
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker

order = 0
prize = 0

logging.basicConfig(level=logging.DEBUG)
kite = KiteConnect(api_key="z830r462fkvxo1y4")
access_token ="9CkdF8zaw34oAKw94e286028HGLij029"


# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

#data = kite.generate_session("9X80lMXQaWD6L5ftrNhrpfmvALc1TPwX", api_secret="56rpjyatohblsqc2i0rn76jeij8s1beb")
#kite.set_access_token(data["access_token"])

kite.set_access_token(access_token)
kws = KiteTicker("z830r462fkvxo1y4", access_token)


def on_ticks(ws, ticks):
    global order
    global prize
    value = 125.80
    for x in  ticks:
        #print(x['last_price'])
        if(x['last_price']>=value)and order == 0 and prize == 0:
            order_id = kite.place_order(tradingsymbol="TATAMOTORS",
                                exchange=kite.EXCHANGE_NSE,
                                transaction_type=kite.TRANSACTION_TYPE_SELL,
                                quantity=1,
                                order_type=kite.ORDER_TYPE_MARKET,
                                variety='regular',
                                product=kite.PRODUCT_MIS)
            order = 1
            prize = x['last_price']
            print('order_id',order_id,'--------SELL---------','last_price         ',x['last_price'])

        if(x['last_price']<=(prize-0.1))and order == 1:
            order_id = kite.place_order(tradingsymbol="TATAMOTORS",
                                exchange=kite.EXCHANGE_NSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=1,
                                order_type=kite.ORDER_TYPE_MARKET,
                                variety='regular',
                                product=kite.PRODUCT_MIS)
            order = 0
            prize = 0
            print('order_id',order_id,'--------BUY---------Profit','last_price         ',x['last_price'])
        if(x['last_price']>=(prize+0.2))and order == 1:
            order_id = kite.place_order(tradingsymbol="TATAMOTORS",
                                exchange=kite.EXCHANGE_NSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=1,
                                order_type=kite.ORDER_TYPE_MARKET,
                                variety='regular',
                                product=kite.PRODUCT_MIS)
            order = 0
            prize = 0
            print('order_id',order_id ,'--------BUY---------Loss','last_price         ',x['last_price'])
            







































def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([884737])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_LTP, [884737])

def on_close(ws, code, reason):
    # On connection close stop the event loop.
    # Reconnection will not happen after executing `ws.stop()`
    ws.stop()

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()

