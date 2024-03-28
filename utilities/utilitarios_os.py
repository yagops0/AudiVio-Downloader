import os


def criar_pasta_programa():
    raiz = "C:/AudiVio/Downloads"
    lista = ['AudiVio Videos', 'AudiVio Audios']
    try:
        for dire in lista:
            path = os.path.join(raiz, dire)
            os.makedirs(path)
        return True
    
    except OSError as oerr:
        print(f"Erro: {oerr}")
        return False

def criar_pasta_usuario(caminho, nome_pasta):
    try: 
        os.mkdir(f"{caminho}/{nome_pasta}")
        return True
    except OSError:
        return False
    
def verificar_caminho_existe():
    if os.path.exists("C:/AudiVio/Downloads"):
        return True
    else:
        return False

def salvar_pastas_certas(tipo):
    if verificar_caminho_existe():
        if tipo == "Vídeo":
            return "C:/AudiVio/Downloads/AudiVio Videos"
        elif tipo == "Música":
            return "C:/AudiVio/Downloads/AudiVio Audios"
    else:
        return 

def retornar_arquivos(caminho):
    try:
        arquivos = os.listdir(caminho)
        
        for i in arquivos:
            print(i)
        return True
    except OSError:
        return False

