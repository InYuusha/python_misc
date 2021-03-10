import PyPDF2 as p
pdfreader=p.PdfFileReader(open('C:\\users\\op\\Desktop\\2pdf\\lion.pdf','rb'))
                               
pdfwriter=p.PdfFileWriter()
for numPage in range(pdfreader.numPages):
    pdfwriter.addPage(pdfreader.getPage(numPage))
pdfwriter.encrypt('qwertyasdzx')
result=open('encrypted.pdf','wb')
pdfwriter.write(result)
result.close()

    
