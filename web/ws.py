from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def title(url):
    try:
        url=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs=BeautifulSoup(url.read(),'html.parser')
        title=bs.head.h1
        
    except AttributeError as a:
        return None
    return title    
t=title("https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path")
if t==None:
    print("Title COuldnt be found")
else:
    print(t)                        