import os
import numpy as np
import cv2 as c
r_text=os.urandom(120000)
arr=bytearray(r_text)
print(arr)
flatarr=np.array(arr)
print(flatarr)
shaped_arr=flatarr.reshape((300,400))
print(shaped_arr)

c.imwrite("C:\\Users\\op\\Desktop\\rand.png",shaped_arr)


