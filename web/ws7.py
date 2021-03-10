from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

html=urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')

data=bs(html,'html.parser')
for link in data.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
