import numpy as np
import matplotlib.pyplot as plt

item=[1,2,3,4,5]
def sqr(x):
    return(x**2)

fig=plt.figure()
new=fig.add_subplot(111)
y=list(map(sqr,item))
new.plot(item,y)
plt.show()

