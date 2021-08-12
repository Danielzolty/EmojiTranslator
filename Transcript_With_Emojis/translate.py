from sys import argv

import speech_recognition as sr
from deep_translator import GoogleTranslator
import docx
import emoji as e

e.main()
d = e.dict

# mydoc = docx.Document()

dest_lang = argv[1].lower()
st = argv[2]
# file_name = "file.docx"

array = st.split()
for i in range(len(array)):
    if array[i] in d.keys():
        array[i] = d[array[i]]
s = " ".join(array)

try:
    translated = GoogleTranslator(source='auto', target=dest_lang).translate(s)
    print(translated)
    # mydoc.add_paragraph(translated)
    # mydoc.save(file_name)
    # print(emo.emojify(text))
except:
    print("Sorry, I did not get that")