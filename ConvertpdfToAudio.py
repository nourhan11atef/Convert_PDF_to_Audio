import pyttsx3
import pypdf

pdf_file = open('CodeWithNour.pdf','rb')
reader = pypdf.PdfReader(pdf_file, strict=False)
number_of_pages = len(reader.pages)

engine = pyttsx3.init()
for i in range (0,1):
    page = reader.pages[i]
    page_content = page.extract_text()
    rate = 140
    engine.setProperty('rate', rate)
    volume = 1.0
    engine.setProperty('volume', volume)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(page_content)
    engine.save_to_file(page_content, 'pdf_audio.wav')
    engine.runAndWait()
    engine.stop()