import random
data={'maharastra':'mumbai','goa':'panji','up':'agra'}
for quizno in range(5):
    test=open('quizs.txt' +str(quizno+1),'w')
    ans=open('ans%s.txt' %(quizno+1),'w')

    test.write('Name:\nDate:\n\n')
    test.write(''*20+'\tState Capitals Quiz (Form%s)'%(quizno+1))
    states=list(data.keys())
    random.shuffle(states)
    
    for i in range(len(states)):
       

         test.write('\nThe capital of '+states[i]+':-\n')
         ans.write('The capital of '+states[i]+'is'+data[states[i]])
         capitals=list(data.values())
         random.shuffle(capitals)
         for i in range(len(capitals)):
                test.write(str(i+1)+' '+capitals[i]+'\n')
                
                
   
                             
for i in range(5):
    test=open('quizs.txt'+str(i+1))
    content=test.read()
    print(content)
