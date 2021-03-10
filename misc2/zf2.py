import zipfile, os , shutil as s
import time as t

zfile=zipfile.ZipFile('newzpfile','w')
def newzpfile(folder):
  
    for foldern ,sbfoldern,filesn in os.walk(folder):
        zfile.write(foldern)
        
      
        
        for file in filesn:
            
            zfile.write(os.path.join(foldern,file))

newzpfile('C:\\New folder\\Freedom Fighters 1 - Apun Ka Games')
print(zfile.namelist())
        
    
    
    
    
