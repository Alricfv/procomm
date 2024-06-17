mysp=__import__("my-voice-analysis")

p="alrsp" #audio File title

c=r"C:\Users\alric\Music\aud" # Path to the Audio_File directory (Python 3.7

mysp.myspsr(p,c) #rate of speech

mysp.mysppron(p,c) #correct pronounciation percentage

mysp.mysppaus(p,c) #detect the no. of fillers/ pauses

mysp.myspst(p,c) #measure total speaking time

#now for transcription

import speech_recognition as sr

r = sr.Recognizer()

audio_file = sr.AudioFile("alrsp.wav")

with audio_file as source:
    audio = r.record(source)

raizen = r.recognize_google(audio)

print(raizen , file=open('outpu.txt' , 'a'))

#now to summarize this text

import bs4 as bs
import urllib.request
import re

scraped_data = r"outpu.txt"
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text
