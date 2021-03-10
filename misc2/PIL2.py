from PIL import Image,ImageFilter
img=Image.open("C:\\Users\\op\Desktop\\img.png")
blurry_img=img.filter(ImageFilter.GaussianBlur)
blurry_img.save("C:\\Users\\op\\Desktop\\burred.png")
blurry_img.show()