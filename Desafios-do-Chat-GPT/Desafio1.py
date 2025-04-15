class Pet:
    def __init__ (self, nome, tipo, energia=100, felicidade=50):
        self.nome = nome
        self.tipo = tipo
        self.energia = energia
        self.felicidade = felicidade

    def brincar(self):
        self.felicidade += 10
        self.energia -= 15

    def comer(self):
        self.energia += 20

    def status (self):
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Energia: {self.energia}")
        print(f"Felicidade: {self.felicidade}")

meu_pet = Pet("Rex", "cachorro")
meu_pet.status()

meu_pet.brincar()
meu_pet.status()

meu_pet.comer()
meu_pet.status()
