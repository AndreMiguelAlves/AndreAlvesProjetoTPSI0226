import uuid

def criar_colmeia(codigo, localizacao, data_instalacao, tipo_mel, email_responsavel):
    # Gera ID único automático 
    return {
        "id": str(uuid.uuid4())[:8],
        "codigo": codigo,
        "localizacao": localizacao,
        "data_instalacao": data_instalacao,
        "tipo_mel": tipo_mel,
        "email_responsavel": email_responsavel
    }

def atualizar_colmeia(colmeias, id_alvo, novos_dados):
    for i, colmeia in enumerate(colmeias):
        if colmeia['id'] == id_alvo:
            novos_dados['id'] = id_alvo
            colmeias[i] = novos_dados
            return True
    return False

def eliminar_colmeia(colmeias, id_alvo):
    for i, colmeia in enumerate(colmeias):
        if colmeia['id'] == id_alvo:
            colmeias.pop(i)
            return True
    return False