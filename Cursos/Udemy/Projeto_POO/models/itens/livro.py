from models.itens.item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco)
        self.isbn = isbn