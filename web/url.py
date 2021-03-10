from urllib.request import urlopen
link="https://www.geeksforgeeks.org/create-copy-move-gui-using-tkinter-in-python/"

http=urlopen(link)
print(http)
html=http.read()
print(html)
hd=html.decode()
print(hd)
    
