def adicionar_permissao(dic, usuario, permissao):
    if usuario in dic:
        if permissao not in dic[usuario]:
            dic[usuario].append(permissao)
    else:
        dic[usuario] = [permissao]
    return dic
