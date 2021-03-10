import numpy as np
import matplotlib.pyplot as plt
labels=['Smasung','Nokia','Xiomi','Redmi']
plt.title("Brand Domination of Smartphones",fontsize=30,fontname='Times New Roman')
values=[35,15,20,30]
explode=[0.2,1,0,0]
colors=['Blue','Green','Red','Yellow']
plt.pie(values,colors=colors,labels=labels,explode=explode, shadow=True,startangle=180)

plt.show()
