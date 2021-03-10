import pyautogui as p,time as t
t.sleep(5)
print('Starting')
for i in range(5):
    t.sleep(1)
    print('Time remaining :'+str(i))
dist=200

while dist>0:
    
    p.dragRel(dist,0,duration=0.7)
    dist=dist-5
    p.dragRel(0,dist,duration=0.7)
    dist=dist-5
    p.dragRel(-dist,0,duration=0.7)
    dist=dist-5
    p.dragRel(0,-dist,duration=0.7)
    dist=dist-5
    p.FAILSAFE=True











