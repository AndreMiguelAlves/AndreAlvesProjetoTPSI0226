import json
import os

FICHEIRO_DADOS = "colmeias.json"

def guardar_dados(lista_colmeias):
    
    try:
        with open(FICHEIRO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(lista_colmeias, f, indent=4, ensure_ascii=False)
        print("\n[Sucesso] Dados guardados com êxito!")
    except Exception as e:
        print(f"\nFalha ao guardar dados: {e}")

def carregar_dados():
    
    if not os.path.exists(FICHEIRO_DADOS):
        return []
    try:
        with open(FICHEIRO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"\nFalha ao carregar dados: {e}")
        return []