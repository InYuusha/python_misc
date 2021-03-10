import numpy as np
import matplotlib.pyplot as plt
import math as m


x=np.arange(0,2.5,0.1)
y=list(map(m.sin,m.pi*x+m.pi/2))
plt.plot(x,y)
plt.show()
