from e21 import ItemInventario
from e22 import Perecivel
from e23 import Inventario


def adicionar(self, item):
    self.estoque.append(item)


def remover(self, nome):
    try:
        for i in self.estoque:
            if i.nome == nome:
                self.estoque.remove(i)
                return
        raise ValueError("Item não encontrado")
    except ValueError as e:
        print(e)
