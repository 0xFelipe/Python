from models.itens.item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, edicao):
        super().__init__(titulo, autor, preco)
        self.edicao = edicao