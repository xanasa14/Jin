import speech_recognition as sr
print(sr.__version__)
import simpleaudio as sa

file = '/Users/xaviernavarro/PycharmProjects/Speech2Text/assets/audio_files_harvard.wav'
file = '/Users/xaviernavarro/PycharmProjects/Speech2Text/assets/recorded.wav'

r = sr.Recognizer()
r.recognize_google

harvard = sr.AudioFile(file)
with harvard as source:
    audio = r.record(source)

text = r.recognize_google(audio)
print(text)


wave_obj = sa.WaveObject.from_wave_file(file)
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing
