import time
print('Instructions \n1)Enter to strart\n2)Enter to click\n3)Ctrl-C to exit')
input()
print("Started")
starttime=time.time()
lasttime=starttime
lapnum=1
try:
    while True:
        input()
        overalltime=round(time.time()-starttime)
       
        laptime=round(time.time()-lasttime)
        print('Overall time :'+str(overalltime)+'\nlap time '+str(laptime))
        
        
        lapnum+=1
        lasttime=time.time()
except KeyboardInterrupt:
    print('Done')

        
        
