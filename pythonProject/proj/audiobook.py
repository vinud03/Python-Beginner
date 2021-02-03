import pyttsx3
import PyPDF2
book = open('Let Us C-Yashwant Kanetkar.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
s=pyttsx3.init()
page=pdfreader.getPage(16)
text=page.extractText()
s.say(text)
s.runAndWait()