from gtts import gTTS

# arquivos de texto que será convertido em áudio
text_file = 'example.txt'

# arquivo de áudio que será gerado
audio_file = 'output.mp3'

# Lê o arquivo de texto
with open(text_file, 'r') as file:
    text = file.read()

# instanciar um objeto gTTS e gerar o áudio
tts = gTTS(text=text, lang='pt-br', tld='com.br')
tts.save(audio_file)

print(f"Texto convertido em áudio. Áudio salvo como {audio_file}")