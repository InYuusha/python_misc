from PIL import Image as im,ImageDraw
obj=im.new('RGBA',(1080,1080))
draw=ImageDraw.Draw(obj)
draw.rectangle((500,300,700,500))



obj.show()
