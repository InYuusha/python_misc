import requests as s
import urllib.parse as up

raw_string="Hello world"
print(up.quote(raw_string))
print(up.quote_plus(raw_string))
