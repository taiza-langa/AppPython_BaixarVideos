from pytubefix import YouTube

url = input("Digite o link do YouTube: ")

yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
print("Título do vídeo:", yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()
print("Download concluído!")