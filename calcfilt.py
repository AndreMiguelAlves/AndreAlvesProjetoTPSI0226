def gerar_estatisticas(lista):
    if not lista: return None
    tipos = {}
    for c in lista:
        t = c['tipo_mel']
        tipos[t] = tipos.get(t, 0) + 1
    return {"total": len(lista), "tipos": tipos}

