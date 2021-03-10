import requests
from bs4 import BeautifulSoup as bs

html=requests.get('https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155')

data=bs(html.text,'html.parser')
price_list=[]

books_list=[]

for price in data.find_all('span',class_="a-offscreen"):
    price_list.append(price.get_text())
    
    
for name in data.find_all('div',{alt}):
    print(name.attrs['alt'])


 
