import pyautogui as p
im=p.screenshot()
obj=im.convert('L')
print(obj.getpixel((944,743)))
obj.show()
