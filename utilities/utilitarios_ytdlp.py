import yt_dlp as ydl
import os

def baixar_video(url, caminho, resolucao):
    try:
        if resolucao == "360": # SD
            ydl_opts = {
                'format' : f'mp4/bestvideo[height<=360]+bestaudio[height<=360]/best',
                'outtmpl' : f'{caminho}/%(title)s.%(ext)s'
            }
            
            with ydl.YoutubeDL(ydl_opts) as video:
                video.download([url])
        elif resolucao == "720": # HD
            ydl_opts = {
                'format' : f'mp4/bestvideo[height<=720]+bestaudio[height<=720]/best',
                'outtmpl' : f'{caminho}/%(title)s.%(ext)s'
            }
            
            with ydl.YoutubeDL(ydl_opts) as video:
                video.download([url])
        elif resolucao == "1080": # FULL HD
            ydl_opts = {
                'format' : f'mp4/bestvideo[height<=1080]+bestaudio[height<=1080]/best',
                'outtmpl' : f'{caminho}/%(title)s.%(ext)s'
            }
            
            with ydl.YoutubeDL(ydl_opts) as video:
                video.download([url])
        
        return True
    except ydl.DownloadError:
        return False
        
    

def baixar_musica(url, caminho):
    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }],
        'ignoreerrors' : True,
        'outtmpl' : f'{caminho}/%(title)s.%(ext)s'
    }
    
    with ydl.YoutubeDL(ydl_opts) as audio:
        audio.download([url])


def baixar_playlist_videos(url_playlist, caminho):
    ydl_opts = {
        'format' : 'mp4/bestvideo+bestaudio/best',
        'outtmpl' : f'{caminho}/%(title)s.%(ext)s',
        'ignoreerrors' : True
    }
    
    with ydl.YoutubeDL(ydl_opts) as playlist_video:
        playlist_video.download([url_playlist])


'''def baixar_playlist_musicas(url_playlist, caminho):
    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }],
        'outtmpl' : f'{caminho}/%(title)s.%(ext)s'   
    }
    
    with ydl.YoutubeDL(ydl_opts) as playlist_musica:
        playlist_musica.download([url_playlist])'''

