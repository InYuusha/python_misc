from PIL import Image as i
img=i.open('C:\\Users\\op\\Desktop\\zeldoris_001___BfdzUJHFzy-___.jpg')
for i in range(100):
    for j in range(50):
        img.putpixel((j,i),(210,210,210))
img.save('C:\\Users\\op\\Desktop\\new.png')        
