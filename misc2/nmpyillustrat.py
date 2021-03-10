import numpy as np
import cv2 as c

arr=np.arange(10000).reshape((100,100))
c.imwrite("C:\\Users\\op\\Desktop\\win.png",arr)
