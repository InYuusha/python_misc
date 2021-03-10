import matplotlib.pyplot as p
import numpy as np

np.random.seed(0)
g=np.floor(np.random.random((100,100))+0.5)
p.imshow(g,cmap='pink')
p.show()
