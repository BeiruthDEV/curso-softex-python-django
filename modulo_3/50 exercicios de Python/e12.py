def inverter_filtrar_dict(d):
    
    return {v: k for k, v in d.items() if isinstance(v, str) and len(v) > 5}


d = {
    "a": "banana",
    "b": "maçã",
    "c": "abacaxi",
    "d": 12345
}

resultado = inverter_filtrar_dict(d)
print(resultado)

