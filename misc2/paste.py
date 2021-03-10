import pyperclip as p
text=p.paste()

lines=text.split('.')
for i in range(len(lines)):
    lines[i]= '*' +lines[i]
text='/n'.join(lines)
p.copy(text)
print(text)
    

    
