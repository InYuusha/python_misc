from selenium import webdriver as wd

browser=wd.Firefox()
browser.get('http//localhost:8000')

assert 'django'  in browser.title
