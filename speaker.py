# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

def speakerOut(mytext):
    # The text that you want to convert to audio
    #mytext = 'Welcome to geeksforgeeks!'
    if (mytext == ""):
        mytext = "Sorry. I could not get you"

    # Language in which you want to convert
    #ACCENT
    language = 'zh-TW'
    # ACCENT
    accent = 'zh-CN'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False,tld=accent )
    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("assets/welcome.mp3")

    # Playing the converted file
    os.system("mpg321 assets/welcome.mp3")
    return "succesfully completed"
