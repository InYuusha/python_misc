'''           CRAWLING WIKIPEDIA
              -------------------
   GETTING A RANDOM HYPERLINK FROM A WIKIPEDIA PAGE , 
   PASSING IT INTO THE FUNC
   GETTING  RANDOM HYPERLINK FROM THAT PAGE AND SO ON    '''

 #                                          @doingstuffswithpython

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import random
import re
random.seed()

def get_url(given_url):
    url="http://en.wikipedia.org{}".format(given_url)
    html=urlopen(url)
    data=bs(html,'html.parser')

    return data.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki)((?!:).)*$'))   
                                                                                
                                      #Regular expression
                                      # ^ ="starts with"   
                                      # #?!="doesnt have"
                                      # $="till end"                                
link=get_url('/wiki/Bodhidharma')
while len(link)>0:
    new_link=link[random.randrange(0,len(link)-1)].attrs['href'] 
    ''' attribute value(that is hyperlink) of <a> tag '''
    print(new_link)
    link=get_url(new_link)    





