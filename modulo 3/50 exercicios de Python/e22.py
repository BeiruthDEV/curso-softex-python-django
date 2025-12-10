from e21 import ItemInventario

class Perecivel(ItemInventario):
    def __init__(self, nome, quantidade, valor_unitario, data_validade):
        super().__init__(nome, quantidade, valor_unitario)
        self.data_validade = data_validade

    def __str__(self):
        return f"{self.nome} - Validade: {self.data_validade}"


p = Perecivel("Leite", 5, 4.5, "10/11/2025")
print(p)
