import pyttsx3
import PyPDF2

file = open('D:\\VS_Code\\Python\\Project\\PP.pdf','rb')
pdf_read = PyPDF2.PdfReader(file)
k = len(pdf_read.pages)

play = pyttsx3.init()
print('Playing PDF File')
choose_page = pdf_read.pages[0]
pdf_text = choose_page.extract_text()
play.say(pdf_text)
play.runAndWait()