def fact(num):
   
     if num==1:
         return num
     else:
         return num*fact(num-1)
         
        
        
       

    
while True:
    
   c=int(input('Enter a number'))
   print(fact(c))
   continue

