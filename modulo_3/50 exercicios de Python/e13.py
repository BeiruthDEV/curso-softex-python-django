def gerar_metadados(dic):
    return {
        k: {"tipo": type(v).__name__, "tamanho_chave": len(k), "é_par": v % 2 == 0}
        for k, v in dic.items()
        if isinstance(v, (int, float))
    }


print(gerar_metadados({"um": 1, "dois": 2, "tres": 3}))
