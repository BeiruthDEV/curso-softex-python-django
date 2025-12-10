def contagem_palavras(texto):
    palavras = texto.split()
    contagem = {}

    for palavra in palavras:
        try:
            contagem[palavra] += 1
        except KeyError:
            contagem[palavra] = 1
    return contagem


texto = "casa bolo casa amigo bolo bolo"
resultado = contagem_palavras(texto)
print(resultado)
