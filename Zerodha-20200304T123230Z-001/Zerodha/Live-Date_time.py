import datetime
from pprint import pprint
import logging
from kiteconnect import KiteTicker

logging.basicConfig(level=logging.DEBUG)


# Initialise
kws = KiteTicker("z830r462fkvxo1y4", "9CkdF8zaw34oAKw94e286028HGLij029")

time = '2020-03-04 11:52:00'

def on_ticks(ws, ticks):
    global time
    for x in  ticks:
        #print(datetime.datetime.now())
        print(x['last_price'])
        if( str(datetime.datetime.now()) >=time):
            print(datetime.datetime.now())
            time = '2020-03-04 11:53:00'
        
        

























def on_connect(ws, response):
    ws.subscribe([884737])
    ws.set_mode(ws.MODE_LTP, [884737])

















def on_close(ws, code, reason):
   
    ws.stop()
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect()






