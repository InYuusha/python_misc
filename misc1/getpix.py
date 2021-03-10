import pyautogui as p,time as t
t.sleep(10)
im=p.screenshot()
print(im.getpixel((734,201)))
