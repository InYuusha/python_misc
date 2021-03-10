import requests
from bs4 import BeautifulSoup as bs
html=requests.get("http://oreilly.com")
print(html)
#data=bs(html,'html.parser')
print((html.text).encode('utf-8'))

