import uuid

def criar_colmeia(codigo, localizacao, data_instalacao, tipo_mel, email_responsavel):
    
    return {
        "id": str(uuid.uuid4())[:8],
        "codigo": codigo,
        "localizacao": localizacao,
        "data_instalacao": data_instalacao,
        "tipo_mel": tipo_mel,
        "email_responsavel": email_responsavel
    }