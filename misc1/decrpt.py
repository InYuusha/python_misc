import PyPDF2 as p
pdfreader=p.PdfFileReader(open('C:\\Users\\op\\Desktop\\2pdf\\encrypted.pdf','rb'))
pdfreader.decrypt('qwertyasdzx')
page=pdfreader.getPage(0)
print(page.extractText())
