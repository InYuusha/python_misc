import pytesseract
from PIL import Image

def clean_image(orignal_path,new_path):
    
    img=Image.open(orignal_path)
    img=img.point(lambda x: 0 if x<90 else 255)    #thresholding
    img.save(new_path)
    return img
    
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"   

clean_image=clean_image("C:\\Users\\op\\Desktop\\ocr.png","C:\\Users\\op\\Desktop\\clean.png")

print(pytesseract.image_to_string(clean_image))

