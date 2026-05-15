def pesquisa_linear(lista, campo, valor):
   
    resultados = []
    for item in lista:
        
        if valor.lower() in str(item[campo]).lower():
            resultados.append(item)
    return resultados

def pesquisa_binaria(lista, campo, valor):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor_atual = str(lista[meio][campo]).lower()
        valor_procurado = str(valor).lower()
        
        if valor_atual == valor_procurado:
            return [lista[meio]] 
        elif valor_atual < valor_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return []