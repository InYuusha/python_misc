



'''           WEB SCRAPING eg -2          '''
'''     GETTING ALL IMAGES FROM A WEB '''
          
'''    ---------------------------    '''
#                            @doingstuffswithpython

import requests
from urllib.request import urlretrieve,Request,urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse

i=0

url='https://wallpapercave.com/best-2020-anime-wallpapers'

req=Request(url,headers={'User-Agent':'XYZ/5.0'}) # USED IT FOR FAKING NOT BEING A BOT

html= urlopen(req).read()

link_list=[]    #CREATING A LIST TO STORE IMG ADDRESS

data=bs(html,'html.parser')


for link in data.find_all('img'):    # FINDING ALL IMG TAGS

    if link.attrs['src'] not in link_list:    #|----> THESE TWO LINES
        link_list.append(link.attrs['src'])   #|      AVOID REPETITION'''
      
        loc=link.attrs['src']           #GETTING IMG ADDRESS IN LOC
    
        domain='{}://{}'.format(urlparse(url).scheme,urlparse(url).netloc)  #FORMATTING ADDRESS

        image_address='{}{}'.format(domain,loc)

        urlretrieve(image_address,'C:\\Users\\op\\Desktop\\logo\\im{}.png'.format(i)) #GETS THE IMG AND SAVES IT

        i+=1         #ie, img1.png , img2.png , img3.png




