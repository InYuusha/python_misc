import time
def calc():
    product=1
    for i in range(1,100000):
        
       product=product*i
    return product
starttime=time.time()
num=calc()
endtime=time.time()
print('Result is '+str(len(str(num)))+'\Long')
print('Time taken is '+str(endtime-starttime)+'\tSeconds')
      
