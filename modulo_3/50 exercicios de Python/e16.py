def flatten(dic):
    novo = {}
    for k, v in dic.items():
        if isinstance(v, dict):
            for subk, subv in v.items():
                novo[f"{k}_{subk}"] = subv
        else:
            novo[k] = v
    return novo
