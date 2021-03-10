from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
    html= urlopen("http://google.com")
except HTTPError as e:
    print(e)
except URLError as u:
    print(u)
else:
    print("it Worked" )    #shows nothing except it worked
