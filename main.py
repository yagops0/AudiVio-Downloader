import flet as ft
from utilities import utilitarios_ytdlp as uydl
from utilities import utilitarios_os as uos

def main(page : ft.Page):
    page.title = "Audivio Downloader"   
    page.horizontal_alignment="CENTER"
    #page.vertical_alignment=ft.MainAxisAlignment.SPACE_AROUND
    
    
    def on_click_usuario(e):
        criar_pasta = uos.criar_pasta_usuario(txtField_caminho_usuario.value, txtField_nome_pasta.value)
        if not txtField_caminho_usuario.value:
            txtField_caminho_usuario.error_text = "Por favor escolha o caminho"
        if not txtField_nome_pasta.value:
            txtField_nome_pasta.error_text = "Por favor digite o nome da pasta"
        else:
            if criar_pasta:
                txt_diretorio.value = f"Downloads em: {txtField_caminho_usuario.value}\\{txtField_nome_pasta.value}"
        page.update()
        
    def on_click_programa(e):
        criar_pasta = uos.criar_pasta_programa()
        if criar_pasta:
            txt_diretorio.value = f"Downloads em: C:\\Audivio\\Downloads"
        page.update()
    
    def cancelar_modal(e):
        alert_erro.open = False
        page.update()
    
    def radiogroup_changed(e):
        if radio_opcoes.value == "Vídeo":
            ft.RadioGroup()
        
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
        label="Digite o nome na pasta"
    )
    
    txtField_colar_url = ft.TextField(
        label="Cole a url do vídeo/música"
    )
    
    
    btn_continuar = ft.ElevatedButton(
        "Continuar com caminho escolhido",
        on_click=on_click_usuario
    )
    
    txt_ou = ft.Text(
        value="OU"
    )
    
    btn_app = ft.ElevatedButton(
        "Deixar que o programa crie a pasta",
        on_click=on_click_programa
    )
    
    alert_erro = ft.AlertDialog(
            modal=True,
            content=ft.Text("Não foi possível criar a pasta, por favor tente novamente."),
            actions=[
                ft.TextButton("Ok", on_click=cancelar_modal)
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
    
    radio_opcoes = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="Vídeo", label="Vídeo"),
                ft.Radio(value="Música", label="Música"),
                ft.Radio(value="Playlist Vídeo", label="Playlist Vídeo"),
                ft.Radio(value="Playlist Música", label="Playlist Música")
            ]
        )
    )
    
    
    page.add(
        txt_centro,
        txt_title1,
        txtField_caminho_usuario,
        txtField_nome_pasta,
        btn_continuar,
        txt_ou,
        btn_app,
        txt_diretorio,
        txtField_colar_url,
        radio_opcoes
    )
    
    
    page.update()

ft.app(target=main)