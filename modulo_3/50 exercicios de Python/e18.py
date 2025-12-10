def atualizar_dic():
    dic = {}
    while True:
        chave = input("Chave: ")
        if not chave:
            break
        valor = input("Valor: ")
        try:
            dic[chave] = valor
        except Exception as e:
            print(f"Erro: {e}")
    print(dic)
