def duplicatas(lista):
    contagem = {}
    for item in lista:
        contagem[item] = contagem.get(item, 0) + 1
    return [(item, freq) for item, freq in contagem.items() if freq > 1]


lista = [1, 2, 2, 3, 3, 3, 4]
resultado = duplicatas(lista)
print(resultado)
