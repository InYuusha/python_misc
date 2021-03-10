
import re

s=re.compile('\w+')

string="I love sleeping"

sep=s.findall(string)

print(sep)

print("hello world")
