from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
data=bs(html ,'html.parser')
for child  in data.find('table',{'id':'giftList'}).tr:
     print(child)
