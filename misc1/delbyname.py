import os
for finame in os.listdir('C:\\New Folder\\create'):   # Any Location
    
 if finame.endswith('.txt'):                        #All text files
    os.unlink(os.path.join('C:\\New Folder\\create',finame)) #Deleting Files








