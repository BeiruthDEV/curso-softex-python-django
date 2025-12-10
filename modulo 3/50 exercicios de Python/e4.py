def manter_numeros(lista):
    return [x for x in lista if isinstance(x, (int, float))]


lista_mista = [1, "olá", 2.5, True, "5", 3]
resultado = manter_numeros(lista_mista)
print(resultado)
