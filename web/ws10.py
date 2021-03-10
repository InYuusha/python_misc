from urllib.request import urlretrieve
from bs4 import BeautifulSoup as bs
import re
import requests
i=0
html=requests.get("https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155")
data=bs(html.text,'html.parser')
img_loc=data.find_all('img')
for img in img_loc:


    urlretrieve(img,"C:\\Users\\op\\Desktop\\logi{}.jpg".format(i))
    i+=1
    
    
