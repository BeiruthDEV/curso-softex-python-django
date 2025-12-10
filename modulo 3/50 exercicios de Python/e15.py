import random


def remover_aleatorios(dic):
    try:
        for chave in random.sample(list(dic.keys()), 3):
            dic.pop(chave)
    except ValueError:
        dic.clear()
    return dic
