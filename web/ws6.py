from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
html=urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
data=bs(html,'html.parser')
for link in data.findAll('a',href=re.compile('^(/wiki)((?!')):
