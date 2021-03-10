import PyPDF2 as p
pfile=p.PdfFileReader(open('C:\\Users\\op\\Desktop\\Ankush Singh Bhagaur.pdf','rb'))
page=pfile.getPage(0)
page.rotateClockwise(90)

npfile=p.PdfFileWriter()
npfile.addPage(page)
resultpdf=open('rotated.pdf','wb')
npfile.write(resultpdf)
resultpdf.close()

jfile=p.PdfFileReader(open('rotated.pdf','rb'))
jpage=jfile.getPage(0)
print(jpage.extractText())


 


#nwpdf=p.PdfFileReader(open('rotated.pdf','rb'))
#nwpage=nwfile.getpage(0)
#print(nwpage.extractText())

                      


