def pesquisa_linear(lista, campo, valor):
   
    resultados = []
    for item in lista:
        
        if valor.lower() in str(item[campo]).lower():
            resultados.append(item)
    return resultados

