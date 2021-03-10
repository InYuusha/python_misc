import random as rand
print('Iam taking a guess between (1,20)')
print('You have a 5 chances to guess the number')
def check(i):
    if i==rno:
        return '1'
    elif i>=rno+10:
            
        return '2'
  
    elif i>=rno+5 or i<rno+10:
        return '3'
        
       
  
       
    
        
    elif i<=rno-5 or i>rno-10:
        
        return'5'
    else:
        return '4'
        

    



rno=rand.randint(1,20)

for c in range(5):
    i=int(input('Take a guess'))
    r=check(i)
    if r=='1':
        print('correct the number was:'+str(rno))
    elif r=='2':
        print('Too high')
    elif r=='3':
        print('High')
    elif r=='4':
        print('Too low')
    elif r=='5':
        print('Low')
print(rno)        
