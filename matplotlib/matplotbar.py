import matplotlib.pyplot as plt
import numpy as np

index=['a','b','c','d','e']
values=[5,6,4,3,2]
std1=[0.8,0.1,0.4,0.9,1]
plt.bar(index,values,yerr=std1)
plt.legend(["red","green"],loc="lower right")
plt.show()


