keys=['hello','say','we','donot','lie']
import random
start=random.randrange(0,len(keys)-1)
end=random.randrange(1,len(keys))
for i  in range(start,end):
    print(keys[i])

