import datetime
from pprint import pprint
import logging
from kiteconnect import KiteTicker

logging.basicConfig(level=logging.DEBUG)


# Initialise
kws = KiteTicker("z830r462fkvxo1y4", "9CkdF8zaw34oAKw94e286028HGLij029")



def on_ticks(ws, ticks):
    for x in  ticks:
        print(x['last_price'])
        
        
        
    # Callback to receive ticks.
    #logging.debug("Ticks: {}".format(ticks))
    #pprint(ticks)
    #print("\n")

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




#[{'instrument_token': 884737,
 # 'last_price': 125.8,
  #'mode': 'ltp',
  #'tradable': True}]



