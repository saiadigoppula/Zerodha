import datetime
import time
#2020-03-04 11:53:00

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
        print('its me Pickil rick rick ',datetime.datetime.now())
        
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
        
