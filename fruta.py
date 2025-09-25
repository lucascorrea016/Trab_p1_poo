# 2 - Crie uma class que defina um objeto --> qualquer coisa Fruta, Movel, Carro, Moto

class Fruta:
    def __init__(self, nome, cor, sabor, peso):
        self.nome = nome
        self.cor = cor
        self.sabor = sabor
        self.peso = peso

    def descascar(self):
        return f"\nA fruta {self.nome} foi descascada."
    
    def comer(self):
        return f"\nVocê está comendo {self.nome}, que é {self.sabor}."
    
    def __str__(self):
        return f"\n{self.nome} \nCor: {self.cor} \nSabor: {self.sabor} \nPeso: {self.peso}g"
    
fruta1 = Fruta("Maçã", "Vermelha", "doce", 150)

print(fruta1)
print(fruta1.comer())