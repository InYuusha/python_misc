bday={'ankush':'05-May','abhisshek':'08-june','kajol':'03-jul'}
while True:
    name=input('Enter a Name:(Blank to quit)')
    if name=='':
        quit()
        
    elif name in bday:
        print('The bday of'+name+' is'+bday[name])
        
    else:
        print('I dont have bday info of '+name)
