import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
fig,a=plt.subplots(2,2)

a[0][0].plot(x,x**2)
a[0][0].set_title("Square",fontsize=20,fontname="Times New Roman",bbox={'facecolor':'red','alpha':0.5})
a[0][0].grid(True)

a[0][1].plot(x,np.sqrt(x))
a[0][1].set_title("Square root",fontsize=20,fontname="Times New Roman",bbox={'facecolor':'red','alpha':0.5})
a[0][1].grid(True)

a[1][0].plot(x,np.exp(x))
a[1][0].set_title("exponential",fontsize=20,fontname="Times New Roman",bbox={'facecolor':'red','alpha':0.5})
a[1][0].grid(True)

a[1][1].plot(x,np.log10(x))
a[1][1].set_title("logarithm",fontsize=20,fontname="Times New Roman" ,bbox={'facecolor':'red','alpha':0.5})
a[1][1].grid(True)

plt.show()



