import requests
from bs4 import BeautifulSoup as bs

html=requests.get("http://oreilly.com")
data=bs(html.text,"html.parser")
all_tags=data.select('h1')

f="\n".join(tag.get_text() for tag in all_tags)
print(f)