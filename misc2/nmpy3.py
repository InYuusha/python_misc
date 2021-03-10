import numpy as np
import cv2
img=cv2.imread("C:\\Users\op\\Desktop\\python.jpeg")
print(img.dtype)


arr=np.zeros(img.shape,dtype=img.dtype)
print(arr)
