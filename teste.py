import yt_dlp as ydl
from utilities import utilitarios_ytdlp as uydl
from utilities import utilitarios_os as uos


#help(ytp)

try:
    '''ydl_opts = {
        'format' : 'best[height<=144]/mp4',
        'outtmpl' : 'C:/Users/yagos/Music/%(title)s.%(ext)s'
    }
    url = "https://www.youtube.com/watch?v=S71qIOTRVi0"
    
    video = ydl.YoutubeDL(ydl_opts)
    video.download([url])'''
    
    #uydl.baixar_video("https://www.youtube.com/watch?v=FKlGHHhTOsQ", "C:/Users/yagos/Music/", "1080")
    
    #uydl.baixar_musica("https://www.youtube.com/watch?v=S71qIOTRVi0", "C:/Users/yagos/Music/")
    
    #uydl.baixar_playlist_videos("https://youtube.com/playlist?list=PLSptejTZ0klP6Oi2njvyNfLV9Ap8n8rry&si=eHSiCgXSqzbWN6Xp", "C:/Users/yagos/Music/")
    
    #uydl.baixar_playlist_musicas("https://youtube.com/playlist?list=PLSptejTZ0klP6Oi2njvyNfLV9Ap8n8rry&si=eHSiCgXSqzbWN6Xp", "C:/Users/yagos/Music/")
    
except ydl.DownloadError as derr:
    print(f"Erro: {derr}")
    
    
#uos.criar_pasta("teste")

#uos.retornar_arquivos("C:/Users/yagos/Music/MusicasYago")

#cam = str(input("Digite o caminho: "))
'''opcao = str(input("Digite uma opção: "))

if uos.criar_pasta_usuario(cam, opcao):
    print("pasta criada!!")
else:
    print("erro")'''
    
'''if uos.criar_pasta_programa():
    print("Pasta criada")
else:
    print("erro")'''

#uos.verificar_caminho_existe()
