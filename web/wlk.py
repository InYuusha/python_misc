import os
for fonames , sfnames , finames in os.walk('C:\\New folder\\Freedom Fighters 1 - Apun Ka Games'):
    print(fonames)

    for finame in finames:
        print(finame)
    
