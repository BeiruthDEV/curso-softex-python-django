def maior_sequencia(lista):
    max_atual = max_global = lista[0]
    for num in lista[1:]:
        max_atual = max(num, max_atual + num)
        max_global = max(max_global, max_atual)
    return max_global


numeros = [1, -2, 3, 5, -1, 2]
resultado = maior_sequencia(numeros)
print(resultado)
