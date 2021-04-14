import speech_recognition as sr
from nameFinder2 import extract_names
from record import recordWav
from Search import searcher
import simpleaudio as sa
from speaker import speakerOut

#from punctuator import Punctuator
#file = '/Users/xaviernavarro/PycharmProjects/Speech2Text/assets/recorded3.wav'
#file = str(recordWav())
file = "assets/recorded3.wav"
def fanboyRule(text):
    text = text.replace(' and ', ',and ')
    text = text.replace(' nor ', ',nor ')
    text = text.replace(' but ', ',but ')
    text = text.replace(' or ', ',or ')
    text = text.replace(' yet ',',yet ')
    return text

r = sr.Recognizer()
r.recognize_google

harvard = sr.AudioFile(file)
with harvard as source:
    audio = r.record(source)

text = r.recognize_google(audio)
#text = fanboyRule(text)
#p = Punctuator('/Users/xaviernavarro/PycharmProjects/Speech2Text/assets/model/INTERSPEECH-T-BRNN-pre.pcl')
#newText = p.punctuate(text)
#print(newText)

wave_obj = sa.WaveObject.from_wave_file(file)
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing

#print(extract_names(newText))

print(text)
answer = searcher(text)
speakerOut(answer)
