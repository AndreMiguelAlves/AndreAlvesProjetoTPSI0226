def bubble_sort(lista, campo, crescente=True):
    n = len(lista)
    res = lista[:]
    for i in range(n):
        for j in range(0, n - i - 1):
            v1 = str(res[j][campo]).lower()
            v2 = str(res[j+1][campo]).lower()
            if (v1 > v2 if crescente else v1 < v2):
                res[j], res[j+1] = res[j+1], res[j]
    return res

