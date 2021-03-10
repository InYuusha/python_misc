import requests
cred={'Email':'asuse975@gmail.com'}
r=requests.post("https://get.oreilly.com/email-signup.html?utm_medium=email&utm_source=oreilly.com&utm_campaign=na&utm_content=20180518+ipost+redirect",data=cred)
print(r.text)
      
      

      
