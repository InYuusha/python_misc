import pyautogui as p,time as t
from PIL import ImageGrab as ig

def escape(key):
    p.press(key)
    return

   
def check(data):
    
    for i in range(760,840):
        for j in range(195,200):
            if data[i,j]<100:
                    escape('up')
                    return
                    
                
    for i in range(760,840):
        for j in range(167,182):
            if data[i,j]<100:
                escape('down')
                return
        


print('Program will run in 10 secs')
for i in range(10):
    print('programm will run in :'+str(i)+'seconds')

while True:
        
    
        im=ig.grab()
        im=im.convert('L')
        data=im.load()
        check(data)
    
    
    
                
