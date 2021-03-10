import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,2,3,4,5]
xx,yy=np.meshgrid(x,y)
plt.plot(xx,yy)
plt.show()
