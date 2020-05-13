from kiteconnect import KiteConnect


# --- URL for request tocken-----
#https://kite.trade/connect/login?api_key=z830r462fkvxo1y4



#give for the first time 
request_token = "0JW35IyMOcKkNZMxe7C3V0PojHa6cuxY"

api_key = "z830r462fkvxo1y4"

api_secret = "56rpjyatohblsqc2i0rn76jeij8s1beb"

access_token ="9CkdF8zaw34oAKw94e286028HGLij029"





kite = KiteConnect(api_key = api_key)



#---using request tocken----
data = kite.generate_session(request_token, api_secret = api_secret)
print(data)



#kite.set_access_token(access_token)




#print(kite.orders())
