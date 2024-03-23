import yt_dlp as ydl
from utilities import utilitarios_ytdlp as uydl

#help(ytp)

try:
    '''ydl_opts = {
        'format' : 'best[height<=144]/mp4',
        'outtmpl' : 'C:/Users/yagos/Music/%(title)s.%(ext)s'
    }
    url = "https://www.youtube.com/watch?v=S71qIOTRVi0"
    
    video = ydl.YoutubeDL(ydl_opts)
    video.download([url])'''
    
    uydl.baixar_video("https://www.youtube.com/watch?v=FKlGHHhTOsQ", "C:/Users/yagos/Music/", "1080")
    
except ydl.DownloadError as derr:
    print(f"Erro: {derr}")
    
    
