from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs
import re
import random
import requests

pages=set()
random.seed()

def get_internal_links(data,iurl):                                                         

"l='{}://{}'.format(urlparse(iurl).scheme,urlparse(iurl).netloc)
    internal_links=[]
    for link in data.find_all('a',href=re.compile('^(/|.*'+iurl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internal_links:
                if (link.attrs['href'].startswith('/')):
                    internal_links.append(iurl+link.attrs['herf'])
                else :
                    internal_links.append(link.attrs['href'])    
    return internal_links


def get_external_links(data,eurl):
    global elinks
    elinks=[]
    for link in data.find_all('a',href=re.compile('^(http|www)((?!'+eurl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in elinks:
                elinks.append(link.attrs['href'])
    return elinks

def get_random_external_link(starting_page):
    html=requests.get("https://docs.python.org/3.4/library/urllib.request.html?highlight=urllib") 
    data=bs(html.text,'html.parser')     
    external_links=get_external_links(data,urlparse(starting_page).netloc)
    if len(external_links)==0:
        print('NO external link')
        domain='{}://{}'.format(urlparse(starting_page).scheme,urlparse(starting_page).netloc)  
        internal_links=get_internal_links(data,domain)
        return get_random_external_link(internal_links[random.randint(0,len(internal_links)-1)])
    else :
        return external_links[random.randint(0,len(external_links)-1)]    


def follow_external_links(starting_site):

    elink=get_random_external_link(starting_site)
    print("random external link  is {}".format(elink))
    follow_external_links(elink)

follow_external_links("http://oreilly.com")    
