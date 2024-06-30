import os
import speech_recognition as sr
from googleapiclient.discovery import build

# setar a chave de acesso da API do youtube
api_key = "YOUR_API_KEY"
youtube = build('youtube', 'v3', developerKey=api_key)

# define o id do video
video_id = "YOUR_VIDEO_ID"
video_id = "Kgh9TVm4X8s"

# download do audio do video usando youtube-dl
os.system(f"youtube-dl -f 'bestaudio' --output 'audio.%(ext)s' https://www.youtube.com/watch?v={video_id}")

# download do video original
os.system(f"youtube-dl https://www.youtube.com/watch?v={video_id}")

# coverter o audio para o formato wav
os.system("ffmpeg -i audio.webm audio.wav")

# transcrever o audio para texto usando o SpeechRecognition
r = sr.Recognizer()
with sr.AudioFile("audio.wav") as source:
    audio = r.record(source)
    text = r.recognize_google(audio, language="en-US")

# mostra o texto transcrito
print(text)