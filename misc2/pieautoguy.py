import pyautogui as p

for i in range(300,0,-15):
    for j in range(300,0,-30):
                   

    
           p.moveRel(-i,0,duration=0.25)
           p.moveRel(0,-j,duration=0.25)
           p.moveRel(i,0,duration=0.25)
           p.moveRel(0,j,duration=0.25)
           p.FAILSAFE=True
           i=i-30
           if j==20 :
               exit()
           
       
 

