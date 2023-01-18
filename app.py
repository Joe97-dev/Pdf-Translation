#Write the translated text into a pdf
output.addPage(PyPDF2.PageObject.create_blank_page())
output.getPage(0).writeText(translate_text)

with open ("translated.pdf", 'wb') as output_file:
    output.write(output_file)