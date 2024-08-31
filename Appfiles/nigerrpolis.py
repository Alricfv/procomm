import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 10  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('outp.wav', fs, myrecording)  # Save as WAV file

mysp=__import__("my-voice-analysis")

p="outp" #audio File title

c=r"C:\Users\alric\Music\aud\mp3recor" # Path to the Audio_File directory (Python 3.7

mysp.myspsr(p,c) #rate of speech

mysp.mysppron(p,c) #correct pronounciation percentage

mysp.mysppaus(p,c) #detect the no. of fillers/ pauses

mysp.myspst(p,c) #measure total speaking time


#now for transcription

import whisper

model = whisper.load_model("medium")
result = model.transcribe(r"C:\Users\alric\Music\aud\mp3recor\outp.wav", fp16=False)
print(result["text"])
