import pyautogui as p,time as t
t.sleep(5)
p.typewrite('something',0.25)
x,y,z,w=p.locateOnScreen('C:\\Users\\op\\Desktop\\submit.png')
t.sleep(2)
p.click(p.center((x,y,z,w)))



