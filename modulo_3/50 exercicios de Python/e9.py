def fatiamento_circular(lista, inicio, fim):
    n = len(lista)
    if inicio <= fim:
        return lista[inicio:fim]
    else:
        return lista[inicio:] + lista[:fim]


l = [0, 1, 2, 3, 4, 5]
print(fatiamento_circular(l, 4, 2))
print(fatiamento_circular(l, 1, 4))
