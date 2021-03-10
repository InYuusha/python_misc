Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: C:/Users/op/AppData/Local/Programs/Python/Python37-32/jn.py ====
>>> import od
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import od
ModuleNotFoundError: No module named 'od'
>>> import os
>>> os.path.abspath('.')
'C:\\Users\\op\\AppData\\Local\\Programs\\Python\\Python37-32'
>>> os.path.isabs('C:\\Users')
True
>>> os.path.relpath('C:\\Users')
'..\\..\\..\\..\\..\\..'
>>> path='C:\\New folder\\elizabeth.nnt___Bq-zO08HLfv___.mp4'
>>> os.path.basename(path)
'elizabeth.nnt___Bq-zO08HLfv___.mp4'
>>> os.path.dirname(path)
'C:\\New folder'
>>> os.path.split(path)
('C:\\New folder', 'elizabeth.nnt___Bq-zO08HLfv___.mp4')
>>> p=(os.path.basename(path),os.path.dirname(path))
>>> print(p)
('elizabeth.nnt___Bq-zO08HLfv___.mp4', 'C:\\New folder')
>>> path.split(os.path.sep)
['C:', 'New folder', 'elizabeth.nnt___Bq-zO08HLfv___.mp4']
>>> os.path.getsize('C;\\Users')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    os.path.getsize('C;\\Users')
  File "C:\Users\op\AppData\Local\Programs\Python\Python37-32\lib\genericpath.py", line 50, in getsize
    return os.stat(filename).st_size
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'C;\\Users'
>>> os.path.getsize('C:\\New folder\\Prototype 2\\Steamclient.dll')
358912
>>> os.listdir('Cos.path.getsize('C:\\New folder\\Prototype 2\\Steamclient.dll')os.path.getsize('C:\\New folder\\Prototype 2\\Steamclient.dll')Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
	   
SyntaxError: invalid syntax
>>> os.path.getsize('c:\\New folder\\Prototype 2\\Steamclient.dll')
