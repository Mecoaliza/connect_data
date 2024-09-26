import os
import pandas as pd

def save_to_excel(df, file_name):
    try:
        if os.path.exists(file_name):
            print(f"O arquivo {file_name} já existe e será atualizado.")
        else:
            print(f"Criando novo arquivo {file_name}.")
        
        df.to_excel(file_name, index=False)
        print(f"O arquivo {file_name} foi salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo {file_name}: {e}")