import PyPDF2 as p
pdfreader=p.PdfFileReader(open('C:\\Users\\op\\Desktop\\2pdf\\7901 Fundamentals of Photography.pdf','rb'))
page=pdfreader.getPage(0)
pdfreader1=p.PdfFileReader(open('C:\\Users\\op\\Desktop\\2pdf\\11_chapter 5.pdf','rb'))
page1=pdfreader1.getPage(0)
page.mergePage(page1)
pdfwriter=p.PdfFileWriter()
pdfwriter.addPage(page)

for numPages in range(1,pdfreader.numPages):
    pageobj=pdfreader.getPage(numPages)
    pdfwriter.addPage(pageobj)
result=open('watermarked.pdf','wb')
pdfwriter.write(result)
result.close()

result1=p.PdfFileReader(open('watermarked.pdf','rb'))
page2=result1.getPage(0)
print(page.getContents())



                          
                          
