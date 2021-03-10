import requests
data={'uploadFile':open('C:\\Users\\op\\Desktop\\logi.jpg','rb')}
r=requests.post("http://www.pythonscraping.com/pages/files/processing2.php",files=data)
print(r.text)
