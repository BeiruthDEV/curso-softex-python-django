from e23 import Inventario
from e21 import ItemInventario
from e22 import Perecivel


def baixo_estoque(self):
    return [i.nome for i in self.estoque if i.quantidade < 5]
