from urllib.request import urlopen
from urllib.parse import urlparse 
from bs4 import BeautifulSoup as bs
import re
import random
import requests

def get_internal_links(data,iurl):
    global internal_links
    internal_links=[]
    for link in data.find_all('a',href=re.compile('^(/|.*'+iurl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internal_links:
                internal_links.append(link.attrs['href'])

    return internal_links 

def get_external_links(data,eurl):
    global external_links
    external_links=[]
    for link in data.find_all('a',href=re.compile('^(http|www)((?!'+eurl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in external_links:
                external_links.append(link.attrs['href'])

    return external_links

def get_random_external_link(starting_page):
    html=requests.get("http://oreilly.com")
    data=bs(html.text,'html.parser')
    
    elinks=get_external_links(data,urlparse(starting_page).netloc)
    if len(elinks)==0:
        print("NO external links")
        ilinks=get_internal_links(data,urlparse(starting_page).netloc)
        return get_random_external_link(ilinks[random.randrange(0,len(ilinks)-1)])
    else :
        return elinks[random.randrange(0,len(elinks)-1)]    

        
def follow_external_links(starting_site):
    o_link=get_random_external_link(starting_site)
    print('External link is {}'.format(o_link))
    follow_external_links(o_link)

follow_external_links("http://oreilly.com")    
    
