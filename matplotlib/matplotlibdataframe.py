import numpy as  np
import matplotlib.pyplot as plt
import pandas as pd
data={'series1':[1,2,3,4,5],
       'series2':[2,3,5,2,4],
       'series3':[7,3,2,5,6]
       }

ndata=pd.DataFrame(data)
ndata.plot(kind="bar")

plt.grid(True)
plt.show()
1
