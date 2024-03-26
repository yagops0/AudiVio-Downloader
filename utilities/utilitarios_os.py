import os


def criar_pasta_programa(caminho):
    raiz = f"{caminho}/Audivio/Downloads"
    lista = ['Audivio Videos', 'Audivio Audios']
    try:
        for dire in lista:
            path = os.path.join(raiz, dire)
            os.makedirs(path)
        return True
    
    except OSError as oerr:
        print(f"Erro: {oerr}")

def criar_pasta_usuario(caminho, nome_pasta):
    try: 
        os.mkdir(f"{caminho}/{nome_pasta}")
        return True
    except OSError:
        return False

def retornar_arquivos(caminho):
    try:
        arquivos = os.listdir(caminho)
        
        for i in arquivos:
            print(i)
        return True
    except OSError:
        return False

