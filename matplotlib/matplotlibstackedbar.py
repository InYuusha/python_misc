import matplotlib.pyplot as plt
import numpy as np
index=['March','May','June','July']
series=np.array([1,2,5,3])
series2=np.array([4,3,1,5])
series3=np.array([2,1,3,3])

plt.bar(index,series,color='w',hatch='xx')
plt.bar(index,series3,color='w',hatch='--',bottom=series)
plt.bar(index,series3,color='r',bottom=series+series2)
plt.legend(['Cross','Line','Red'],loc='upper left')

plt.show()

