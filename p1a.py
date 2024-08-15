from gtts import gTTS
import os
f = open("C:/NLP/file.txt")
x=f.read()
langauge='en'
audio=gTTS(text=x,lang=langauge)
audio_save("‪C:/NLP/wishes.wav")
os.system("‪C:/NLP/wishes.wav")
print("program executed succesfully.")
