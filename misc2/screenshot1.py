import pyautogui as p,time as t
t.sleep(5)
im=p.screenshot()
im.save('C:\\Users\\op\\Desktop\\new.png')
print(p.locateOnScreen('C:\\Users\\op\\Desktop\\new.png'))
