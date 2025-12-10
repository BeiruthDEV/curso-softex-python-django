import random


def filtro_random(lista, n):
    try:
        return random.sample(lista, n)
    except ValueError:
        print(f"Erro: n={n} maior que o tamanho da lista ({len(lista)})")
        return []


l = [10, 20, 30, 40, 50]
print(filtro_random(l, 3))
print(filtro_random(l, 10))
