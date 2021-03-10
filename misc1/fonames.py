import os
for fonames , sfnames, finames in os.walk('C:\\New folder'):
    print('folder is...'+fonames)
    for sfname in sfnames:
        print('The subfolder of '+fonames+'\tis\t'+sfname)
   # for finame in finames:
    #    print('The filenames of '+fonames+'\tis\t'+finame)
