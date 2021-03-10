from PIL import ImageGrab as ig
import time as t
from PIL import ImageDraw as id
t.sleep(10)
im=ig.grab()
draw=id.Draw(im)
draw.rectangle((750,175,820,185),fill='white',outline='RED')
im.show()
