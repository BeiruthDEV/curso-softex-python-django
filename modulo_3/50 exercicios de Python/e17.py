d = {"a": 3, "b": 7, "c": 1}
ordenado = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(ordenado)
