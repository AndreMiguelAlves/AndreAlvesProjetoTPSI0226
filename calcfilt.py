def gerar_estatisticas(lista):
    if not lista: return None
    tipos = {}
    for c in lista:
        t = c['tipo_mel']
        tipos[t] = tipos.get(t, 0) + 1
    return {"total": len(lista), "tipos": tipos}

def filtrar_por_local(lista, local):
    return [c for c in lista if local.lower() in c['localizacao'].lower()]