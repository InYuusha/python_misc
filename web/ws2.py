from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
u="https://www.w3schools.com/html/html_formatting.asp"
html=urlopen(u)

b=bs(html.read(),'html.parser')
name_list=b.findAll('',{'class_':{'pink','red','green'}})
print(" name list=" +str(name_list))

