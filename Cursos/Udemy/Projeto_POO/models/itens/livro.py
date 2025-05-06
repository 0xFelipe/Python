from models.itens.item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco)
        self.isbn = isbn

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.10) #10% de desconto