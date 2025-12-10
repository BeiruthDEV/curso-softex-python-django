def soma_condicional(dic, letra):
    soma = 0
    for chave, valor in dic.items():
        try:
            if chave.startswith(letra):
                soma += valor
        except TypeError:
            pass
    return soma
