from pytube import YouTube
import os

# Função para baixar um vídeo do YouTube
def download_video(url, output_path):
    # Obtém informações do vídeo em um objeto do tipo Youtube
    yt = YouTube(url)
    # Recupera a maior resolução disponível para o video
    video = yt.streams.get_highest_resolution()
    # Realiza o download do vídeo na pasta definida
    video.download(output_path=output_path)

# Define a pasta onde os vídeos serão baixados
pasta_videos = os.getcwd() + os.sep + "assets" + os.sep + "videos"

# Lê o arquivo de texto com a lista de URLs dos vídeos
with open("lista_videos.txt", "r") as file:
    urls = file.readlines()

# Baixa cada vídeo da lista
for url in urls:
    download_video(url.strip(), pasta_videos)