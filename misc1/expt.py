import time as t
def prog(num,word):
    
    
    if len(word)!=5:
        raise Exception('length must be equal to 5')
    if num<5:
        raise Exception('num must be greater than 5')
    if  num>10:
        raise Exception('num must be smaleer than 10')
    
    
num=int(input('Enter a number that must not exceed 10 , and not smaller than 5'))
t.sleep(3)
word=str((input('Enter a word of length 5 only')))
prog(num,word)
