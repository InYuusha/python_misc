import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

pages=set()
def get_url(url):
    global pages
    html=urlopen('http://en.wikipedia.org{}'.format(url))
    data=bs(html,'html.parser')
    try:

        print(data.h1.get_text())
        print((data.find(id='mw-content-text').find_all('p')[0]).encode('utf-8'))
        print((data.find(id='ca-edit').find('span').find('a').attrs['href']).encode('utf-8'))

    except AttributeError:
        print("This page is misssing something")    

    for link in data.find_all('a',href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                new_page= link.attrs['href']
                print('-'*20)
                print(new_page)
                
                pages.add(new_page)
                get_url(new_page)

get_url('')                