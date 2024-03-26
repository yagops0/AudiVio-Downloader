# AUDIVIO YOUTUBE DOWNLOADER

## O QUE QUERO
- Três telas
    - Tela Inicial
        - Mostra uma introdução ao programa.
    - Tela de realização de downloads
        - Onde serão feitos os downloads de vídeos, músicas e playlists
    - Tela de Arquivos
        - Tela que mostra todos os downloads feitos.
- Função para trocar o tema do programa
- Possibilidade de escolher a resolução que deseja do vídeo
- Dar a possibilidade de escolher se deseja criar uma pasta nova para armazenar os downloads, ou usar a padrão(que será decidido pelo programa, provavelmente a pasta de músicas do computador)
- Baixar Vídeo e Áudio ou apenas áudio.
- Usar appbar para opções da tela do flet
- Usar progressBar para feedback do download do vídeo/música.
- Opção para vídeo, música, playlist vídeo/música
- Usar Radio para escolher as opções de download

## CLASSES/MÓDULOS
- yt-dlp
    - YoutubeDL
- OS
    - Tudo
- Flet
    - Tudo

## FUNÇÕES
- baixar_video_padrao(url)
- baixar_vido_escolha(url, caminho, nome_arquivo)
- criar_pasta_audio()
- retornar_arquivos_baixados(diretorio : str)

## EXEMPLOS

- Vídeo Teste
    - chachorro mortal -  https://www.youtube.com/watch?v=j1_HaVIqgZo
    - ayane lov u - https://www.youtube.com/watch?v=S71qIOTRVi0

- Caminho Teste
    - C:/Users/yagos/Music

## FUNCIONALIDADES

- Na tela principal será feita uma introdução, falando sobre o programa, e antes de iniciar o programa, pedir ao usuário onde os downloads serão guardados, mostrando algumas opções como por exemplo pedir que o programa crie uma pasta ou pedir para que o usuário cole um caminho para uma pasta de sua preferência.

