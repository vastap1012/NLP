import speech_recognition as sr
filename = "C:/Users/VASTA PRITHVI RAJESH/Downloads/NLP Practicals/Practical No 1-20240815T131719Z-001/Practical No 1/Greetings.wav"
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
