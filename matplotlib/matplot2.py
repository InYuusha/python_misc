import matplotlib.pyplot as plt
import math as m
import numpy as np
t=np.arange(0,2.5,0.1)
y=list(map(m.sin,m.pi*t))
y1=list(map(m.sin,m.pi*t+m.pi/2))
y2=list(map(m.sin,m.pi*t-m.pi/2))
plt.plot(t,y,'b*',t,y1,t,'^',y2,'b--')
plt.show()

