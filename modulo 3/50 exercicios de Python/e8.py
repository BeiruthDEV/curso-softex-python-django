def soma_listas(lista1, lista2):
    resultado = []
    for i in range(max(len(lista1), len(lista2))):
        try:
            soma = lista1[i] + lista2[i]
        except IndexError:

            soma = lista1[i] if i < len(lista1) else lista2[i]
        resultado.append(soma)
    return resultado


l1 = [1, 2, 3]
l2 = [4, 5]
print(soma_listas(l1, l2))
