import PyPDF2 as p
pdffile=p.PdfFileReader(open('C:\\Users\\op\\Desktop\\practical ankush-converted.pdf','rb'))
c=pdffile.numPages
print(c)
print(pdffile.isEncrypted)
                        
