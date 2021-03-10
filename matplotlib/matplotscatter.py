import numpy as np
import matplotlib.pyplot as plt
y=1
for x in range(10):
    
    plt.scatter(x,y)
    y=y+1
for x in range(10,20):
    plt.scatter(x,y)
    y=y-1

plt.show()    
