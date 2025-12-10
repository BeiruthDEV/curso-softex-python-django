def transpor_matriz(matriz):
    return [[linha[i] for linha in matriz] for i in range(len(matriz[0]))]


matriz = [[1, 2, 3], [4, 5, 6]]
resultado = transpor_matriz(matriz)
print(resultado)
