import pyttsx3
from pypdf import PdfReader

#extracting text from pdf
reader = PdfReader('OOPs.pdf')
page = reader.pages[5]
text = page.extract_text()

#text to speech
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()