from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
data=bs(html,'html.parser')
all_tags=data.findAll(lambda ta:ta.get_text()=="something")
print(all_tags)
images=data.findAll('img',{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    print(image['src'])