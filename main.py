import flet as ft
from utilities import utilitarios_ytdlp as uydl
from utilities import utilitarios_os as uos

def main(page : ft.Page):
    page.title = "Audivio Downloader"   
    page.horizontal_alignment="CENTER"
    #page.vertical_alignment=ft.MainAxisAlignment.SPACE_AROUND
    
    opcao_caminho : int
    
    def on_click_usuario(e):
        criar_pasta = uos.criar_pasta_usuario(txtField_caminho_usuario.value, txtField_nome_pasta.value)
        if not txtField_caminho_usuario.value:
            txtField_caminho_usuario.error_text = "Por favor escolha o caminho"
        else:
            if not txtField_nome_pasta.value:     
                txt_diretorio.value = f"Downloads em: {txtField_caminho_usuario.value}"
            else:
                txt_diretorio.value = f"Downloads em: {txtField_caminho_usuario.value}\\{txtField_nome_pasta.value}"
                
        page.update()
        
    def on_click_sd(e):
        if btn_continuar.data:
            if uydl.baixar_video(txtField_colar_url.value, f"{txtField_caminho_usuario.value}\\{txtField_nome_pasta.value}", "360"):
                print("Download concluído")
    
    def on_click_hd(e):
        if btn_continuar.data:
            if uydl.baixar_video(txtField_colar_url.value, f"{txtField_caminho_usuario.value}\\{txtField_nome_pasta.value}", "720"):
                print("Donwloada HD.")

    def on_click_full_hd(e):
        if btn_continuar.data:
            if uydl.baixar_video(txtField_colar_url.value, f"{txtField_caminho_usuario.value}\\{txtField_nome_pasta.value}", "1080"):
                print("Donwload FULL HD.")
    
    def on_click_musica(e):
        if btn_continuar.data:
            if uydl.baixar_musica(txtField_colar_url.value, f"{txtField_caminho_usuario.value}\\{txtField_nome_pasta.value}"):
                print("Musica baixada.")
    
    def on_click_playlist_musica(e):
        if btn_continuar.data:
            if uydl.baixar_musica(txtField_colar_url.value, f"{txtField_caminho_usuario.value}\\{txtField_nome_pasta.value}"):
                print("Playlist baixada.")
    
    def on_click_playlist_video(e):
        if btn_continuar.data:
            if uydl.baixar_video(txtField_colar_url.value, f"{txtField_caminho_usuario.value}\\{txtField_nome_pasta.value}", "1080"):
                print("Playlist video baixada.")
    
    def cancelar_modal(e):
        alert_erro.open = False
        page.update()
        
    txt_diretorio = ft.Text()
    
    
    txt_centro = ft.Text(
        value = "AUDIVIO DOWNLOADER",
        weight=ft.FontWeight.BOLD,
        theme_style=ft.TextThemeStyle.TITLE_LARGE
    )
    
    txt_title1 = ft.Text(
        value = "Escolha onde seus downloads serão salvos...",
        theme_style=ft.TextThemeStyle.BODY_MEDIUM
    )
    
    txtField_caminho_usuario = ft.TextField(
        label="Digite ou cole o caminho onde os downloads serão salvos"
    )
    
    txtField_nome_pasta = ft.TextField(
        label="Digite o nome na pasta(caso não queira criar uma pasta, não é necessário colocar um nome)"
    )
    
    txtField_colar_url = ft.TextField(
        label="Cole a url do vídeo/música ou playlist"
    )
    
    
    btn_continuar = ft.ElevatedButton(
        "Continuar com caminho escolhido",
        on_click=on_click_usuario, data=True
    )
    

    btn_sd = ft.ElevatedButton(
        "SD",
        on_click=on_click_sd
    )
    
    btn_hd = ft.ElevatedButton(
        "HD",
        on_click=on_click_hd
    )
    
    btn_full_hd = ft.ElevatedButton(
        "FULL HD",
        on_click=on_click_full_hd
    )
    
    btn_musica = ft.ElevatedButton(
        ".MP3", 
        on_click=on_click_musica
    )
    
    btn_playlist_musica = ft.ElevatedButton(
        "Playlist Música",
        on_click=on_click_playlist_musica    
    )
    
    btn_playlist_video = ft.ElevatedButton(
        "Playlist Vídeo",
        on_click=on_click_playlist_video
    )
    
    pb_download = ft.ProgressBar(width=500)
    
    conteudo_pb = ft.Column([
        ft.Text("Fazendo o download..."),
        pb_download
    ])
    
    alert_erro = ft.AlertDialog(
            modal=True,
            content=ft.Text("Não foi possível criar a pasta, por favor tente novamente."),
            actions=[
                ft.TextButton("Ok", on_click=cancelar_modal)
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
     
    page.add(
        txt_centro,
        txt_title1,
        txtField_caminho_usuario,
        txtField_nome_pasta,
        btn_continuar,
        txt_diretorio,
        txtField_colar_url,
        btn_sd,
        btn_hd,
        btn_full_hd,
        btn_musica,
        btn_playlist_musica,
        btn_playlist_video,
        pb_download
    )
    
    
    page.update()

ft.app(target=main)