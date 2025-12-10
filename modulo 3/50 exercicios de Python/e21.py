class ItemInventario:
    def __init__(self, nome, quantidade, valor_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def valor_total(self):
        return self.quantidade * self.valor_unitario


item = ItemInventario("Mouse", 10, 50.0)
print(item.valor_total())
