import os
import PyPDF2
from gtts import gTTS
from tqdm import trange
from time import sleep

# Progress of conversion
def progress():
    for i in trange(100, desc ="Progress: "):
        sleep(.5)
            
# Open the PDF file 
with open('document.pdf', 'rb') as file:
    # Create a PDF object
    reader = PyPDF2.PdfFileReader(file)

    # Iterate over every page in the PDF
    for page in range(reader.getNumPages()):
        text = reader.getPage(page).extractText()
        
        # Convert the text to audio format
        audio = gTTS(text)
        
        # Progress Bar
        progress()
        
        audio.save(f'Generated Speech.mp3')
        