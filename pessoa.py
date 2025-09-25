# 1 - Crie uma class que reserve os atributos de uma pessoa

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def __str__(self):
        return f"Nome: {self.nome} \nIdade: {self.idade} \nCPF: {self.cpf}"

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cpf = input("Digite seu CPF: ")

pessoa1 = Pessoa(nome, idade, cpf)
print("\n---Seus Dados---")
print(pessoa1)