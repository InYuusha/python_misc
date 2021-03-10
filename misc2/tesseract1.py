from PIL import Image
import pytesseract as pt
from pytesseract import Output
pt.pytesseract.tesseract_cmd="C://Program Files//Tesseract-OCR//tesseract.exe"
print(pt.image_to_string(Image.open("C://Users//op//Desktop//ur.png"),lang='eng'))
