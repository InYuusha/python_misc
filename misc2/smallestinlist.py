def small(arr):
    
    small=arr[0]
    
    for i in range (len(arr)):
        if i==(len(arr)-1):
            
           return small
        
        
        elif arr[i]>arr[i+1]:
            
           small=arr[i+1]
    return small           
        
    
def s_small(arr):

    r_arr=sorted(arr,reverse=True)
    s_sma=r_arr[-2]
    return s_sma
   
    
    

s=int(input("Enter the size of array"))
print("Enter the elements of the array")
arr=[]
for i in range(s):
    e=int(input("Enter the "+str(i)+" Element"))
    arr.append(e)
sma=small(arr)
s_sma=s_small(arr)
print("smallest number is "+str(sma))
print("second smallest number is "+str(s_sma))
