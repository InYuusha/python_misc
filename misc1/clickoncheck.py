import pyautogui as p,time as t
t.sleep(5)
x,y,z,w=p.locateOnScreen('C:\\Users\\op\\Desktop\\submit.png')
p.click(p.center((x,y,z,w)))
