import requests
url='https://www.edhitch.com/login.html/?query=edhitch'
r=requests.get(url)
print(r.text)
#print(r.request.url)
#print(r.status_code)#200
#print(r.reason) #OK
#print(r.headers)
