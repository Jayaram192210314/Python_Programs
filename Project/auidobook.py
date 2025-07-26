import pyttsx3
import PyPDF2

file = open('E:\\VS_Code\\Python\\Project\\Dev.pdf','rb')
pdf_read = PyPDF2.PdfReader(file)
k = len(pdf_read.pages)

play = pyttsx3.init()
print('Playing PDF File')
for i in range (0,k):  
    print(i)
    choose_page = pdf_read.pages[i]
    pdf_text = choose_page.extract_text()
    play.say(pdf_text)
    print(pdf_text)
    play.runAndWait()