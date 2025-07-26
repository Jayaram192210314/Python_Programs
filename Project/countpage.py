import PyPDF2
file = open('D:\\VS_Code\\Python\\Project\\Dev.pdf','rb')
PdfReader = PyPDF2.PdfReader(file)
totalPages = len(PdfReader.pages)
print(f"Total Pages: {totalPages}")