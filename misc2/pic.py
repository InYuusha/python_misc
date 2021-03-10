from PIL import Image
img=Image.open('C:\\New folder\\ANIME\\zeldoris_001___BW4qKavAlcP___.jpg')
width,height=img.size
print(width,height)
print(img.filename)
print(img.format_description)

