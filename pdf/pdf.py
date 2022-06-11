import PyPDF2

f = open('2.pdf', 'rb')
pdf_read = PyPDF2.PdfFileReader(f)
# print(pdf_read.numPages)
first_page = pdf_read.getPage(0)
# page_one_text = page_one.extractText()
pdf_write = PyPDF2.PdfFileWriter()
pdf_write.addPage(first_page)
pdf_output = open("new.pdf", "wb")
pdf_write.write(pdf_output)
f.close()

