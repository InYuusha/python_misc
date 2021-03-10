import os
for fonames , sfnames, finames in os.walk('C:\\New folder'):
    print('The current folder name is '+fonames)
    for sfname in sfnames:
        print('The subfolder in '+fonames+'\tis\t'+sfnames)
    for finames in finame:
        print('The filenames in '+fonames+'\tis\t'+finames)
