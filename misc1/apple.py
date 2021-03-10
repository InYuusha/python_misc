allitems={'alice':{'apple':5,'melon':10},
          'phil':{'apple':7,'melon':9},
          'sam':{'apple':4,'melon':7}
          }
def itemsbrought(name,item):
    itm=0
    for k,v in allitems.items():
        itm=itm+v.get(item,0)
    return itm
print("apple brought" +str(itemsbrought(allitems,'apple')))
