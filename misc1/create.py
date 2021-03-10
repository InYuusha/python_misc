from PIL import Image ,ImageDraw,ImageFont
img=Image.new('RGBA',(500,400),'BLACK')

draw=ImageDraw.Draw(img)
draw.text((200,250),'this is the way',fill='purple')
draw.rectangle((200,200,300,400),fill='blue',outline='red')
img.save('C:\\Users\\op\\Desktop\\create.png')
