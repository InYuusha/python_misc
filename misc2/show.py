from PIL import ImageGrab as i
import pyautogui as p
im=i.grab()
im=im.convert('L')
im.show()
