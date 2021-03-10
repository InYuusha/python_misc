import PyPDF2 as p
pfile=p.PdfFileReader(open('C:\\Users\\op\\Desktop\\ankush.pdf','rb'))
page=pfile.getPage(0)
text=page.extractText()
print(text)
