import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=Axes3D(fig)
X=np.arange(-2,2,0.1)
Y=np.arange(-2,2,0.1)
X,Y=np.meshgrid(X,Y)
def f(x,y):
    return (x**2+y**2)
ax.plot_surface(X,Y,f(X,Y),rstride=1,cstride=1,cmap=plt.cm.hot)
plt.show()
