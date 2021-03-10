def picnicitems(itmdict,lewid,rewid):
    print('PICNIC ITEMS'.center(lewid+rewid,'-'))
    for k,v in itm.items():
       
        print(k.ljust(lewid,'-')+str(v).rjust(rewid,'-'))
              

itm={'sanwitches':4,'toast':7,'milk':3,'jam':9}

picnicitems(itm,16,4)
picnicitems(itm,20,5)
                              
                            
