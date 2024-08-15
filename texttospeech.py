print ("Name: Abhishekkumar Mishra \tRoll No.:08")
from gtts import gTTS
import os
f = open('file2.txt')
x=f.read()
langauge='en'
audio=gTTS(text=x,lang=langauge)
audio.save ("wishes.wav")
os.system("wishes.wav")
print ("Text file converted to audio succesfully.")
