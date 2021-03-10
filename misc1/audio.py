import time , os , subprocess as s
timeleft=5
while timeleft>0:
    print('Time Left is: '+str(timeleft))
    time.sleep(1)
    timeleft-=1
s.Popen(['start','C:\\New folder\\audio.mp3'],shell=True)    
    
   

    
