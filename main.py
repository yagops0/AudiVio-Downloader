import flet as ft
from utilities import utilitarios_ytdlp as uydl

def main(page : ft.Page):
    page.horizontal_alignment="CENTER"
    #page.vertical_alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    page.title = "Audivio Downloader"

    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Diretorio: ", e.path)
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)
    page.update()

    
    txt_centro = ft.Text(
        value = "AUDIVIO DOWNLOADER",
        weight=ft.FontWeight.BOLD,
        theme_style=ft.TextThemeStyle.TITLE_LARGE
    )
    
    txt_title1 = ft.Text(
        value = "Escolha onde seus downloads serão salvos...",
        theme_style=ft.TextThemeStyle.BODY_MEDIUM
    )
    
    escolher_caminho = ft.ElevatedButton(
        "Escolher arquivos",
        on_click=file_picker.get_directory_path()
    )
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    
    page.add(
        txt_centro,
        txt_title1,
        escolher_caminho
    )
    
    
    page.update()

ft.app(target=main)