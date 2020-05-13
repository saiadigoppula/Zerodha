import time
import datetime
import pandas as pd
import requests
import json
import csv
import os

number_Period =14
multpL = 3
B = 1
pre_profit_open = 0

pre_loss_open = 0
firstATR = 0
Pre_ATR_trolling = 0



print(datetime.datetime.now())
currentDT = datetime.datetime.now()
print ("Current Hour is: %d" % currentDT.hour)
print ("Current Minute is: %d" % currentDT.minute)
print ("Current Second is: %d" % currentDT.second)

date = '2020-03-04'
hr = 0
mn = 0
sec = '00'

for_demo = 0

if(currentDT.minute == 59):
    hr = currentDT.hour + 1
    if(hr<=9):
        hr_str = '0'+str(hr)
        mn = 00
        timee = date+' '+hr_str+':'+str(mn)+':'+sec
        #timee_demo = date+' '+hr_str+':'+str(mn)+':'+'55'
    else:
        timee = date+' '+str(hr)+':'+str(mn)+':'+sec
        #timee_demo = date+' '+str(hr)+':'+str(mn)+':'+'55'
else:
    hr = currentDT.hour
    mn = currentDT.minute + 1
    if(mn<=9):
        mn_str = '0'+str(mn)
        timee = date+' '+str(hr)+':'+mn_str+':'+sec
        #timee_demo = date+' '+str(hr)+':'+mn_str+':'+'55'
    
    else:
        timee = date+' '+str(hr)+':'+str(mn)+':'+sec
        #timee_demo = date+' '+str(hr)+':'+str(mn)+':'+'55'

timee_demo = date+' '+str(currentDT.hour)+':'+str(currentDT.minute)+':'+'55'

print('our one min time',timee)
print('our one min timee_demo',timee_demo)

for x in range(1000):
	if(timee_demo <= str(datetime.datetime.now()) and for_demo == 0):
		for_demo = 1
		print('its me Pickil rick before ',datetime.datetime.now())
		take_data_and_save()
    	
        print('its me Pickil rick after ',datetime.datetime.now())
        superTrend()
        print('its me Pickil rick after superTrend',datetime.datetime.now())
        
    if(timee<=str(datetime.datetime.now())):
        currentDT = datetime.datetime.now()
        print('its me rick ',datetime.datetime.now())


        if(currentDT.minute == 59):
            hr = currentDT.hour + 1
            if(hr<=9):
                hr_str = '0'+str(hr)
                mn = 00
                timee = date+' '+hr_str+':'+str(mn)+':'+sec
            else:
                timee = date+' '+str(hr)+':'+str(mn)+':'+sec
        else:
            hr = currentDT.hour
            mn = currentDT.minute + 1
            if(mn<=9):
                mn_str = '0'+str(mn)
                timee = date+' '+str(hr)+':'+mn_str+':'+sec
    
            else:
                timee = date+' '+str(hr)+':'+str(mn)+':'+sec


    time.sleep(1)




def superTrend():
	ompany_list = ['TATAMOTORSone']
	length_list = len(company_list)
	global number_Period
	global multpL
	global B
	global pre_profit_open

	global pre_loss_open 
	global firstATR 
	global Pre_ATR_trolling

	for i in range(length_list):
		print(company_list[i])
    	file = company_list[i] + ".csv"
    	df = pd.read_csv(file)

    	for x in range((number_Period+1),len(df)):
        Sum = 0
        if(x == (number_Period+1)):
            for y in range(x-number_Period,number_Period):
            	high =df['high'][y]
            	low = df['low'][y]
            	pre_close = df['close'][y-1]


            	true_range = true_range(high,low,pre_close)
            	sum = sum + true_range
            firstATR = (Sum)/number_Period
            Pre_ATR_trolling = (firstATR*multpL)+df['close'][x]
        else:
        	high =df['high'][x]
        	low = df['low'][x]
        	pre_close = df['close'][x-1]

        	true_range = true_range(high,low,pre_close)

        	ATR = (firstATR*(number_Period-1) +true_range)/number_Period


        	if(B == 0):
                
                if(df['close'][x]<=Pre_ATR_trolling):
                    ATR_trolling = (ATR*multpL)+(df['high'][x]+df['low'][x])/2 
                    if(float(Pre_ATR_trolling) > float(ATR_trolling)):
                        Pre_ATR_trolling = ATR_trolling
                    else:
                        Pre_ATR_trolling = Pre_ATR_trolling

                else:
                    B = 1
                    print("date    ",df['date'][x])
                    pre_profit_open = df['openn'][x]
                    ATR_trolling = (df['high'][x]+df['low'][x])/2 - (ATR*multpL)
                    Pre_ATR_trolling = ATR_trolling
                    print("B",B,"  Pre_ATR_trolling ",Pre_ATR_trolling)
                    
            else:
               
                if(df['close'][x] >= Pre_ATR_trolling ):
                    ATR_trolling = (df['high'][x]+df['low'][x])/2 - (ATR*multpL)
                    if(float(Pre_ATR_trolling) < float(ATR_trolling)):
                        Pre_ATR_trolling = ATR_trolling
                else:
                    B = 0
                    pre_loss_open = df['openn'][x]
                    print("date    ",df['date'][x])
                    ATR_trolling = (ATR*multpL)+(df['high'][x]+df['low'][x])/2
                    Pre_ATR_trolling = ATR_trolling
                    print("B",B,"  Pre_ATR_trolling ",Pre_ATR_trolling)

            print("date    ",df['date'][x])
            print("close   ",df['close'][x])
            print("B",B,"  Pre_ATR_trolling ",Pre_ATR_trolling)
            print("")
            firstATR = ATR








def true_range(high,low,pre_close):
	High_Low = (high - low)
    High_PreClose = abs(high - pre_close)
    Low_PreClose = abs (low - pre_close)
    list =[High_Low,High_PreClose,Low_PreClose]

                    
    if(High_Low ==High_PreClose == Low_PreClose ):
        true_range = High_Low

    else:
        true_range = max(list)


    return true_range









def take_data_and_save():
	

	lists = ['TATAMOTORS']        




	length = len(lists) 

	for i in range(length):
		x = lists[i]+".NS"
		url = 'https://intraday.worldtradingdata.com/api/v1/intraday'
		params = {
		  'symbol': x,
		  'api_token': 'EfopvFRc7g1bEnX6vpfifY0spt1rHFWDy1m4yjAHI6iSrMGBJJOS6z8Q9Tg8',
		  'interval': '1',
		  'range': '4'
		}
		response = requests.request('GET', url, params=params)
		response.json()
		sai = response.json()
		rai = sai['intraday']
		with open("demo.csv","w",newline='') as f:
		    thewriter = csv.writer(f)
		    #thewriter.writerow(['date','openn','close','high','low','volume'])
		    for p_id, p_info in rai.items():
		        #print(p_id,end = ',')
		        for key in p_info:
		            if(key == "open"):
		                openn =  float(p_info[key])
		                #print(openn,end = ',')

		            if(key == "close"):
		                close =  float(p_info[key])
		                #print(close,end = ',')

		            if(key == "high"):
		                high =  float(p_info[key])
		                #print(high,end = ',')

		            if(key == "low"):
		                low =  float(p_info[key])
		                #print(low,end = ',')

		            if(key == "volume"):
		                volume =  float(p_info[key])
		                #print(volume)
		        thewriter.writerow([p_id,openn,close,high,low,volume])
		        
		with open('demo.csv', 'r') as textfile:
		    with open(lists[i]+"one.csv","w",newline='') as ff:
		        thewriterr = csv.writer(ff)
		        thewriterr.writerow(['date','openn','close','high','low','volume'])
		        for row in reversed(list(csv.reader(textfile))):
		            date = row[0]
		            #print(date)
		            openn = row[1]
		            close = row[2]
		            high = row[3]
		            low = row[4]
		            volume = row[5]
		            thewriterr.writerow([date,openn,close,high,low,volume])
		                #print(', '.join(row))
		                #print(row[1])
		os.remove("demo.csv")
		print("fineshed"+lists[i])
	print("FINISHED ALL!")
