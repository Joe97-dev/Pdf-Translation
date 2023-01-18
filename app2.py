import PyPDF2
from googletrans import Translator
import warnings
warnings.filterwarnings("ignore")


#Open the PDF fILE
#with open ('pdf_52.pdf', 'rb') as pdf_file:
    #pdf_reader = PyPDF2.PdfReader(pdf_file)

pdf_file = open('pdf_52.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

#Extracting text from pdf
for p in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[p]
    text = page.extract_text()
    print (text)


#Translate the text into swahili
#Use google Translate API to convert into any language

    translator = Translator()
    translate_text = translator.translate(text, dest ='fr')

    print(translate_text)

#Create a new PDF with the translated text
output = PyPDF2.PdfWriter()

#Write the translated text into a pdf
output.addPage(PyPDF2.PageObject.create_blank_page())
output.getPage(0).writeText(translate_text)

with open ("translated.pdf", 'wb') as output_file:
    output.write(output_file)

    







