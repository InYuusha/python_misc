from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

pages=set()

def get_url(url):
    global pages
    url="http://en.wikipedia.org{}".format(url)
    html= urlopen(url)
    data=bs(html,'html.parser')
    for link in data.find_all('a',href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:

                new_page=link.attrs['href']
                print(new_page)
                pages.add(new_page)
                get_url(new_page)



get_url('')
