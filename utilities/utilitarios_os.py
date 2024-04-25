import os

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

