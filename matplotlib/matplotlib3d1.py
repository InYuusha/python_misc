import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
x=[1,2,3,4,5]
y=[1,2,3,4,5]
ax=Axes3D(fig)
ax.bar(x,y,color='red')
plt.show()
