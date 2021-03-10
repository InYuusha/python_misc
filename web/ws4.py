from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
data=bs(html,'html.parser')
print(data.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())