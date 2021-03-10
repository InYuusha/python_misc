from PIL import ImageGrab as ig
from PIL import Image
im=ig.grab() 
data=im.getdata()
print(list(data))
