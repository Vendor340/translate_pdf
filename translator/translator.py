import time
from deep_translator import GoogleTranslator
from PyPDF2 import PdfReader, PdfFileWriter

translator = GoogleTranslator(target="uk")
book = input("Path to book: ")
reader = PdfReader(book)
text_en = ""
text = ""
translate_file = open("translate1.txt", "w")
for page in reader.pages:

    for letter in page.extract_text():

        if letter == "." or letter == "\n":
            print(text)
            try:
                text_en += translator.translate(text)+letter

            except Exception:
                continue
            text = ""
            print(text_en)
            time.sleep(0.5)
        else:
            text += letter
translate_file.write(text_en)
translate_file.close()
