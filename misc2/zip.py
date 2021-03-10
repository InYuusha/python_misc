import os ,zipfile as z
zfile=z.ZipFile('C:\\New folder\\zfile.zip','w')
for finame in os.listdir('C:\\New folder\\create'):
    zfile.write(os.path.join('C:\\New folder\\create',finame))
zfile.close()    
   
    
