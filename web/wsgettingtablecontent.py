import csv
import requests
from bs4 import BeautifulSoup as bs

html=requests.get('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
data=bs(html.text,'html.parser')
table=data.findAll('table',{'class':"wikitable sortable"})[0]

rows=table.findAll('tr')
file=open("C:\\Users\\op\\Desktop\\data.csv",'w',encoding='utf=8') 
for row in rows:
    row_content=[]
    for cell in row.findAll(["td","th"]):
       
            row_content.append(cell.get_text())
            writer=csv.writer(file)
            writer.writerow(row_content)
           

