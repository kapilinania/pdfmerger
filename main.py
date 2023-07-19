import PyPDF2

# first module import
pdfiles = ["1.pdf", "2.pdf"]
# create pdf colletion
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')
# final merge pdf name
