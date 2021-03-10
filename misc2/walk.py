import os
for fonames , subfonames, finames in os.walk('C:\\New Folder\\ANIME'):
    print('The folders :'+fonames)

for finame in finames:
    print('The filenames are:'+finame)
